from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.database.connection import get_db
from src.core.security.permissions import require_permission
from .chamado_tecnico_schema import ChamadoTecnicoCreate, ChamadoTecnicoRead, ChamadoTecnicoUpdate
from .chamado_tecnico_service import ChamadoTecnicoService

router = APIRouter(prefix="/chamados-tecnicos", tags=["Obras - Chamados"])
service = ChamadoTecnicoService()


@router.get("/", response_model=list[ChamadoTecnicoRead])
def list_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), _user=Depends(require_permission("obras", "visualizar"))):
    return service.list(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=ChamadoTecnicoRead)
def get_item(item_id: int, db: Session = Depends(get_db), _user=Depends(require_permission("obras", "visualizar"))):
    item = service.get(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return item


@router.post("/", response_model=ChamadoTecnicoRead, status_code=status.HTTP_201_CREATED)
def create_item(payload: ChamadoTecnicoCreate, db: Session = Depends(get_db), _user=Depends(require_permission("obras", "criar"))):
    return service.create(db, payload)


@router.put("/{item_id}", response_model=ChamadoTecnicoRead)
def update_item(item_id: int, payload: ChamadoTecnicoUpdate, db: Session = Depends(get_db), _user=Depends(require_permission("obras", "editar"))):
    item = service.update(db, item_id, payload)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db), _user=Depends(require_permission("obras", "excluir"))):
    if not service.delete(db, item_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return None
