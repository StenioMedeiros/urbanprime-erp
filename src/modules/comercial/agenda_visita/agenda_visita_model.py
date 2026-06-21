from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class AgendaVisita(TimestampMixin, Base):
    __tablename__ = "agenda_visitas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(ForeignKey('clientes.id'), nullable=False)
    funcionario_id = Column(ForeignKey('funcionarios.id'), nullable=True)
    data_visita = Column(Date, nullable=False)
    horario = Column(Time, nullable=True)
    local_visita = Column(String(180), nullable=True)
    observacoes = Column(Text, nullable=True)
    status = Column(String(30), nullable=False, default='agendada')
