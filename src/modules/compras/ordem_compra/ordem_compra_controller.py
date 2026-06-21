from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.database.connection import get_db
from src.core.security.permissions import require_permission
from .ordem_compra_schema import OrdemCompraCreate, OrdemCompraRead, OrdemCompraUpdate
from .ordem_compra_service import OrdemCompraService

router = APIRouter(prefix="/ordens-compra", tags=["Compras - Ordens de Compra"])
service = OrdemCompraService()


@router.get("/", response_model=list[OrdemCompraRead])
def list_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), _user=Depends(require_permission("compras", "visualizar"))):
    return service.list(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=OrdemCompraRead)
def get_item(item_id: int, db: Session = Depends(get_db), _user=Depends(require_permission("compras", "visualizar"))):
    item = service.get(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return item


@router.post("/", response_model=OrdemCompraRead, status_code=status.HTTP_201_CREATED)
def create_item(payload: OrdemCompraCreate, db: Session = Depends(get_db), _user=Depends(require_permission("compras", "criar"))):
    return service.create(db, payload)


@router.put("/{item_id}", response_model=OrdemCompraRead)
def update_item(item_id: int, payload: OrdemCompraUpdate, db: Session = Depends(get_db), _user=Depends(require_permission("compras", "editar"))):
    item = service.update(db, item_id, payload)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db), _user=Depends(require_permission("compras", "excluir"))):
    if not service.delete(db, item_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return None
