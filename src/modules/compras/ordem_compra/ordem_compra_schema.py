from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class OrdemCompraBase(BaseModel):
    fornecedor_id: int
    obra_id: int | None = None
    cotacao_id: int | None = None
    numero: str
    data_emissao: date | None = None
    data_aprovacao: date | None = None
    data_recebimento: date | None = None
    valor_total: Decimal = Decimal("0")
    status: str = "aberta"


class OrdemCompraCreate(OrdemCompraBase):
    pass


class OrdemCompraUpdate(BaseModel):
    fornecedor_id: int | None = None
    obra_id: int | None = None
    cotacao_id: int | None = None
    numero: str | None = None
    data_emissao: date | None = None
    data_aprovacao: date | None = None
    data_recebimento: date | None = None
    valor_total: Decimal | None = None
    status: str | None = None


class OrdemCompraRead(OrdemCompraBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
