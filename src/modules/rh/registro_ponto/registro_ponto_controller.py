from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.database.connection import get_db
from src.core.security.permissions import require_permission
from .registro_ponto_schema import RegistroPontoCreate, RegistroPontoRead, RegistroPontoUpdate
from .registro_ponto_service import RegistroPontoService

router = APIRouter(prefix="/registro-ponto", tags=["RH - Ponto"])
service = RegistroPontoService()


@router.get("/", response_model=list[RegistroPontoRead])
def list_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), _user=Depends(require_permission("rh", "visualizar"))):
    return service.list(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=RegistroPontoRead)
def get_item(item_id: int, db: Session = Depends(get_db), _user=Depends(require_permission("rh", "visualizar"))):
    item = service.get(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return item


@router.post("/", response_model=RegistroPontoRead, status_code=status.HTTP_201_CREATED)
def create_item(payload: RegistroPontoCreate, db: Session = Depends(get_db), _user=Depends(require_permission("rh", "criar"))):
    return service.create(db, payload)


@router.put("/{item_id}", response_model=RegistroPontoRead)
def update_item(item_id: int, payload: RegistroPontoUpdate, db: Session = Depends(get_db), _user=Depends(require_permission("rh", "editar"))):
    item = service.update(db, item_id, payload)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db), _user=Depends(require_permission("rh", "excluir"))):
    if not service.delete(db, item_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return None
