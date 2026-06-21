from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class Projeto(TimestampMixin, Base):
    __tablename__ = "projetos"

    id = Column(Integer, primary_key=True, index=True)
    contrato_id = Column(ForeignKey('contratos.id'), nullable=False)
    responsavel_id = Column(ForeignKey('funcionarios.id'), nullable=True)
    nome = Column(String(160), nullable=False)
    descricao = Column(Text, nullable=True)
    tipo_projeto = Column(String(80), nullable=True)
    data_inicio = Column(Date, nullable=True)
    data_previsao_entrega = Column(Date, nullable=True)
    data_entrega = Column(Date, nullable=True)
    status = Column(String(30), nullable=False, default='em_elaboracao')
    arquivo_projeto = Column(String(255), nullable=True)
