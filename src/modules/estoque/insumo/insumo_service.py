from sqlalchemy.orm import Session

from .insumo_repository import InsumoRepository
from .insumo_schema import InsumoCreate, InsumoUpdate


class InsumoService:
    def __init__(self, repository: InsumoRepository | None = None):
        self.repository = repository or InsumoRepository()

    def list(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.list(db, skip=skip, limit=limit)

    def get(self, db: Session, item_id: int):
        return self.repository.get(db, item_id)

    def create(self, db: Session, payload: InsumoCreate):
        return self.repository.create(db, payload.model_dump())

    def update(self, db: Session, item_id: int, payload: InsumoUpdate):
        return self.repository.update(db, item_id, payload.model_dump(exclude_unset=True))

    def delete(self, db: Session, item_id: int):
        return self.repository.delete(db, item_id)
