from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class ChamadoTecnicoBase(BaseModel):
    obra_id: int
    solicitante_id: int | None = None
    titulo: str
    descricao: str | None = None
    prioridade: str = 'media'
    status: str = 'aberto'


class ChamadoTecnicoCreate(ChamadoTecnicoBase):
    pass


class ChamadoTecnicoUpdate(BaseModel):
    obra_id: int | None = None
    solicitante_id: int | None | None = None
    titulo: str | None = None
    descricao: str | None | None = None
    prioridade: str | None = None
    status: str | None = None


class ChamadoTecnicoRead(ChamadoTecnicoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
