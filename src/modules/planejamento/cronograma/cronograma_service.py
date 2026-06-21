from sqlalchemy.orm import Session

from .cronograma_repository import CronogramaRepository
from .cronograma_schema import CronogramaCreate, CronogramaUpdate


class CronogramaService:
    def __init__(self, repository: CronogramaRepository | None = None):
        self.repository = repository or CronogramaRepository()

    def list(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.list(db, skip=skip, limit=limit)

    def get(self, db: Session, item_id: int):
        return self.repository.get(db, item_id)

    def create(self, db: Session, payload: CronogramaCreate):
        return self.repository.create(db, payload.model_dump())

    def update(self, db: Session, item_id: int, payload: CronogramaUpdate):
        return self.repository.update(db, item_id, payload.model_dump(exclude_unset=True))

    def delete(self, db: Session, item_id: int):
        return self.repository.delete(db, item_id)
