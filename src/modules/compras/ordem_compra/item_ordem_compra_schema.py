from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class ItemOrdemCompraBase(BaseModel):
    ordem_compra_id: int
    insumo_id: int | None = None
    descricao: str
    quantidade: Decimal = Decimal('0')
    valor_unitario: Decimal = Decimal('0')
    valor_total: Decimal = Decimal('0')


class ItemOrdemCompraCreate(ItemOrdemCompraBase):
    pass


class ItemOrdemCompraUpdate(BaseModel):
    ordem_compra_id: int | None = None
    insumo_id: int | None | None = None
    descricao: str | None = None
    quantidade: Decimal | None = None
    valor_unitario: Decimal | None = None
    valor_total: Decimal | None = None


class ItemOrdemCompraRead(ItemOrdemCompraBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
