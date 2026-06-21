from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class FrotaBase(BaseModel):
    identificacao: str
    tipo: str | None = None
    placa: str | None = None
    status: str = 'disponivel'
    obra_id: int | None = None


class FrotaCreate(FrotaBase):
    pass


class FrotaUpdate(BaseModel):
    identificacao: str | None = None
    tipo: str | None | None = None
    placa: str | None | None = None
    status: str | None = None
    obra_id: int | None | None = None


class FrotaRead(FrotaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
