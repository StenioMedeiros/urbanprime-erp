from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class MedicaoBase(BaseModel):
    obra_id: int
    contrato_id: int | None = None
    competencia: str
    valor_medido: Decimal = Decimal('0')
    data_medicao: date | None = None
    status: str = 'pendente'


class MedicaoCreate(MedicaoBase):
    pass


class MedicaoUpdate(BaseModel):
    obra_id: int | None = None
    contrato_id: int | None | None = None
    competencia: str | None = None
    valor_medido: Decimal | None = None
    data_medicao: date | None | None = None
    status: str | None = None


class MedicaoRead(MedicaoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
