from sqlalchemy import Boolean, CheckConstraint, Column, Date, DateTime, ForeignKey, Index, Integer, Numeric, String, Text, UniqueConstraint

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class CategoriaFinanceira(TimestampMixin, Base):
    __tablename__ = "categorias_financeiras"
    __table_args__ = (
        CheckConstraint("tipo IN ('receita', 'despesa', 'ambos')", name="ck_categoria_financeira_tipo"),
        Index("ix_categoria_financeira_tipo_ativo", "tipo", "ativo"),
    )

    id = Column(Integer, primary_key=True)
    codigo = Column(String(30), nullable=False, unique=True)
    nome = Column(String(120), nullable=False, unique=True)
    tipo = Column(String(20), nullable=False)
    categoria_pai_id = Column(ForeignKey("categorias_financeiras.id", ondelete="SET NULL"), nullable=True)
    descricao = Column(Text, nullable=True)
    contabilizavel = Column(Boolean, nullable=False, default=True)
    ativo = Column(Boolean, nullable=False, default=True)


class CentroCusto(TimestampMixin, Base):
    __tablename__ = "centros_custo"
    __table_args__ = (Index("ix_centro_custo_tipo_ativo", "tipo", "ativo"),)

    id = Column(Integer, primary_key=True)
    codigo = Column(String(30), nullable=False, unique=True)
    nome = Column(String(140), nullable=False)
    tipo = Column(String(30), nullable=False, default="obra")
    obra_id = Column(ForeignKey("obras.id", ondelete="SET NULL"), nullable=True, unique=True)
    responsavel_id = Column(ForeignKey("funcionarios.id", ondelete="SET NULL"), nullable=True)
    descricao = Column(Text, nullable=True)
    ativo = Column(Boolean, nullable=False, default=True)


class ContaBancaria(TimestampMixin, Base):
    __tablename__ = "contas_bancarias"
    __table_args__ = (
        UniqueConstraint("banco", "agencia", "numero_conta", name="uq_conta_bancaria_identificacao"),
    )

    id = Column(Integer, primary_key=True)
    banco = Column(String(120), nullable=False)
    agencia = Column(String(30), nullable=True)
    numero_conta = Column(String(40), nullable=False)
    tipo_conta = Column(String(30), nullable=False, default="corrente")
    descricao = Column(String(160), nullable=True)
    saldo_inicial = Column(Numeric(16, 2), nullable=False, default=0)
    data_saldo_inicial = Column(Date, nullable=False)
    ativo = Column(Boolean, nullable=False, default=True)


class Fatura(TimestampMixin, Base):
    __tablename__ = "faturas"
    __table_args__ = (
        Index("ix_fatura_competencia_status", "competencia", "status"),
        Index("ix_fatura_obra", "obra_id"),
    )

    id = Column(Integer, primary_key=True)
    cliente_id = Column(ForeignKey("clientes.id", ondelete="RESTRICT"), nullable=False)
    contrato_id = Column(ForeignKey("contratos.id", ondelete="SET NULL"), nullable=True)
    obra_id = Column(ForeignKey("obras.id", ondelete="SET NULL"), nullable=True)
    medicao_id = Column(ForeignKey("medicoes.id", ondelete="SET NULL"), nullable=True)
    numero_documento = Column(String(60), nullable=False, unique=True)
    data_emissao = Column(Date, nullable=False)
    competencia = Column(String(7), nullable=False)
    valor_bruto = Column(Numeric(16, 2), nullable=False)
    impostos = Column(Numeric(16, 2), nullable=False, default=0)
    retencoes = Column(Numeric(16, 2), nullable=False, default=0)
    valor_liquido = Column(Numeric(16, 2), nullable=False)
    data_vencimento = Column(Date, nullable=False)
    status = Column(String(30), nullable=False, default="emitida")
    observacao = Column(Text, nullable=True)


