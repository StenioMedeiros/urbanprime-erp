from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class Insumo(TimestampMixin, Base):
    __tablename__ = "insumos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(160), nullable=False)
    descricao = Column(Text, nullable=True)
    unidade_medida = Column(String(20), nullable=False, default='un')
    quantidade_atual = Column(Numeric(14, 3), nullable=False, default=0)
    estoque_minimo = Column(Numeric(14, 3), nullable=False, default=0)
    valor_unitario = Column(Numeric(14, 2), nullable=True)
    status = Column(String(30), nullable=False, default='ativo')
