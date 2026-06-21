from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class DiarioObra(TimestampMixin, Base):
    __tablename__ = "diarios_obra"

    id = Column(Integer, primary_key=True, index=True)
    obra_id = Column(ForeignKey('obras.id'), nullable=False)
    funcionario_id = Column(ForeignKey('funcionarios.id'), nullable=True)
    data_registro = Column(Date, nullable=False)
    clima = Column(String(80), nullable=True)
    atividades = Column(Text, nullable=True)
    ocorrencias = Column(Text, nullable=True)
