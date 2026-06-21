from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class Medicao(TimestampMixin, Base):
    __tablename__ = "medicoes"

    id = Column(Integer, primary_key=True, index=True)
    obra_id = Column(ForeignKey('obras.id'), nullable=False)
    contrato_id = Column(ForeignKey('contratos.id'), nullable=True)
    competencia = Column(String(7), nullable=False)
    valor_medido = Column(Numeric(14, 2), nullable=False)
    data_medicao = Column(Date, nullable=True)
    status = Column(String(30), nullable=False, default='pendente')
