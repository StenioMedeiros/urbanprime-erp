from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ContaPagarBase(BaseModel):
    fornecedor_id: int | None = None
    ordem_compra_id: int | None = None
    obra_id: int | None = None
    categoria_financeira_id: int | None = None
    centro_custo_id: int | None = None
    numero_documento: str | None = None
    descricao: str
    valor: Decimal = Decimal("0")
    data_competencia: date | None = None
    data_vencimento: date
    data_pagamento: date | None = None
    status: str = "em_aberto"


class ContaPagarCreate(ContaPagarBase):
    pass


class ContaPagarUpdate(BaseModel):
    fornecedor_id: int | None = None
    ordem_compra_id: int | None = None
    obra_id: int | None = None
    categoria_financeira_id: int | None = None
    centro_custo_id: int | None = None
    numero_documento: str | None = None
    descricao: str | None = None
    valor: Decimal | None = None
    data_competencia: date | None = None
    data_vencimento: date | None = None
    data_pagamento: date | None = None
    status: str | None = None


class ContaPagarRead(ContaPagarBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
