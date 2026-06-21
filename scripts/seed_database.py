from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sqlalchemy import create_engine, text

from src.core.config.settings import get_settings


def main() -> None:
    engine = create_engine(get_settings().database_url)
    sql = Path("src/core/database/seed.sql").read_text(encoding="utf-8")
    with engine.begin() as conn:
        conn.execute(text(sql))
    print("Seed executado com sucesso.")


if __name__ == "__main__":
    main()
