from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class Frota(TimestampMixin, Base):
    __tablename__ = "frotas"

    id = Column(Integer, primary_key=True, index=True)
    identificacao = Column(String(120), nullable=False)
    tipo = Column(String(80), nullable=True)
    placa = Column(String(12), nullable=True)
    status = Column(String(30), nullable=False, default='disponivel')
    obra_id = Column(ForeignKey('obras.id'), nullable=True)
