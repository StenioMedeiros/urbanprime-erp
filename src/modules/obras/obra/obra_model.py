from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, String, Text

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class Obra(TimestampMixin, Base):
    __tablename__ = "obras"

    id = Column(Integer, primary_key=True, index=True)
    contrato_id = Column(ForeignKey("contratos.id"), nullable=False)
    projeto_id = Column(ForeignKey("projetos.id"), nullable=False)
    nome = Column(String(160), nullable=False)
    descricao = Column(Text, nullable=True)
    endereco = Column(Text, nullable=True)
    cidade = Column(String(100), nullable=True)
    estado = Column(String(2), nullable=True)
    cep = Column(String(12), nullable=True)
    responsavel_id = Column(ForeignKey("funcionarios.id"), nullable=True)
    data_inicio = Column(Date, nullable=True)
    data_previsao_fim = Column(Date, nullable=True)
    data_fim = Column(Date, nullable=True)
    percentual_fisico = Column(Numeric(5, 2), nullable=False, default=0)
    status = Column(String(30), nullable=False, default="planejada")
