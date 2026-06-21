from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class DiarioObraBase(BaseModel):
    obra_id: int
    funcionario_id: int | None = None
    data_registro: date
    clima: str | None = None
    atividades: str | None = None
    ocorrencias: str | None = None


class DiarioObraCreate(DiarioObraBase):
    pass


class DiarioObraUpdate(BaseModel):
    obra_id: int | None = None
    funcionario_id: int | None | None = None
    data_registro: date | None = None
    clima: str | None | None = None
    atividades: str | None | None = None
    ocorrencias: str | None | None = None


class DiarioObraRead(DiarioObraBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
