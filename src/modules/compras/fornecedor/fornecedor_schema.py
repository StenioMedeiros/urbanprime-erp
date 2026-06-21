from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import EmailStr
from pydantic import BaseModel, ConfigDict


class FornecedorBase(BaseModel):
    razao_social: str
    nome_fantasia: str | None = None
    cnpj: str | None = None
    email: EmailStr | None = None
    telefone: str | None = None
    endereco: str | None = None
    status: str = 'ativo'


class FornecedorCreate(FornecedorBase):
    pass


class FornecedorUpdate(BaseModel):
    razao_social: str | None = None
    nome_fantasia: str | None | None = None
    cnpj: str | None | None = None
    email: EmailStr | None | None = None
    telefone: str | None | None = None
    endereco: str | None | None = None
    status: str | None = None


class FornecedorRead(FornecedorBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
