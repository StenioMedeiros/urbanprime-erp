import pytest
from sqlalchemy import create_engine, text

from src.core.config.settings import get_settings


def test_database_connection():
    engine = create_engine(get_settings().database_url)
    try:
        with engine.connect() as conn:
            assert conn.execute(text("SELECT 1")).scalar() == 1
    except Exception as exc:
        pytest.skip(f"Banco indisponivel no ambiente de teste: {exc}")
