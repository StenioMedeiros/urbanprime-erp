from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class RegistroPonto(TimestampMixin, Base):
    __tablename__ = "registro_ponto"

    id = Column(Integer, primary_key=True, index=True)
    funcionario_id = Column(ForeignKey('funcionarios.id'), nullable=False)
    data = Column(Date, nullable=False)
    entrada = Column(Time, nullable=True)
    saida_intervalo = Column(Time, nullable=True)
    retorno_intervalo = Column(Time, nullable=True)
    saida = Column(Time, nullable=True)
    observacao = Column(Text, nullable=True)
