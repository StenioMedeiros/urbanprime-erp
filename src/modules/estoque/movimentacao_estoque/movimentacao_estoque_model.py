from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class MovimentacaoEstoque(TimestampMixin, Base):
    __tablename__ = "movimentacoes_estoque"

    id = Column(Integer, primary_key=True, index=True)
    insumo_id = Column(ForeignKey('insumos.id'), nullable=False)
    obra_id = Column(ForeignKey('obras.id'), nullable=True)
    tipo = Column(String(20), nullable=False)
    quantidade = Column(Numeric(14, 3), nullable=False)
    data_movimentacao = Column(Date, nullable=True)
    observacao = Column(Text, nullable=True)
