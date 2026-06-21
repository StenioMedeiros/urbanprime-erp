from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class RevisaoProjetoBase(BaseModel):
    projeto_id: int
    responsavel_id: int | None = None
    numero_revisao: int
    descricao: str | None = None
    motivo: str | None = None
    arquivo_revisao: str | None = None
    data_revisao: date | None = None
    aprovado: bool = False


class RevisaoProjetoCreate(RevisaoProjetoBase):
    pass


class RevisaoProjetoUpdate(BaseModel):
    projeto_id: int | None = None
    responsavel_id: int | None | None = None
    numero_revisao: int | None = None
    descricao: str | None | None = None
    motivo: str | None | None = None
    arquivo_revisao: str | None | None = None
    data_revisao: date | None | None = None
    aprovado: bool | None = None


class RevisaoProjetoRead(RevisaoProjetoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
