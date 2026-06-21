from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class AgendaVisitaBase(BaseModel):
    cliente_id: int
    funcionario_id: int | None = None
    data_visita: date
    horario: time | None = None
    local_visita: str | None = None
    observacoes: str | None = None
    status: str = 'agendada'


class AgendaVisitaCreate(AgendaVisitaBase):
    pass


class AgendaVisitaUpdate(BaseModel):
    cliente_id: int | None = None
    funcionario_id: int | None | None = None
    data_visita: date | None = None
    horario: time | None | None = None
    local_visita: str | None | None = None
    observacoes: str | None | None = None
    status: str | None = None


class AgendaVisitaRead(AgendaVisitaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
