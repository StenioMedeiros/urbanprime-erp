from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.database.connection import get_db
from src.core.security.permissions import require_permission
from .frota_schema import FrotaCreate, FrotaRead, FrotaUpdate
from .frota_service import FrotaService

router = APIRouter(prefix="/frotas", tags=["Planejamento - Frotas"])
service = FrotaService()


@router.get("/", response_model=list[FrotaRead])
def list_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), _user=Depends(require_permission("planejamento", "visualizar"))):
    return service.list(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=FrotaRead)
def get_item(item_id: int, db: Session = Depends(get_db), _user=Depends(require_permission("planejamento", "visualizar"))):
    item = service.get(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return item


@router.post("/", response_model=FrotaRead, status_code=status.HTTP_201_CREATED)
def create_item(payload: FrotaCreate, db: Session = Depends(get_db), _user=Depends(require_permission("planejamento", "criar"))):
    return service.create(db, payload)


@router.put("/{item_id}", response_model=FrotaRead)
def update_item(item_id: int, payload: FrotaUpdate, db: Session = Depends(get_db), _user=Depends(require_permission("planejamento", "editar"))):
    item = service.update(db, item_id, payload)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db), _user=Depends(require_permission("planejamento", "excluir"))):
    if not service.delete(db, item_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return None
