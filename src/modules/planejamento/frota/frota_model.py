from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, String

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class Frota(TimestampMixin, Base):
    __tablename__ = "frotas"

    id = Column(Integer, primary_key=True, index=True)
    identificacao = Column(String(120), nullable=False)
    tipo = Column(String(80), nullable=True)
    placa = Column(String(12), nullable=True)
    marca = Column(String(80), nullable=True)
    modelo = Column(String(100), nullable=True)
    ano_fabricacao = Column(Integer, nullable=True)
    data_aquisicao = Column(Date, nullable=True)
    valor_aquisicao = Column(Numeric(16, 2), nullable=True)
    horimetro_atual = Column(Numeric(14, 2), nullable=True)
    status = Column(String(30), nullable=False, default="disponivel")
    obra_id = Column(ForeignKey("obras.id"), nullable=True)
