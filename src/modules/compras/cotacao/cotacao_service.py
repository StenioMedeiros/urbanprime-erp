from sqlalchemy.orm import Session

from .cotacao_repository import CotacaoRepository
from .cotacao_schema import CotacaoCreate, CotacaoUpdate


class CotacaoService:
    def __init__(self, repository: CotacaoRepository | None = None):
        self.repository = repository or CotacaoRepository()

    def list(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.list(db, skip=skip, limit=limit)

    def get(self, db: Session, item_id: int):
        return self.repository.get(db, item_id)

    def create(self, db: Session, payload: CotacaoCreate):
        return self.repository.create(db, payload.model_dump())

    def update(self, db: Session, item_id: int, payload: CotacaoUpdate):
        return self.repository.update(db, item_id, payload.model_dump(exclude_unset=True))

    def delete(self, db: Session, item_id: int):
        return self.repository.delete(db, item_id)
