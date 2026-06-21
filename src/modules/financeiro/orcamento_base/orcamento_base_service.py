from sqlalchemy.orm import Session

from .orcamento_base_repository import OrcamentoBaseRepository
from .orcamento_base_schema import OrcamentoBaseCreate, OrcamentoBaseUpdate


class OrcamentoBaseService:
    def __init__(self, repository: OrcamentoBaseRepository | None = None):
        self.repository = repository or OrcamentoBaseRepository()

    def list(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.list(db, skip=skip, limit=limit)

    def get(self, db: Session, item_id: int):
        return self.repository.get(db, item_id)

    def create(self, db: Session, payload: OrcamentoBaseCreate):
        return self.repository.create(db, payload.model_dump())

    def update(self, db: Session, item_id: int, payload: OrcamentoBaseUpdate):
        return self.repository.update(db, item_id, payload.model_dump(exclude_unset=True))

    def delete(self, db: Session, item_id: int):
        return self.repository.delete(db, item_id)
