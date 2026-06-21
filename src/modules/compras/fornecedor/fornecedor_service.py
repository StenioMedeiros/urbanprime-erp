from sqlalchemy.orm import Session

from .fornecedor_repository import FornecedorRepository
from .fornecedor_schema import FornecedorCreate, FornecedorUpdate


class FornecedorService:
    def __init__(self, repository: FornecedorRepository | None = None):
        self.repository = repository or FornecedorRepository()

    def list(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.list(db, skip=skip, limit=limit)

    def get(self, db: Session, item_id: int):
        return self.repository.get(db, item_id)

    def create(self, db: Session, payload: FornecedorCreate):
        return self.repository.create(db, payload.model_dump())

    def update(self, db: Session, item_id: int, payload: FornecedorUpdate):
        return self.repository.update(db, item_id, payload.model_dump(exclude_unset=True))

    def delete(self, db: Session, item_id: int):
        return self.repository.delete(db, item_id)