class MovimentacaoCaixa(TimestampMixin, Base):
    __tablename__ = "movimentacoes_caixa"
    __table_args__ = (
        CheckConstraint("tipo IN ('entrada', 'saida')", name="ck_movimentacao_caixa_tipo"),
        CheckConstraint("valor > 0", name="ck_movimentacao_caixa_valor"),
        Index("ix_movimento_caixa_data_tipo", "data_movimentacao", "tipo"),
        Index("ix_movimento_caixa_centro", "centro_custo_id"),
    )

    id = Column(Integer, primary_key=True)
    conta_bancaria_id = Column(ForeignKey("contas_bancarias.id", ondelete="RESTRICT"), nullable=False)
    conta_pagar_id = Column(ForeignKey("contas_pagar.id", ondelete="SET NULL"), nullable=True)
    conta_receber_id = Column(ForeignKey("contas_receber.id", ondelete="SET NULL"), nullable=True)
    fatura_id = Column(ForeignKey("faturas.id", ondelete="SET NULL"), nullable=True)
    categoria_financeira_id = Column(ForeignKey("categorias_financeiras.id", ondelete="RESTRICT"), nullable=False)
    centro_custo_id = Column(ForeignKey("centros_custo.id", ondelete="SET NULL"), nullable=True)
    tipo = Column(String(10), nullable=False)
    data_movimentacao = Column(Date, nullable=False)
    valor = Column(Numeric(16, 2), nullable=False)
    descricao = Column(String(200), nullable=False)
    forma_pagamento = Column(String(40), nullable=True)
    conciliado = Column(Boolean, nullable=False, default=False)
    data_conciliacao = Column(Date, nullable=True)


class ItemOrcamento(TimestampMixin, Base):
    __tablename__ = "itens_orcamento"
    __table_args__ = (
        UniqueConstraint("orcamento_base_id", "codigo", name="uq_item_orcamento_codigo"),
        Index("ix_item_orcamento_etapa", "orcamento_base_id", "etapa"),
    )

    id = Column(Integer, primary_key=True)
    orcamento_base_id = Column(ForeignKey("orcamentos_base.id", ondelete="CASCADE"), nullable=False)
    categoria_financeira_id = Column(ForeignKey("categorias_financeiras.id", ondelete="SET NULL"), nullable=True)
    codigo = Column(String(40), nullable=False)
    etapa = Column(String(120), nullable=True)
    descricao = Column(String(200), nullable=False)
    unidade_medida = Column(String(20), nullable=False, default="un")
    quantidade = Column(Numeric(16, 3), nullable=False, default=1)
    valor_unitario = Column(Numeric(16, 2), nullable=False, default=0)
    valor_total = Column(Numeric(16, 2), nullable=False, default=0)


class ApropriacaoCusto(TimestampMixin, Base):
    __tablename__ = "apropriacoes_custo"
    __table_args__ = (Index("ix_apropriacao_obra_competencia", "obra_id", "competencia"),)

    id = Column(Integer, primary_key=True)
    obra_id = Column(ForeignKey("obras.id", ondelete="CASCADE"), nullable=False)
    centro_custo_id = Column(ForeignKey("centros_custo.id", ondelete="SET NULL"), nullable=True)
    categoria_financeira_id = Column(ForeignKey("categorias_financeiras.id", ondelete="RESTRICT"), nullable=False)
    conta_pagar_id = Column(ForeignKey("contas_pagar.id", ondelete="SET NULL"), nullable=True)
    ordem_compra_id = Column(ForeignKey("ordens_compra.id", ondelete="SET NULL"), nullable=True)
    funcionario_id = Column(ForeignKey("funcionarios.id", ondelete="SET NULL"), nullable=True)
    frota_id = Column(ForeignKey("frotas.id", ondelete="SET NULL"), nullable=True)
    competencia = Column(String(7), nullable=False)
    data_apropriacao = Column(Date, nullable=False)
    tipo_custo = Column(String(30), nullable=False)
    descricao = Column(String(200), nullable=False)
    quantidade = Column(Numeric(16, 3), nullable=False, default=1)
    valor_unitario = Column(Numeric(16, 2), nullable=False, default=0)
    valor_total = Column(Numeric(16, 2), nullable=False)
    origem = Column(String(40), nullable=False, default="manual")


class MetaIndicador(TimestampMixin, Base):
    __tablename__ = "metas_indicadores"
    __table_args__ = (Index("ix_meta_indicador_competencia", "codigo_indicador", "competencia"),)

    id = Column(Integer, primary_key=True)
    codigo_indicador = Column(String(60), nullable=False)
    nome = Column(String(140), nullable=False)
    competencia = Column(String(7), nullable=False)
    valor_meta = Column(Numeric(18, 4), nullable=False)
    unidade = Column(String(30), nullable=False, default="numero")
    centro_custo_id = Column(ForeignKey("centros_custo.id", ondelete="SET NULL"), nullable=True)
    obra_id = Column(ForeignKey("obras.id", ondelete="SET NULL"), nullable=True)
    observacao = Column(Text, nullable=True)
    ativo = Column(Boolean, nullable=False, default=True)


