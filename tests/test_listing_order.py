from datetime import UTC, datetime, timedelta

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.database.base import Base
from src.modules.comercial.cliente.cliente_model import Cliente
from src.shared.utils.crud_repository import CRUDRepository


def test_crud_list_returns_most_recently_modified_records_first():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine, tables=[Cliente.__table__])
    db = sessionmaker(bind=engine)()
    try:
        db.add_all(
            [
                Cliente(nome="Cliente antigo", tipo_pessoa="juridica"),
                Cliente(nome="Cliente intermediário", tipo_pessoa="juridica"),
                Cliente(nome="Cliente mais recente", tipo_pessoa="juridica"),
            ]
        )
        db.commit()

        oldest = db.query(Cliente).filter_by(nome="Cliente antigo").one()
        oldest.nome = "Cliente antigo atualizado"
        oldest.updated_at = datetime.now(UTC).replace(tzinfo=None) + timedelta(seconds=1)
        db.commit()

        rows = CRUDRepository(Cliente).list(db, skip=0, limit=100)

        assert [row.nome for row in rows] == [
            "Cliente antigo atualizado",
            "Cliente mais recente",
            "Cliente intermediário",
        ]
    finally:
        db.close()
