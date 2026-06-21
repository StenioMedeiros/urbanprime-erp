from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sqlalchemy import create_engine, text

from src.core.config.settings import get_settings


TABLES = [
    "registro_ponto", "folha_pagamento", "cronogramas", "frotas", "itens_ordem_compra",
    "ordens_compra", "cotacoes", "fornecedores", "movimentacoes_estoque", "insumos",
    "contas_receber", "contas_pagar", "orcamentos_base", "chamados_tecnicos", "medicoes",
    "diarios_obra", "obras", "revisoes_projeto", "projetos", "agenda_visitas", "contratos",
    "clientes", "logs_auditoria", "tokens_refresh", "sessoes_usuario", "usuario_perfil",
    "perfil_permissao", "permissoes", "perfis", "usuarios", "funcionarios"
]


def main() -> None:
    engine = create_engine(get_settings().database_url)
    with engine.begin() as conn:
        for table in TABLES:
            conn.execute(text(f"DROP TABLE IF EXISTS {table} CASCADE"))
    print("Banco limpo. Execute alembic upgrade head e depois scripts/seed_database.py.")


if __name__ == "__main__":
    main()
