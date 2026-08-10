from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session, sessionmaker

from src.core.config.settings import get_settings
import src.core.database.all_models  # noqa: F401

settings = get_settings()
engine = create_engine(settings.database_url, pool_pre_ping=True)


if engine.dialect.name == "postgresql":
    @event.listens_for(engine, "connect")
    def set_database_timezone(dbapi_connection, _connection_record) -> None:
        cursor = dbapi_connection.cursor()
        try:
            cursor.execute("SET TIME ZONE %s", (settings.app_timezone,))
        finally:
            cursor.close()


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
