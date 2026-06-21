from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.database.connection import get_db
from src.core.security.permissions import require_permission
from .item_ordem_compra_schema import ItemOrdemCompraCreate, ItemOrdemCompraRead, ItemOrdemCompraUpdate
from .item_ordem_compra_service import ItemOrdemCompraService

router = APIRouter(prefix="/itens-ordem-compra", tags=["Compras - Itens OC"])
service = ItemOrdemCompraService()


@router.get("/", response_model=list[ItemOrdemCompraRead])
def list_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), _user=Depends(require_permission("compras", "visualizar"))):
    return service.list(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=ItemOrdemCompraRead)
def get_item(item_id: int, db: Session = Depends(get_db), _user=Depends(require_permission("compras", "visualizar"))):
    item = service.get(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return item


@router.post("/", response_model=ItemOrdemCompraRead, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemOrdemCompraCreate, db: Session = Depends(get_db), _user=Depends(require_permission("compras", "criar"))):
    return service.create(db, payload)


@router.put("/{item_id}", response_model=ItemOrdemCompraRead)
def update_item(item_id: int, payload: ItemOrdemCompraUpdate, db: Session = Depends(get_db), _user=Depends(require_permission("compras", "editar"))):
    item = service.update(db, item_id, payload)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db), _user=Depends(require_permission("compras", "excluir"))):
    if not service.delete(db, item_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return None
