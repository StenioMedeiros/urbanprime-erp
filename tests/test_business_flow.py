from datetime import date
from decimal import Decimal

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import src.core.database.all_models  # noqa: F401
from src.core.database.base import Base
from src.modules.comercial.cliente.cliente_model import Cliente
from src.modules.comercial.contrato.contrato_model import Contrato
from src.modules.compras.fornecedor.fornecedor_model import Fornecedor
from src.modules.compras.ordem_compra.ordem_compra_model import OrdemCompra
from src.modules.engenharia.projeto.projeto_model import Projeto
from src.modules.financeiro.conta_pagar.conta_pagar_model import ContaPagar
from src.modules.financeiro.orcamento_base.orcamento_base_model import OrcamentoBase
from src.modules.obras.obra.obra_model import Obra


def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()


def test_fluxo_cliente_contrato_projeto_obra_orcamento():
    db = session()
    cliente = Cliente(nome="Cliente Teste", tipo_pessoa="juridica")
    db.add(cliente)
    db.commit()
    contrato = Contrato(cliente_id=cliente.id, numero_contrato="CT-001", valor_total=Decimal("1000"))
    db.add(contrato)
    db.commit()
    projeto = Projeto(contrato_id=contrato.id, nome="Projeto Teste")
    db.add(projeto)
    db.commit()
    obra = Obra(contrato_id=contrato.id, projeto_id=projeto.id, nome="Obra Teste")
    db.add(obra)
    db.commit()
    orcamento = OrcamentoBase(obra_id=obra.id, valor_total=Decimal("1000"))
    db.add(orcamento)
    db.commit()
    assert obra.contrato_id == contrato.id
    assert obra.projeto_id == projeto.id
    assert orcamento.obra_id == obra.id


def test_vinculo_ordem_compra_conta_pagar():
    db = session()
    fornecedor = Fornecedor(razao_social="Fornecedor Teste")
    db.add(fornecedor)
    db.commit()
    oc = OrdemCompra(fornecedor_id=fornecedor.id, numero="OC-001", valor_total=Decimal("500"))
    db.add(oc)
    db.commit()
    conta = ContaPagar(ordem_compra_id=oc.id, fornecedor_id=fornecedor.id, descricao="Compra teste", valor=Decimal("500"), data_vencimento=date(2026, 6, 30))
    db.add(conta)
    db.commit()
    assert conta.ordem_compra_id == oc.id
