from datetime import datetime
from datetime import date, time
from decimal import Decimal
from pydantic import EmailStr
from pydantic import BaseModel, ConfigDict


class FuncionarioBase(BaseModel):
    nome: str
    cpf: str | None = None
    rg: str | None = None
    data_nascimento: date | None = None
    email_corporativo: EmailStr
    telefone: str | None = None
    cargo: str | None = None
    setor: str | None = None
    data_admissao: date | None = None
    data_demissao: date | None = None
    salario_base: Decimal | None = None
    status: str = 'ativo'


class FuncionarioCreate(FuncionarioBase):
    pass


class FuncionarioUpdate(BaseModel):
    nome: str | None = None
    cpf: str | None | None = None
    rg: str | None | None = None
    data_nascimento: date | None | None = None
    email_corporativo: EmailStr | None = None
    telefone: str | None | None = None
    cargo: str | None | None = None
    setor: str | None | None = None
    data_admissao: date | None | None = None
    data_demissao: date | None | None = None
    salario_base: Decimal | None | None = None
    status: str | None = None


class FuncionarioRead(FuncionarioBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
