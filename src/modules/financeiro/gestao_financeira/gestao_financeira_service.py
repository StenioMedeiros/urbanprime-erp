from pydantic import BaseModel
from sqlalchemy.orm import Session

from src.shared.utils.crud_repository import CRUDRepository


class GestaoFinanceiraService:
    def __init__(self, model):
        self.repository = CRUDRepository(model)

    def list(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.list(db, skip=skip, limit=limit)

    def get(self, db: Session, item_id: int):
        return self.repository.get(db, item_id)

    def create(self, db: Session, payload: BaseModel):
        return self.repository.create(db, payload.model_dump())

    def update(self, db: Session, item_id: int, payload: BaseModel):
        return self.repository.update(db, item_id, payload.model_dump(exclude_unset=True))

    def delete(self, db: Session, item_id: int):
        return self.repository.delete(db, item_id)
