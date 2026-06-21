from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.database.connection import get_db
from src.core.security.permissions import require_permission
from .conta_pagar_schema import ContaPagarCreate, ContaPagarRead, ContaPagarUpdate
from .conta_pagar_service import ContaPagarService

router = APIRouter(prefix="/contas-pagar", tags=["Financeiro - Contas a Pagar"])
service = ContaPagarService()


@router.get("/", response_model=list[ContaPagarRead])
def list_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), _user=Depends(require_permission("financeiro", "visualizar"))):
    return service.list(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=ContaPagarRead)
def get_item(item_id: int, db: Session = Depends(get_db), _user=Depends(require_permission("financeiro", "visualizar"))):
    item = service.get(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return item


@router.post("/", response_model=ContaPagarRead, status_code=status.HTTP_201_CREATED)
def create_item(payload: ContaPagarCreate, db: Session = Depends(get_db), _user=Depends(require_permission("financeiro", "criar"))):
    return service.create(db, payload)


@router.put("/{item_id}", response_model=ContaPagarRead)
def update_item(item_id: int, payload: ContaPagarUpdate, db: Session = Depends(get_db), _user=Depends(require_permission("financeiro", "editar"))):
    item = service.update(db, item_id, payload)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db), _user=Depends(require_permission("financeiro", "excluir"))):
    if not service.delete(db, item_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return None
