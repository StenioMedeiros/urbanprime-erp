from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class OrcamentoBaseBase(BaseModel):
    obra_id: int
    versao: int = 1
    descricao: str | None = None
    valor_total: Decimal = Decimal('0')
    data_aprovacao: date | None = None
    aprovado_por_id: int | None = None
    status: str = 'vigente'


class OrcamentoBaseCreate(OrcamentoBaseBase):
    pass


class OrcamentoBaseUpdate(BaseModel):
    obra_id: int | None = None
    versao: int | None = None
    descricao: str | None | None = None
    valor_total: Decimal | None = None
    data_aprovacao: date | None | None = None
    aprovado_por_id: int | None | None = None
    status: str | None = None


class OrcamentoBaseRead(OrcamentoBaseBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