class HistoricoStatus(TimestampMixin, Base):
    __tablename__ = "historicos_status"
    __table_args__ = (Index("ix_historico_entidade_data", "entidade", "entidade_id", "data_alteracao"),)

    id = Column(Integer, primary_key=True)
    entidade = Column(String(80), nullable=False)
    entidade_id = Column(Integer, nullable=False)
    status_anterior = Column(String(30), nullable=True)
    status_novo = Column(String(30), nullable=False)
    data_alteracao = Column(DateTime, nullable=False)
    usuario_id = Column(ForeignKey("usuarios.id", ondelete="SET NULL"), nullable=True)
    observacao = Column(Text, nullable=True)


class ManutencaoFrota(TimestampMixin, Base):
    __tablename__ = "manutencoes_frota"
    __table_args__ = (Index("ix_manutencao_frota_data", "frota_id", "data_entrada"),)

    id = Column(Integer, primary_key=True)
    frota_id = Column(ForeignKey("frotas.id", ondelete="CASCADE"), nullable=False)
    fornecedor_id = Column(ForeignKey("fornecedores.id", ondelete="SET NULL"), nullable=True)
    obra_id = Column(ForeignKey("obras.id", ondelete="SET NULL"), nullable=True)
    tipo = Column(String(30), nullable=False)
    descricao = Column(Text, nullable=False)
    data_entrada = Column(Date, nullable=False)
    data_saida = Column(Date, nullable=True)
    custo = Column(Numeric(16, 2), nullable=False, default=0)
    horimetro = Column(Numeric(14, 2), nullable=True)
    status = Column(String(30), nullable=False, default="aberta")


class AbastecimentoFrota(TimestampMixin, Base):
    __tablename__ = "abastecimentos_frota"
    __table_args__ = (Index("ix_abastecimento_frota_data", "frota_id", "data_abastecimento"),)

    id = Column(Integer, primary_key=True)
    frota_id = Column(ForeignKey("frotas.id", ondelete="CASCADE"), nullable=False)
    obra_id = Column(ForeignKey("obras.id", ondelete="SET NULL"), nullable=True)
    responsavel_id = Column(ForeignKey("funcionarios.id", ondelete="SET NULL"), nullable=True)
    data_abastecimento = Column(Date, nullable=False)
    litros = Column(Numeric(14, 3), nullable=False)
    valor_total = Column(Numeric(16, 2), nullable=False)
    quilometragem_horimetro = Column(Numeric(14, 2), nullable=True)
    observacao = Column(Text, nullable=True)


class UtilizacaoFrota(TimestampMixin, Base):
    __tablename__ = "utilizacoes_frota"
    __table_args__ = (Index("ix_utilizacao_frota_data", "frota_id", "data_utilizacao"),)

    id = Column(Integer, primary_key=True)
    frota_id = Column(ForeignKey("frotas.id", ondelete="CASCADE"), nullable=False)
    obra_id = Column(ForeignKey("obras.id", ondelete="SET NULL"), nullable=True)
    funcionario_id = Column(ForeignKey("funcionarios.id", ondelete="SET NULL"), nullable=True)
    data_utilizacao = Column(Date, nullable=False)
    horas_utilizadas = Column(Numeric(10, 2), nullable=False)
    horimetro_inicial = Column(Numeric(14, 2), nullable=True)
    horimetro_final = Column(Numeric(14, 2), nullable=True)
    custo_hora = Column(Numeric(14, 2), nullable=False, default=0)
    observacao = Column(Text, nullable=True)


class AlocacaoFuncionarioObra(TimestampMixin, Base):
    __tablename__ = "alocacoes_funcionario_obra"
    __table_args__ = (Index("ix_alocacao_obra_ativo", "obra_id", "ativo"),)

    id = Column(Integer, primary_key=True)
    funcionario_id = Column(ForeignKey("funcionarios.id", ondelete="CASCADE"), nullable=False)
    obra_id = Column(ForeignKey("obras.id", ondelete="CASCADE"), nullable=False)
    centro_custo_id = Column(ForeignKey("centros_custo.id", ondelete="SET NULL"), nullable=True)
    funcao = Column(String(120), nullable=True)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=True)
    custo_hora = Column(Numeric(14, 2), nullable=False, default=0)
    ativo = Column(Boolean, nullable=False, default=True)


