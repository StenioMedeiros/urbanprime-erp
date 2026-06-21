from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class MovimentacaoEstoqueBase(BaseModel):
    insumo_id: int
    obra_id: int | None = None
    tipo: str
    quantidade: Decimal = Decimal('0')
    data_movimentacao: date | None = None
    observacao: str | None = None


class MovimentacaoEstoqueCreate(MovimentacaoEstoqueBase):
    pass


class MovimentacaoEstoqueUpdate(BaseModel):
    insumo_id: int | None = None
    obra_id: int | None | None = None
    tipo: str | None = None
    quantidade: Decimal | None = None
    data_movimentacao: date | None | None = None
    observacao: str | None | None = None


class MovimentacaoEstoqueRead(MovimentacaoEstoqueBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
