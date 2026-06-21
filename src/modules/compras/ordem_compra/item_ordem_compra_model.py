from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class ItemOrdemCompra(TimestampMixin, Base):
    __tablename__ = "itens_ordem_compra"

    id = Column(Integer, primary_key=True, index=True)
    ordem_compra_id = Column(ForeignKey('ordens_compra.id'), nullable=False)
    insumo_id = Column(ForeignKey('insumos.id'), nullable=True)
    descricao = Column(String(180), nullable=False)
    quantidade = Column(Numeric(14, 3), nullable=False)
    valor_unitario = Column(Numeric(14, 2), nullable=False)
    valor_total = Column(Numeric(14, 2), nullable=False)
