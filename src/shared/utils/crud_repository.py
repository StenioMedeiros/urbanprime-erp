from typing import Generic, TypeVar

from sqlalchemy.orm import Session

ModelT = TypeVar("ModelT")


class CRUDRepository(Generic[ModelT]):
    def __init__(self, model: type[ModelT]):
        self.model = model

    def list(self, db: Session, skip: int = 0, limit: int = 100) -> list[ModelT]:
        query = db.query(self.model)
        order_columns = []
        if hasattr(self.model, "updated_at"):
            order_columns.append(self.model.updated_at.desc())
        if hasattr(self.model, "created_at"):
            order_columns.append(self.model.created_at.desc())
        if hasattr(self.model, "id"):
            order_columns.append(self.model.id.desc())
        if order_columns:
            query = query.order_by(*order_columns)
        return query.offset(skip).limit(limit).all()

    def get(self, db: Session, item_id: int) -> ModelT | None:
        return db.get(self.model, item_id)

    def create(self, db: Session, data: dict) -> ModelT:
        item = self.model(**data)
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    def update(self, db: Session, item_id: int, data: dict) -> ModelT | None:
        item = self.get(db, item_id)
        if item is None:
            return None
        for key, value in data.items():
            setattr(item, key, value)
        db.commit()
        db.refresh(item)
        return item

    def delete(self, db: Session, item_id: int) -> bool:
        item = self.get(db, item_id)
        if item is None:
            return False
        db.delete(item)
        db.commit()
        return True
