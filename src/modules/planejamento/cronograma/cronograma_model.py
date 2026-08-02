from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, String

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class Cronograma(TimestampMixin, Base):
    __tablename__ = "cronogramas"

    id = Column(Integer, primary_key=True, index=True)
    obra_id = Column(ForeignKey("obras.id"), nullable=False)
    atividade = Column(String(180), nullable=False)
    data_inicio = Column(Date, nullable=True)
    data_fim = Column(Date, nullable=True)
    peso_percentual = Column(Numeric(5, 2), nullable=False, default=0)
    percentual_concluido = Column(Numeric(5, 2), nullable=False, default=0)
    status = Column(String(30), nullable=False, default="planejado")
