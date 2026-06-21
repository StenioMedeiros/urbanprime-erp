from sqlalchemy.orm import Session

from .medicao_repository import MedicaoRepository
from .medicao_schema import MedicaoCreate, MedicaoUpdate


class MedicaoService:
    def __init__(self, repository: MedicaoRepository | None = None):
        self.repository = repository or MedicaoRepository()

    def list(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.list(db, skip=skip, limit=limit)

    def get(self, db: Session, item_id: int):
        return self.repository.get(db, item_id)

    def create(self, db: Session, payload: MedicaoCreate):
        return self.repository.create(db, payload.model_dump())

    def update(self, db: Session, item_id: int, payload: MedicaoUpdate):
        return self.repository.update(db, item_id, payload.model_dump(exclude_unset=True))

    def delete(self, db: Session, item_id: int):
        return self.repository.delete(db, item_id)
