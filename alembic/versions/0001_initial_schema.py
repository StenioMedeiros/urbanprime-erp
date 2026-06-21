"""initial schema

Revision ID: 0001_initial_schema
Revises:
Create Date: 2026-06-19
"""
from pathlib import Path

from alembic import op

revision = "0001_initial_schema"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    schema = Path("src/core/database/schema.sql").read_text(encoding="utf-8")
    for statement in [part.strip() for part in schema.split(";") if part.strip()]:
        op.execute(statement)


def downgrade() -> None:
    tables = [
        "registro_ponto", "folha_pagamento", "cronogramas", "frotas", "itens_ordem_compra",
        "ordens_compra", "cotacoes", "fornecedores", "movimentacoes_estoque", "insumos",
        "contas_receber", "contas_pagar", "orcamentos_base", "chamados_tecnicos", "medicoes",
        "diarios_obra", "obras", "revisoes_projeto", "projetos", "agenda_visitas", "contratos",
        "clientes", "logs_auditoria", "tokens_refresh", "sessoes_usuario", "usuario_perfil",
        "perfil_permissao", "permissoes", "perfis", "usuarios", "funcionarios"
    ]
    for table in tables:
        op.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
