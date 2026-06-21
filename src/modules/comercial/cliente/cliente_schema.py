from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import EmailStr
from pydantic import BaseModel, ConfigDict


class ClienteBase(BaseModel):
    nome: str
    tipo_pessoa: str = 'juridica'
    cpf_cnpj: str | None = None
    email: EmailStr | None = None
    telefone: str | None = None
    endereco: str | None = None
    cidade: str | None = None
    estado: str | None = None
    cep: str | None = None
    status: str = 'ativo'


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(BaseModel):
    nome: str | None = None
    tipo_pessoa: str | None = None
    cpf_cnpj: str | None | None = None
    email: EmailStr | None | None = None
    telefone: str | None | None = None
    endereco: str | None | None = None
    cidade: str | None | None = None
    estado: str | None | None = None
    cep: str | None | None = None
    status: str | None = None


class ClienteRead(ClienteBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
