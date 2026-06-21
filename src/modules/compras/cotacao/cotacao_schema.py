from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class CotacaoBase(BaseModel):
    fornecedor_id: int
    obra_id: int | None = None
    descricao: str | None = None
    valor_total: Decimal | None = None
    data_cotacao: date | None = None
    status: str = 'aberta'


class CotacaoCreate(CotacaoBase):
    pass


class CotacaoUpdate(BaseModel):
    fornecedor_id: int | None = None
    obra_id: int | None | None = None
    descricao: str | None | None = None
    valor_total: Decimal | None | None = None
    data_cotacao: date | None | None = None
    status: str | None = None


class CotacaoRead(CotacaoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
