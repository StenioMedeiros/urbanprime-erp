from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.core.config.settings import get_settings
import src.core.database.all_models  # noqa: F401

settings = get_settings()
engine = create_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
