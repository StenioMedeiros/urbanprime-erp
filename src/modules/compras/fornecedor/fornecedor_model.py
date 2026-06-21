from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class Fornecedor(TimestampMixin, Base):
    __tablename__ = "fornecedores"

    id = Column(Integer, primary_key=True, index=True)
    razao_social = Column(String(180), nullable=False)
    nome_fantasia = Column(String(180), nullable=True)
    cnpj = Column(String(20), nullable=True)
    email = Column(String(180), nullable=True)
    telefone = Column(String(30), nullable=True)
    endereco = Column(Text, nullable=True)
    status = Column(String(30), nullable=False, default='ativo')
