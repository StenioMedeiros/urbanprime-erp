from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class OrdemCompra(TimestampMixin, Base):
    __tablename__ = "ordens_compra"

    id = Column(Integer, primary_key=True, index=True)
    fornecedor_id = Column(ForeignKey('fornecedores.id'), nullable=False)
    obra_id = Column(ForeignKey('obras.id'), nullable=True)
    numero = Column(String(60), nullable=False)
    data_emissao = Column(Date, nullable=True)
    valor_total = Column(Numeric(14, 2), nullable=False)
    status = Column(String(30), nullable=False, default='aberta')
