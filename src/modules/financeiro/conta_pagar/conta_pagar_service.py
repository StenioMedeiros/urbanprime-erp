from sqlalchemy.orm import Session

from .conta_pagar_repository import ContaPagarRepository
from .conta_pagar_schema import ContaPagarCreate, ContaPagarUpdate


class ContaPagarService:
    def __init__(self, repository: ContaPagarRepository | None = None):
        self.repository = repository or ContaPagarRepository()

    def list(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.list(db, skip=skip, limit=limit)

    def get(self, db: Session, item_id: int):
        return self.repository.get(db, item_id)

    def create(self, db: Session, payload: ContaPagarCreate):
        return self.repository.create(db, payload.model_dump())

    def update(self, db: Session, item_id: int, payload: ContaPagarUpdate):
        return self.repository.update(db, item_id, payload.model_dump(exclude_unset=True))

    def delete(self, db: Session, item_id: int):
        return self.repository.delete(db, item_id)
