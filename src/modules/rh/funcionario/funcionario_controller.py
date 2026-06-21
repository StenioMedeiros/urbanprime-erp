from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.database.connection import get_db
from src.core.security.permissions import require_permission
from .funcionario_schema import FuncionarioCreate, FuncionarioRead, FuncionarioUpdate
from .funcionario_service import FuncionarioService

router = APIRouter(prefix="/funcionarios", tags=["RH - Funcionarios"])
service = FuncionarioService()


@router.get("/", response_model=list[FuncionarioRead])
def list_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), _user=Depends(require_permission("rh", "visualizar"))):
    return service.list(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=FuncionarioRead)
def get_item(item_id: int, db: Session = Depends(get_db), _user=Depends(require_permission("rh", "visualizar"))):
    item = service.get(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return item


@router.post("/", response_model=FuncionarioRead, status_code=status.HTTP_201_CREATED)
def create_item(payload: FuncionarioCreate, db: Session = Depends(get_db), _user=Depends(require_permission("rh", "criar"))):
    return service.create(db, payload)


@router.put("/{item_id}", response_model=FuncionarioRead)
def update_item(item_id: int, payload: FuncionarioUpdate, db: Session = Depends(get_db), _user=Depends(require_permission("rh", "editar"))):
    item = service.update(db, item_id, payload)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db), _user=Depends(require_permission("rh", "excluir"))):
    if not service.delete(db, item_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return None
