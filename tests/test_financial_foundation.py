from datetime import date
from decimal import Decimal

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import src.core.database.all_models  # noqa: F401
from src.core.database.base import Base
from src.modules.comercial.cliente.cliente_model import Cliente
from src.modules.comercial.contrato.contrato_model import Contrato
from src.modules.engenharia.projeto.projeto_model import Projeto
from src.modules.financeiro.conta_receber.conta_receber_model import ContaReceber
from src.modules.financeiro.gestao_financeira.gestao_financeira_model import (
    ApropriacaoCusto, CategoriaFinanceira, CentroCusto, ContaBancaria,
    Fatura, ItemOrcamento, MovimentacaoCaixa,
)
from src.modules.financeiro.orcamento_base.orcamento_base_model import OrcamentoBase
from src.modules.obras.medicao.medicao_model import Medicao
from src.modules.obras.obra.obra_model import Obra


def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()


def test_fluxo_financeiro_da_medicao_ao_caixa():
    db = session()
    cliente = Cliente(nome="Cliente Financeiro", tipo_pessoa="juridica")
    db.add(cliente)
    db.flush()
    contrato = Contrato(cliente_id=cliente.id, numero_contrato="CT-FIN-001", valor_total=Decimal("100000"))
    db.add(contrato)
    db.flush()
    projeto = Projeto(contrato_id=contrato.id, nome="Projeto Financeiro")
    db.add(projeto)
    db.flush()
    obra = Obra(contrato_id=contrato.id, projeto_id=projeto.id, nome="Obra Financeira", percentual_fisico=Decimal("35"))
    db.add(obra)
    db.flush()
    centro = CentroCusto(codigo="OBRA-FIN", nome="Obra Financeira", obra_id=obra.id, tipo="obra")
    receita = CategoriaFinanceira(codigo="REC_TESTE", nome="Receita de teste", tipo="receita")
    despesa = CategoriaFinanceira(codigo="DES_TESTE", nome="Despesa de teste", tipo="despesa")
    conta_bancaria = ContaBancaria(banco="Banco Teste", agencia="1", numero_conta="123", data_saldo_inicial=date(2026, 1, 1))
    db.add_all([centro, receita, despesa, conta_bancaria])
    db.flush()
    medicao = Medicao(obra_id=obra.id, contrato_id=contrato.id, competencia="2026-08", valor_medido=Decimal("25000"))
    db.add(medicao)
    db.flush()
    fatura = Fatura(
        cliente_id=cliente.id, contrato_id=contrato.id, obra_id=obra.id, medicao_id=medicao.id,
        numero_documento="NF-TESTE-001", data_emissao=date(2026, 8, 1), competencia="2026-08",
        valor_bruto=Decimal("25000"), impostos=Decimal("500"), retencoes=Decimal("750"),
        valor_liquido=Decimal("23750"), data_vencimento=date(2026, 8, 31),
    )
    db.add(fatura)
    db.flush()
    recebivel = ContaReceber(
        cliente_id=cliente.id, contrato_id=contrato.id, medicao_id=medicao.id, fatura_id=fatura.id,
        categoria_financeira_id=receita.id, centro_custo_id=centro.id,
        descricao="Recebimento da medição", valor=Decimal("23750"), data_vencimento=date(2026, 8, 31),
    )
    db.add(recebivel)
    db.flush()
    movimento = MovimentacaoCaixa(
        conta_bancaria_id=conta_bancaria.id, conta_receber_id=recebivel.id, fatura_id=fatura.id,
        categoria_financeira_id=receita.id, centro_custo_id=centro.id, tipo="entrada",
        data_movimentacao=date(2026, 8, 31), valor=Decimal("23750"), descricao="Recebimento NF-TESTE-001",
    )
    db.add(movimento)
    db.commit()

    assert movimento.fatura_id == fatura.id
    assert recebivel.centro_custo_id == centro.id
    assert fatura.valor_liquido == Decimal("23750")


def test_previsto_e_realizado_por_obra():
    db = session()
    cliente = Cliente(nome="Cliente Custos", tipo_pessoa="juridica")
    db.add(cliente)
    db.flush()
    contrato = Contrato(cliente_id=cliente.id, numero_contrato="CT-CUSTO-001", valor_total=Decimal("80000"))
    db.add(contrato)
    db.flush()
    projeto = Projeto(contrato_id=contrato.id, nome="Projeto Custos")
    db.add(projeto)
    db.flush()
    obra = Obra(contrato_id=contrato.id, projeto_id=projeto.id, nome="Obra Custos")
    categoria = CategoriaFinanceira(codigo="MAT_TESTE", nome="Materiais teste", tipo="despesa")
    db.add_all([obra, categoria])
    db.flush()
    centro = CentroCusto(codigo="CC-CUSTO", nome="Obra Custos", obra_id=obra.id)
    orcamento = OrcamentoBase(obra_id=obra.id, valor_total=Decimal("50000"))
    db.add_all([centro, orcamento])
    db.flush()
    previsto = ItemOrcamento(
        orcamento_base_id=orcamento.id, categoria_financeira_id=categoria.id, codigo="MAT-001",
        descricao="Materiais", quantidade=Decimal("1"), valor_unitario=Decimal("20000"), valor_total=Decimal("20000"),
    )
    realizado = ApropriacaoCusto(
        obra_id=obra.id, centro_custo_id=centro.id, categoria_financeira_id=categoria.id,
        competencia="2026-08", data_apropriacao=date(2026, 8, 15), tipo_custo="direto",
        descricao="Materiais realizados", quantidade=Decimal("1"), valor_unitario=Decimal("18500"),
        valor_total=Decimal("18500"), origem="manual",
    )
    db.add_all([previsto, realizado])
    db.commit()

    assert previsto.valor_total - realizado.valor_total == Decimal("1500")
