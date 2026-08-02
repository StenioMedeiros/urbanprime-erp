"""financial and analytics foundation

Revision ID: 0002_financial_analytics
Revises: 0001_initial_schema
Create Date: 2026-08-02
"""

from alembic import op
import sqlalchemy as sa


revision = "0002_financial_analytics"
down_revision = "0001_initial_schema"
branch_labels = None
depends_on = None


def timestamps():
    return (
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("updated_at", sa.DateTime(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
    )


def upgrade() -> None:
    op.create_table(
        "categorias_financeiras",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("codigo", sa.String(30), nullable=False),
        sa.Column("nome", sa.String(120), nullable=False),
        sa.Column("tipo", sa.String(20), nullable=False),
        sa.Column("categoria_pai_id", sa.Integer(), nullable=True),
        sa.Column("descricao", sa.Text(), nullable=True),
        sa.Column("contabilizavel", sa.Boolean(), nullable=False, server_default=sa.text("true")),
        sa.Column("ativo", sa.Boolean(), nullable=False, server_default=sa.text("true")),
        *timestamps(),
        sa.CheckConstraint("tipo IN ('receita', 'despesa', 'ambos')", name="ck_categoria_financeira_tipo"),
        sa.ForeignKeyConstraint(["categoria_pai_id"], ["categorias_financeiras.id"], name="fk_categoria_pai", ondelete="SET NULL"),
        sa.UniqueConstraint("codigo", name="uq_categoria_financeira_codigo"),
        sa.UniqueConstraint("nome", name="uq_categoria_financeira_nome"),
    )
    op.create_index("ix_categoria_financeira_tipo_ativo", "categorias_financeiras", ["tipo", "ativo"])

    op.create_table(
        "centros_custo",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("codigo", sa.String(30), nullable=False),
        sa.Column("nome", sa.String(140), nullable=False),
        sa.Column("tipo", sa.String(30), nullable=False, server_default="obra"),
        sa.Column("obra_id", sa.Integer(), nullable=True),
        sa.Column("responsavel_id", sa.Integer(), nullable=True),
        sa.Column("descricao", sa.Text(), nullable=True),
        sa.Column("ativo", sa.Boolean(), nullable=False, server_default=sa.text("true")),
        *timestamps(),
        sa.ForeignKeyConstraint(["obra_id"], ["obras.id"], name="fk_centro_custo_obra", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["responsavel_id"], ["funcionarios.id"], name="fk_centro_custo_responsavel", ondelete="SET NULL"),
        sa.UniqueConstraint("codigo", name="uq_centro_custo_codigo"),
        sa.UniqueConstraint("obra_id", name="uq_centro_custo_obra"),
    )
    op.create_index("ix_centro_custo_tipo_ativo", "centros_custo", ["tipo", "ativo"])

    op.create_table(
        "contas_bancarias",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("banco", sa.String(120), nullable=False),
        sa.Column("agencia", sa.String(30), nullable=True),
        sa.Column("numero_conta", sa.String(40), nullable=False),
        sa.Column("tipo_conta", sa.String(30), nullable=False, server_default="corrente"),
        sa.Column("descricao", sa.String(160), nullable=True),
        sa.Column("saldo_inicial", sa.Numeric(16, 2), nullable=False, server_default="0"),
        sa.Column("data_saldo_inicial", sa.Date(), nullable=False),
        sa.Column("ativo", sa.Boolean(), nullable=False, server_default=sa.text("true")),
        *timestamps(),
        sa.UniqueConstraint("banco", "agencia", "numero_conta", name="uq_conta_bancaria_identificacao"),
    )

    op.create_table(
        "faturas",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("cliente_id", sa.Integer(), nullable=False),
        sa.Column("contrato_id", sa.Integer(), nullable=True),
        sa.Column("obra_id", sa.Integer(), nullable=True),
        sa.Column("medicao_id", sa.Integer(), nullable=True),
        sa.Column("numero_documento", sa.String(60), nullable=False),
        sa.Column("data_emissao", sa.Date(), nullable=False),
        sa.Column("competencia", sa.String(7), nullable=False),
        sa.Column("valor_bruto", sa.Numeric(16, 2), nullable=False),
        sa.Column("impostos", sa.Numeric(16, 2), nullable=False, server_default="0"),
        sa.Column("retencoes", sa.Numeric(16, 2), nullable=False, server_default="0"),
        sa.Column("valor_liquido", sa.Numeric(16, 2), nullable=False),
        sa.Column("data_vencimento", sa.Date(), nullable=False),
        sa.Column("status", sa.String(30), nullable=False, server_default="emitida"),
        sa.Column("observacao", sa.Text(), nullable=True),
        *timestamps(),
        sa.CheckConstraint("valor_bruto >= 0 AND impostos >= 0 AND retencoes >= 0 AND valor_liquido >= 0", name="ck_fatura_valores"),
        sa.ForeignKeyConstraint(["cliente_id"], ["clientes.id"], name="fk_fatura_cliente", ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["contrato_id"], ["contratos.id"], name="fk_fatura_contrato", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["obra_id"], ["obras.id"], name="fk_fatura_obra", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["medicao_id"], ["medicoes.id"], name="fk_fatura_medicao", ondelete="SET NULL"),
        sa.UniqueConstraint("numero_documento", name="uq_fatura_numero_documento"),
    )
    op.create_index("ix_fatura_competencia_status", "faturas", ["competencia", "status"])
    op.create_index("ix_fatura_obra", "faturas", ["obra_id"])

    op.create_table(
        "itens_orcamento",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("orcamento_base_id", sa.Integer(), nullable=False),
        sa.Column("categoria_financeira_id", sa.Integer(), nullable=True),
        sa.Column("codigo", sa.String(40), nullable=False),
        sa.Column("etapa", sa.String(120), nullable=True),
        sa.Column("descricao", sa.String(200), nullable=False),
        sa.Column("unidade_medida", sa.String(20), nullable=False, server_default="un"),
        sa.Column("quantidade", sa.Numeric(16, 3), nullable=False, server_default="1"),
        sa.Column("valor_unitario", sa.Numeric(16, 2), nullable=False, server_default="0"),
        sa.Column("valor_total", sa.Numeric(16, 2), nullable=False, server_default="0"),
        *timestamps(),
        sa.CheckConstraint("quantidade >= 0 AND valor_unitario >= 0 AND valor_total >= 0", name="ck_item_orcamento_valores"),
        sa.ForeignKeyConstraint(["orcamento_base_id"], ["orcamentos_base.id"], name="fk_item_orcamento_base", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["categoria_financeira_id"], ["categorias_financeiras.id"], name="fk_item_orcamento_categoria", ondelete="SET NULL"),
        sa.UniqueConstraint("orcamento_base_id", "codigo", name="uq_item_orcamento_codigo"),
    )
    op.create_index("ix_item_orcamento_etapa", "itens_orcamento", ["orcamento_base_id", "etapa"])

    op.create_table(
        "metas_indicadores",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("codigo_indicador", sa.String(60), nullable=False),
        sa.Column("nome", sa.String(140), nullable=False),
        sa.Column("competencia", sa.String(7), nullable=False),
        sa.Column("valor_meta", sa.Numeric(18, 4), nullable=False),
        sa.Column("unidade", sa.String(30), nullable=False, server_default="numero"),
        sa.Column("centro_custo_id", sa.Integer(), nullable=True),
        sa.Column("obra_id", sa.Integer(), nullable=True),
        sa.Column("observacao", sa.Text(), nullable=True),
        sa.Column("ativo", sa.Boolean(), nullable=False, server_default=sa.text("true")),
        *timestamps(),
        sa.ForeignKeyConstraint(["centro_custo_id"], ["centros_custo.id"], name="fk_meta_centro_custo", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["obra_id"], ["obras.id"], name="fk_meta_obra", ondelete="SET NULL"),
    )
    op.create_index("ix_meta_indicador_competencia", "metas_indicadores", ["codigo_indicador", "competencia"])

    op.create_table(
        "historicos_status",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("entidade", sa.String(80), nullable=False),
        sa.Column("entidade_id", sa.Integer(), nullable=False),
        sa.Column("status_anterior", sa.String(30), nullable=True),
        sa.Column("status_novo", sa.String(30), nullable=False),
        sa.Column("data_alteracao", sa.DateTime(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("usuario_id", sa.Integer(), nullable=True),
        sa.Column("observacao", sa.Text(), nullable=True),
        *timestamps(),
        sa.ForeignKeyConstraint(["usuario_id"], ["usuarios.id"], name="fk_historico_status_usuario", ondelete="SET NULL"),
    )
    op.create_index("ix_historico_entidade_data", "historicos_status", ["entidade", "entidade_id", "data_alteracao"])

    op.create_table(
        "manutencoes_frota",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("frota_id", sa.Integer(), nullable=False),
        sa.Column("fornecedor_id", sa.Integer(), nullable=True),
        sa.Column("obra_id", sa.Integer(), nullable=True),
        sa.Column("tipo", sa.String(30), nullable=False),
        sa.Column("descricao", sa.Text(), nullable=False),
        sa.Column("data_entrada", sa.Date(), nullable=False),
        sa.Column("data_saida", sa.Date(), nullable=True),
        sa.Column("custo", sa.Numeric(16, 2), nullable=False, server_default="0"),
        sa.Column("horimetro", sa.Numeric(14, 2), nullable=True),
        sa.Column("status", sa.String(30), nullable=False, server_default="aberta"),
        *timestamps(),
        sa.CheckConstraint("custo >= 0", name="ck_manutencao_custo"),
        sa.ForeignKeyConstraint(["frota_id"], ["frotas.id"], name="fk_manutencao_frota", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["fornecedor_id"], ["fornecedores.id"], name="fk_manutencao_fornecedor", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["obra_id"], ["obras.id"], name="fk_manutencao_obra", ondelete="SET NULL"),
    )
    op.create_index("ix_manutencao_frota_data", "manutencoes_frota", ["frota_id", "data_entrada"])

    op.create_table(
        "abastecimentos_frota",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("frota_id", sa.Integer(), nullable=False),
        sa.Column("obra_id", sa.Integer(), nullable=True),
        sa.Column("responsavel_id", sa.Integer(), nullable=True),
        sa.Column("data_abastecimento", sa.Date(), nullable=False),
        sa.Column("litros", sa.Numeric(14, 3), nullable=False),
        sa.Column("valor_total", sa.Numeric(16, 2), nullable=False),
        sa.Column("quilometragem_horimetro", sa.Numeric(14, 2), nullable=True),
        sa.Column("observacao", sa.Text(), nullable=True),
        *timestamps(),
        sa.CheckConstraint("litros > 0 AND valor_total >= 0", name="ck_abastecimento_valores"),
        sa.ForeignKeyConstraint(["frota_id"], ["frotas.id"], name="fk_abastecimento_frota", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["obra_id"], ["obras.id"], name="fk_abastecimento_obra", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["responsavel_id"], ["funcionarios.id"], name="fk_abastecimento_responsavel", ondelete="SET NULL"),
    )
    op.create_index("ix_abastecimento_frota_data", "abastecimentos_frota", ["frota_id", "data_abastecimento"])

    op.create_table(
        "utilizacoes_frota",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("frota_id", sa.Integer(), nullable=False),
        sa.Column("obra_id", sa.Integer(), nullable=True),
        sa.Column("funcionario_id", sa.Integer(), nullable=True),
        sa.Column("data_utilizacao", sa.Date(), nullable=False),
        sa.Column("horas_utilizadas", sa.Numeric(10, 2), nullable=False),
        sa.Column("horimetro_inicial", sa.Numeric(14, 2), nullable=True),
        sa.Column("horimetro_final", sa.Numeric(14, 2), nullable=True),
        sa.Column("custo_hora", sa.Numeric(14, 2), nullable=False, server_default="0"),
        sa.Column("observacao", sa.Text(), nullable=True),
        *timestamps(),
        sa.CheckConstraint("horas_utilizadas >= 0 AND custo_hora >= 0", name="ck_utilizacao_frota_valores"),
        sa.ForeignKeyConstraint(["frota_id"], ["frotas.id"], name="fk_utilizacao_frota", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["obra_id"], ["obras.id"], name="fk_utilizacao_obra", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["funcionario_id"], ["funcionarios.id"], name="fk_utilizacao_funcionario", ondelete="SET NULL"),
    )
    op.create_index("ix_utilizacao_frota_data", "utilizacoes_frota", ["frota_id", "data_utilizacao"])

    op.create_table(
        "alocacoes_funcionario_obra",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("funcionario_id", sa.Integer(), nullable=False),
        sa.Column("obra_id", sa.Integer(), nullable=False),
        sa.Column("centro_custo_id", sa.Integer(), nullable=True),
        sa.Column("funcao", sa.String(120), nullable=True),
        sa.Column("data_inicio", sa.Date(), nullable=False),
        sa.Column("data_fim", sa.Date(), nullable=True),
        sa.Column("custo_hora", sa.Numeric(14, 2), nullable=False, server_default="0"),
        sa.Column("ativo", sa.Boolean(), nullable=False, server_default=sa.text("true")),
        *timestamps(),
        sa.CheckConstraint("custo_hora >= 0", name="ck_alocacao_custo_hora"),
        sa.ForeignKeyConstraint(["funcionario_id"], ["funcionarios.id"], name="fk_alocacao_funcionario", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["obra_id"], ["obras.id"], name="fk_alocacao_obra", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["centro_custo_id"], ["centros_custo.id"], name="fk_alocacao_centro_custo", ondelete="SET NULL"),
    )
    op.create_index("ix_alocacao_obra_ativo", "alocacoes_funcionario_obra", ["obra_id", "ativo"])

    op.add_column("contas_pagar", sa.Column("categoria_financeira_id", sa.Integer(), nullable=True))
    op.add_column("contas_pagar", sa.Column("centro_custo_id", sa.Integer(), nullable=True))
    op.add_column("contas_pagar", sa.Column("data_competencia", sa.Date(), nullable=True))
    op.add_column("contas_pagar", sa.Column("numero_documento", sa.String(60), nullable=True))
    op.create_foreign_key("fk_conta_pagar_categoria", "contas_pagar", "categorias_financeiras", ["categoria_financeira_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key("fk_conta_pagar_centro", "contas_pagar", "centros_custo", ["centro_custo_id"], ["id"], ondelete="SET NULL")
    op.create_index("ix_conta_pagar_competencia", "contas_pagar", ["data_competencia"])

    op.add_column("contas_receber", sa.Column("categoria_financeira_id", sa.Integer(), nullable=True))
    op.add_column("contas_receber", sa.Column("centro_custo_id", sa.Integer(), nullable=True))
    op.add_column("contas_receber", sa.Column("fatura_id", sa.Integer(), nullable=True))
    op.add_column("contas_receber", sa.Column("data_competencia", sa.Date(), nullable=True))
    op.add_column("contas_receber", sa.Column("numero_documento", sa.String(60), nullable=True))
    op.create_foreign_key("fk_conta_receber_categoria", "contas_receber", "categorias_financeiras", ["categoria_financeira_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key("fk_conta_receber_centro", "contas_receber", "centros_custo", ["centro_custo_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key("fk_conta_receber_fatura", "contas_receber", "faturas", ["fatura_id"], ["id"], ondelete="SET NULL")
    op.create_index("ix_conta_receber_competencia", "contas_receber", ["data_competencia"])

    op.add_column("ordens_compra", sa.Column("cotacao_id", sa.Integer(), nullable=True))
    op.add_column("ordens_compra", sa.Column("data_aprovacao", sa.Date(), nullable=True))
    op.add_column("ordens_compra", sa.Column("data_recebimento", sa.Date(), nullable=True))
    op.create_foreign_key("fk_ordem_compra_cotacao", "ordens_compra", "cotacoes", ["cotacao_id"], ["id"], ondelete="SET NULL")

    op.add_column("obras", sa.Column("percentual_fisico", sa.Numeric(5, 2), nullable=False, server_default="0"))
    op.create_check_constraint("ck_obra_percentual_fisico", "obras", "percentual_fisico >= 0 AND percentual_fisico <= 100")
    op.add_column("cronogramas", sa.Column("peso_percentual", sa.Numeric(5, 2), nullable=False, server_default="0"))
    op.create_check_constraint("ck_cronograma_peso", "cronogramas", "peso_percentual >= 0 AND peso_percentual <= 100")

    op.add_column("frotas", sa.Column("marca", sa.String(80), nullable=True))
    op.add_column("frotas", sa.Column("modelo", sa.String(100), nullable=True))
    op.add_column("frotas", sa.Column("ano_fabricacao", sa.Integer(), nullable=True))
    op.add_column("frotas", sa.Column("data_aquisicao", sa.Date(), nullable=True))
    op.add_column("frotas", sa.Column("valor_aquisicao", sa.Numeric(16, 2), nullable=True))
    op.add_column("frotas", sa.Column("horimetro_atual", sa.Numeric(14, 2), nullable=True))

    op.create_table(
        "apropriacoes_custo",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("obra_id", sa.Integer(), nullable=False),
        sa.Column("centro_custo_id", sa.Integer(), nullable=True),
        sa.Column("categoria_financeira_id", sa.Integer(), nullable=False),
        sa.Column("conta_pagar_id", sa.Integer(), nullable=True),
        sa.Column("ordem_compra_id", sa.Integer(), nullable=True),
        sa.Column("funcionario_id", sa.Integer(), nullable=True),
        sa.Column("frota_id", sa.Integer(), nullable=True),
        sa.Column("competencia", sa.String(7), nullable=False),
        sa.Column("data_apropriacao", sa.Date(), nullable=False),
        sa.Column("tipo_custo", sa.String(30), nullable=False),
        sa.Column("descricao", sa.String(200), nullable=False),
        sa.Column("quantidade", sa.Numeric(16, 3), nullable=False, server_default="1"),
        sa.Column("valor_unitario", sa.Numeric(16, 2), nullable=False, server_default="0"),
        sa.Column("valor_total", sa.Numeric(16, 2), nullable=False),
        sa.Column("origem", sa.String(40), nullable=False, server_default="manual"),
        *timestamps(),
        sa.CheckConstraint("quantidade >= 0 AND valor_unitario >= 0 AND valor_total >= 0", name="ck_apropriacao_valores"),
        sa.ForeignKeyConstraint(["obra_id"], ["obras.id"], name="fk_apropriacao_obra", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["centro_custo_id"], ["centros_custo.id"], name="fk_apropriacao_centro", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["categoria_financeira_id"], ["categorias_financeiras.id"], name="fk_apropriacao_categoria", ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["conta_pagar_id"], ["contas_pagar.id"], name="fk_apropriacao_conta_pagar", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["ordem_compra_id"], ["ordens_compra.id"], name="fk_apropriacao_ordem", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["funcionario_id"], ["funcionarios.id"], name="fk_apropriacao_funcionario", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["frota_id"], ["frotas.id"], name="fk_apropriacao_frota", ondelete="SET NULL"),
    )
    op.create_index("ix_apropriacao_obra_competencia", "apropriacoes_custo", ["obra_id", "competencia"])

    op.create_table(
        "movimentacoes_caixa",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("conta_bancaria_id", sa.Integer(), nullable=False),
        sa.Column("conta_pagar_id", sa.Integer(), nullable=True),
        sa.Column("conta_receber_id", sa.Integer(), nullable=True),
        sa.Column("fatura_id", sa.Integer(), nullable=True),
        sa.Column("categoria_financeira_id", sa.Integer(), nullable=False),
        sa.Column("centro_custo_id", sa.Integer(), nullable=True),
        sa.Column("tipo", sa.String(10), nullable=False),
        sa.Column("data_movimentacao", sa.Date(), nullable=False),
        sa.Column("valor", sa.Numeric(16, 2), nullable=False),
        sa.Column("descricao", sa.String(200), nullable=False),
        sa.Column("forma_pagamento", sa.String(40), nullable=True),
        sa.Column("conciliado", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("data_conciliacao", sa.Date(), nullable=True),
        *timestamps(),
        sa.CheckConstraint("tipo IN ('entrada', 'saida')", name="ck_movimentacao_caixa_tipo"),
        sa.CheckConstraint("valor > 0", name="ck_movimentacao_caixa_valor"),
        sa.ForeignKeyConstraint(["conta_bancaria_id"], ["contas_bancarias.id"], name="fk_movimento_conta_bancaria", ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["conta_pagar_id"], ["contas_pagar.id"], name="fk_movimento_conta_pagar", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["conta_receber_id"], ["contas_receber.id"], name="fk_movimento_conta_receber", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["fatura_id"], ["faturas.id"], name="fk_movimento_fatura", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["categoria_financeira_id"], ["categorias_financeiras.id"], name="fk_movimento_categoria", ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["centro_custo_id"], ["centros_custo.id"], name="fk_movimento_centro", ondelete="SET NULL"),
    )
    op.create_index("ix_movimento_caixa_data_tipo", "movimentacoes_caixa", ["data_movimentacao", "tipo"])
    op.create_index("ix_movimento_caixa_centro", "movimentacoes_caixa", ["centro_custo_id"])


def downgrade() -> None:
    op.drop_table("movimentacoes_caixa")
    op.drop_table("apropriacoes_custo")

    for column in ("horimetro_atual", "valor_aquisicao", "data_aquisicao", "ano_fabricacao", "modelo", "marca"):
        op.drop_column("frotas", column)
    op.drop_constraint("ck_cronograma_peso", "cronogramas", type_="check")
    op.drop_column("cronogramas", "peso_percentual")
    op.drop_constraint("ck_obra_percentual_fisico", "obras", type_="check")
    op.drop_column("obras", "percentual_fisico")

    op.drop_constraint("fk_ordem_compra_cotacao", "ordens_compra", type_="foreignkey")
    for column in ("data_recebimento", "data_aprovacao", "cotacao_id"):
        op.drop_column("ordens_compra", column)

    op.drop_index("ix_conta_receber_competencia", table_name="contas_receber")
    for constraint in ("fk_conta_receber_fatura", "fk_conta_receber_centro", "fk_conta_receber_categoria"):
        op.drop_constraint(constraint, "contas_receber", type_="foreignkey")
    for column in ("numero_documento", "data_competencia", "fatura_id", "centro_custo_id", "categoria_financeira_id"):
        op.drop_column("contas_receber", column)

    op.drop_index("ix_conta_pagar_competencia", table_name="contas_pagar")
    for constraint in ("fk_conta_pagar_centro", "fk_conta_pagar_categoria"):
        op.drop_constraint(constraint, "contas_pagar", type_="foreignkey")
    for column in ("numero_documento", "data_competencia", "centro_custo_id", "categoria_financeira_id"):
        op.drop_column("contas_pagar", column)

    for table in (
        "alocacoes_funcionario_obra", "utilizacoes_frota", "abastecimentos_frota",
        "manutencoes_frota", "historicos_status", "metas_indicadores",
        "itens_orcamento", "faturas", "contas_bancarias", "centros_custo",
        "categorias_financeiras",
    ):
        op.drop_table(table)
