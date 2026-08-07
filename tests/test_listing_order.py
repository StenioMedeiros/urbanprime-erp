from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.database.base import Base
from src.modules.comercial.cliente.cliente_model import Cliente
from src.shared.utils.crud_repository import CRUDRepository


def test_crud_list_returns_newest_records_first():
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

        rows = CRUDRepository(Cliente).list(db, skip=0, limit=100)

        assert [row.nome for row in rows] == [
            "Cliente mais recente",
            "Cliente intermediário",
            "Cliente antigo",
        ]
    finally:
        db.close()
