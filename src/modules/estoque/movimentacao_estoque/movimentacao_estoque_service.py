from sqlalchemy.orm import Session

from .movimentacao_estoque_repository import MovimentacaoEstoqueRepository
from .movimentacao_estoque_schema import MovimentacaoEstoqueCreate, MovimentacaoEstoqueUpdate


class MovimentacaoEstoqueService:
    def __init__(self, repository: MovimentacaoEstoqueRepository | None = None):
        self.repository = repository or MovimentacaoEstoqueRepository()

    def list(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.list(db, skip=skip, limit=limit)

    def get(self, db: Session, item_id: int):
        return self.repository.get(db, item_id)

    def create(self, db: Session, payload: MovimentacaoEstoqueCreate):
        return self.repository.create(db, payload.model_dump())

    def update(self, db: Session, item_id: int, payload: MovimentacaoEstoqueUpdate):
        return self.repository.update(db, item_id, payload.model_dump(exclude_unset=True))

    def delete(self, db: Session, item_id: int):
        return self.repository.delete(db, item_id)
