from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class Cotacao(TimestampMixin, Base):
    __tablename__ = "cotacoes"

    id = Column(Integer, primary_key=True, index=True)
    fornecedor_id = Column(ForeignKey('fornecedores.id'), nullable=False)
    obra_id = Column(ForeignKey('obras.id'), nullable=True)
    descricao = Column(Text, nullable=True)
    valor_total = Column(Numeric(14, 2), nullable=True)
    data_cotacao = Column(Date, nullable=True)
    status = Column(String(30), nullable=False, default='aberta')
