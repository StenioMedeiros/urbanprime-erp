from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class CronogramaBase(BaseModel):
    obra_id: int
    atividade: str
    data_inicio: date | None = None
    data_fim: date | None = None
    peso_percentual: Decimal = Decimal("0")
    percentual_concluido: Decimal = Decimal("0")
    status: str = "planejado"


class CronogramaCreate(CronogramaBase):
    pass


class CronogramaUpdate(BaseModel):
    obra_id: int | None = None
    atividade: str | None = None
    data_inicio: date | None = None
    data_fim: date | None = None
    peso_percentual: Decimal | None = None
    percentual_concluido: Decimal | None = None
    status: str | None = None


class CronogramaRead(CronogramaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
