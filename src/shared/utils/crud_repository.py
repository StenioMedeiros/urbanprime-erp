from typing import Generic, TypeVar

from sqlalchemy.orm import Session

from src.core.audit.audit_logger import add_audit_log, get_audit_context, model_snapshot

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
        db.flush()
        self._audit(db, "criar", item, dados_novos=model_snapshot(item))
        db.commit()
        db.refresh(item)
        return item

    def update(self, db: Session, item_id: int, data: dict) -> ModelT | None:
        item = self.get(db, item_id)
        if item is None:
            return None
        before = model_snapshot(item)
        for key, value in data.items():
            setattr(item, key, value)
        db.flush()
        self._audit(
            db,
            "editar",
            item,
            dados_anteriores=before,
            dados_novos=model_snapshot(item),
        )
        db.commit()
        db.refresh(item)
        return item

    def delete(self, db: Session, item_id: int) -> bool:
        item = self.get(db, item_id)
        if item is None:
            return False
        before = model_snapshot(item)
        entity_id = getattr(item, "id", item_id)
        db.delete(item)
        self._audit(
            db,
            "excluir",
            item,
            entity_id=entity_id,
            dados_anteriores=before,
        )
        db.commit()
        return True

    def _audit(
        self,
        db: Session,
        action: str,
        item: ModelT,
        *,
        entity_id: int | None = None,
        dados_anteriores: dict | None = None,
        dados_novos: dict | None = None,
    ) -> None:
        context = get_audit_context(db)
        if context is None or self.model.__tablename__ == "logs_auditoria":
            return
        entity_name = self.model.__tablename__
        action_description = {
            "criar": "criado",
            "editar": "editado",
            "excluir": "excluído",
        }.get(action, action)
        add_audit_log(
            db,
            usuario_id=context["usuario_id"],
            modulo=context["modulo"],
            acao=action,
            entidade=entity_name,
            entidade_id=entity_id if entity_id is not None else getattr(item, "id", None),
            descricao=f"Registro {action_description} em {context['modulo']}",
            dados_anteriores=dados_anteriores,
            dados_novos=dados_novos,
        )
