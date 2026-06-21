from sqlalchemy.orm import Session

from .diario_obra_repository import DiarioObraRepository
from .diario_obra_schema import DiarioObraCreate, DiarioObraUpdate


class DiarioObraService:
    def __init__(self, repository: DiarioObraRepository | None = None):
        self.repository = repository or DiarioObraRepository()

    def list(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.list(db, skip=skip, limit=limit)

    def get(self, db: Session, item_id: int):
        return self.repository.get(db, item_id)

    def create(self, db: Session, payload: DiarioObraCreate):
        return self.repository.create(db, payload.model_dump())

    def update(self, db: Session, item_id: int, payload: DiarioObraUpdate):
        return self.repository.update(db, item_id, payload.model_dump(exclude_unset=True))

    def delete(self, db: Session, item_id: int):
        return self.repository.delete(db, item_id)
