from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class Contrato(TimestampMixin, Base):
    __tablename__ = "contratos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(ForeignKey('clientes.id'), nullable=False)
    numero_contrato = Column(String(60), nullable=False)
    descricao = Column(Text, nullable=True)
    valor_total = Column(Numeric(14, 2), nullable=False)
    data_assinatura = Column(Date, nullable=True)
    data_inicio = Column(Date, nullable=True)
    data_fim = Column(Date, nullable=True)
    status = Column(String(30), nullable=False, default='ativo')
    arquivo_contrato = Column(String(255), nullable=True)
