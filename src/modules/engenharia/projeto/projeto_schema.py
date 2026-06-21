from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class ProjetoBase(BaseModel):
    contrato_id: int
    responsavel_id: int | None = None
    nome: str
    descricao: str | None = None
    tipo_projeto: str | None = None
    data_inicio: date | None = None
    data_previsao_entrega: date | None = None
    data_entrega: date | None = None
    status: str = 'em_elaboracao'
    arquivo_projeto: str | None = None


class ProjetoCreate(ProjetoBase):
    pass


class ProjetoUpdate(BaseModel):
    contrato_id: int | None = None
    responsavel_id: int | None | None = None
    nome: str | None = None
    descricao: str | None | None = None
    tipo_projeto: str | None | None = None
    data_inicio: date | None | None = None
    data_previsao_entrega: date | None | None = None
    data_entrega: date | None | None = None
    status: str | None = None
    arquivo_projeto: str | None | None = None


class ProjetoRead(ProjetoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
