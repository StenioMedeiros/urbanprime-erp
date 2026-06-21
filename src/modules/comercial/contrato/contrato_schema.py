from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class ContratoBase(BaseModel):
    cliente_id: int
    numero_contrato: str
    descricao: str | None = None
    valor_total: Decimal = Decimal('0')
    data_assinatura: date | None = None
    data_inicio: date | None = None
    data_fim: date | None = None
    status: str = 'ativo'
    arquivo_contrato: str | None = None


class ContratoCreate(ContratoBase):
    pass


class ContratoUpdate(BaseModel):
    cliente_id: int | None = None
    numero_contrato: str | None = None
    descricao: str | None | None = None
    valor_total: Decimal | None = None
    data_assinatura: date | None | None = None
    data_inicio: date | None | None = None
    data_fim: date | None | None = None
    status: str | None = None
    arquivo_contrato: str | None | None = None


class ContratoRead(ContratoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
