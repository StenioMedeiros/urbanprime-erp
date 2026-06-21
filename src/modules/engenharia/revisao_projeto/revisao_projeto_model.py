from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class RevisaoProjeto(TimestampMixin, Base):
    __tablename__ = "revisoes_projeto"

    id = Column(Integer, primary_key=True, index=True)
    projeto_id = Column(ForeignKey('projetos.id'), nullable=False)
    responsavel_id = Column(ForeignKey('funcionarios.id'), nullable=True)
    numero_revisao = Column(Integer, nullable=False)
    descricao = Column(Text, nullable=True)
    motivo = Column(Text, nullable=True)
    arquivo_revisao = Column(String(255), nullable=True)
    data_revisao = Column(Date, nullable=True)
    aprovado = Column(Boolean, nullable=False, default=False)
