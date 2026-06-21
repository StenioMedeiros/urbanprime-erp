from sqlalchemy.orm import Session

from .ordem_compra_repository import OrdemCompraRepository
from .ordem_compra_schema import OrdemCompraCreate, OrdemCompraUpdate


class OrdemCompraService:
    def __init__(self, repository: OrdemCompraRepository | None = None):
        self.repository = repository or OrdemCompraRepository()

    def list(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.list(db, skip=skip, limit=limit)

    def get(self, db: Session, item_id: int):
        return self.repository.get(db, item_id)

    def create(self, db: Session, payload: OrdemCompraCreate):
        return self.repository.create(db, payload.model_dump())

    def update(self, db: Session, item_id: int, payload: OrdemCompraUpdate):
        return self.repository.update(db, item_id, payload.model_dump(exclude_unset=True))

    def delete(self, db: Session, item_id: int):
        return self.repository.delete(db, item_id)
