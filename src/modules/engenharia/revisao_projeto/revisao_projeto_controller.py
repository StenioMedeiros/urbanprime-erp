from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.database.connection import get_db
from src.core.security.permissions import require_permission
from .revisao_projeto_schema import RevisaoProjetoCreate, RevisaoProjetoRead, RevisaoProjetoUpdate
from .revisao_projeto_service import RevisaoProjetoService

router = APIRouter(prefix="/revisoes-projeto", tags=["Engenharia - Revisoes"])
service = RevisaoProjetoService()


@router.get("/", response_model=list[RevisaoProjetoRead])
def list_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), _user=Depends(require_permission("engenharia", "visualizar"))):
    return service.list(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=RevisaoProjetoRead)
def get_item(item_id: int, db: Session = Depends(get_db), _user=Depends(require_permission("engenharia", "visualizar"))):
    item = service.get(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return item


@router.post("/", response_model=RevisaoProjetoRead, status_code=status.HTTP_201_CREATED)
def create_item(payload: RevisaoProjetoCreate, db: Session = Depends(get_db), _user=Depends(require_permission("engenharia", "criar"))):
    return service.create(db, payload)


@router.put("/{item_id}", response_model=RevisaoProjetoRead)
def update_item(item_id: int, payload: RevisaoProjetoUpdate, db: Session = Depends(get_db), _user=Depends(require_permission("engenharia", "editar"))):
    item = service.update(db, item_id, payload)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db), _user=Depends(require_permission("engenharia", "excluir"))):
    if not service.delete(db, item_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return None
