from sqlalchemy.orm import Session

from .conta_receber_repository import ContaReceberRepository
from .conta_receber_schema import ContaReceberCreate, ContaReceberUpdate


class ContaReceberService:
    def __init__(self, repository: ContaReceberRepository | None = None):
        self.repository = repository or ContaReceberRepository()

    def list(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.list(db, skip=skip, limit=limit)

    def get(self, db: Session, item_id: int):
        return self.repository.get(db, item_id)

    def create(self, db: Session, payload: ContaReceberCreate):
        return self.repository.create(db, payload.model_dump())

    def update(self, db: Session, item_id: int, payload: ContaReceberUpdate):
        return self.repository.update(db, item_id, payload.model_dump(exclude_unset=True))

    def delete(self, db: Session, item_id: int):
        return self.repository.delete(db, item_id)
