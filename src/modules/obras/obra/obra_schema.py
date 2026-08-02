from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ObraBase(BaseModel):
    contrato_id: int
    projeto_id: int
    nome: str
    descricao: str | None = None
    endereco: str | None = None
    cidade: str | None = None
    estado: str | None = None
    cep: str | None = None
    responsavel_id: int | None = None
    data_inicio: date | None = None
    data_previsao_fim: date | None = None
    data_fim: date | None = None
    percentual_fisico: Decimal = Decimal("0")
    status: str = "planejada"


class ObraCreate(ObraBase):
    pass


class ObraUpdate(BaseModel):
    contrato_id: int | None = None
    projeto_id: int | None = None
    nome: str | None = None
    descricao: str | None = None
    endereco: str | None = None
    cidade: str | None = None
    estado: str | None = None
    cep: str | None = None
    responsavel_id: int | None = None
    data_inicio: date | None = None
    data_previsao_fim: date | None = None
    data_fim: date | None = None
    percentual_fisico: Decimal | None = None
    status: str | None = None


class ObraRead(ObraBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
