from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class ChamadoTecnico(TimestampMixin, Base):
    __tablename__ = "chamados_tecnicos"

    id = Column(Integer, primary_key=True, index=True)
    obra_id = Column(ForeignKey('obras.id'), nullable=False)
    solicitante_id = Column(ForeignKey('funcionarios.id'), nullable=True)
    titulo = Column(String(160), nullable=False)
    descricao = Column(Text, nullable=True)
    prioridade = Column(String(30), nullable=False, default='media')
    status = Column(String(30), nullable=False, default='aberto')
