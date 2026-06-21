from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class OrcamentoBase(TimestampMixin, Base):
    __tablename__ = "orcamentos_base"

    id = Column(Integer, primary_key=True, index=True)
    obra_id = Column(ForeignKey('obras.id'), nullable=False)
    versao = Column(Integer, nullable=False, default=1)
    descricao = Column(Text, nullable=True)
    valor_total = Column(Numeric(14, 2), nullable=False)
    data_aprovacao = Column(Date, nullable=True)
    aprovado_por_id = Column(ForeignKey('funcionarios.id'), nullable=True)
    status = Column(String(30), nullable=False, default='vigente')
