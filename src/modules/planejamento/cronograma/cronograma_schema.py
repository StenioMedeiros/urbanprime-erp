from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class CronogramaBase(BaseModel):
    obra_id: int
    atividade: str
    data_inicio: date | None = None
    data_fim: date | None = None
    percentual_concluido: Decimal = 0
    status: str = 'planejado'


class CronogramaCreate(CronogramaBase):
    pass


class CronogramaUpdate(BaseModel):
    obra_id: int | None = None
    atividade: str | None = None
    data_inicio: date | None | None = None
    data_fim: date | None | None = None
    percentual_concluido: Decimal | None = None
    status: str | None = None


class CronogramaRead(CronogramaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
