from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class FolhaPagamentoBase(BaseModel):
    funcionario_id: int
    competencia: str
    salario_bruto: Decimal = Decimal('0')
    descontos: Decimal = 0
    salario_liquido: Decimal = Decimal('0')
    status: str = 'aberta'


class FolhaPagamentoCreate(FolhaPagamentoBase):
    pass


class FolhaPagamentoUpdate(BaseModel):
    funcionario_id: int | None = None
    competencia: str | None = None
    salario_bruto: Decimal | None = None
    descontos: Decimal | None = None
    salario_liquido: Decimal | None = None
    status: str | None = None


class FolhaPagamentoRead(FolhaPagamentoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
