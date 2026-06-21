from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class InsumoBase(BaseModel):
    nome: str
    descricao: str | None = None
    unidade_medida: str = 'un'
    quantidade_atual: Decimal = 0
    estoque_minimo: Decimal = 0
    valor_unitario: Decimal | None = None
    status: str = 'ativo'


class InsumoCreate(InsumoBase):
    pass


class InsumoUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None | None = None
    unidade_medida: str | None = None
    quantidade_atual: Decimal | None = None
    estoque_minimo: Decimal | None = None
    valor_unitario: Decimal | None | None = None
    status: str | None = None


class InsumoRead(InsumoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
