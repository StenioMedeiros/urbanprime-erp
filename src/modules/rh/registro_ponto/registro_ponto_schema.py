from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class RegistroPontoBase(BaseModel):
    funcionario_id: int
    data: date
    entrada: time | None = None
    saida_intervalo: time | None = None
    retorno_intervalo: time | None = None
    saida: time | None = None
    observacao: str | None = None


class RegistroPontoCreate(RegistroPontoBase):
    pass


class RegistroPontoUpdate(BaseModel):
    funcionario_id: int | None = None
    data: date | None = None
    entrada: time | None | None = None
    saida_intervalo: time | None | None = None
    retorno_intervalo: time | None | None = None
    saida: time | None | None = None
    observacao: str | None | None = None


class RegistroPontoRead(RegistroPontoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
