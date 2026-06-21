from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class Funcionario(TimestampMixin, Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(160), nullable=False)
    cpf = Column(String(14), nullable=True)
    rg = Column(String(20), nullable=True)
    data_nascimento = Column(Date, nullable=True)
    email_corporativo = Column(String(180), nullable=False)
    telefone = Column(String(30), nullable=True)
    cargo = Column(String(120), nullable=True)
    setor = Column(String(80), nullable=True)
    data_admissao = Column(Date, nullable=True)
    data_demissao = Column(Date, nullable=True)
    salario_base = Column(Numeric(14, 2), nullable=True)
    status = Column(String(30), nullable=False, default='ativo')
