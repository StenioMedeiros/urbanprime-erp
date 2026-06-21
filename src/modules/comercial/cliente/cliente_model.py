from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class Cliente(TimestampMixin, Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(160), nullable=False)
    tipo_pessoa = Column(String(20), nullable=False, default='juridica')
    cpf_cnpj = Column(String(20), nullable=True)
    email = Column(String(180), nullable=True)
    telefone = Column(String(30), nullable=True)
    endereco = Column(Text, nullable=True)
    cidade = Column(String(100), nullable=True)
    estado = Column(String(2), nullable=True)
    cep = Column(String(12), nullable=True)
    status = Column(String(30), nullable=False, default='ativo')
