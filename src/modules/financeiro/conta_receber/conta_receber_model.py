from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class ContaReceber(TimestampMixin, Base):
    __tablename__ = "contas_receber"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(ForeignKey('clientes.id'), nullable=True)
    contrato_id = Column(ForeignKey('contratos.id'), nullable=True)
    medicao_id = Column(ForeignKey('medicoes.id'), nullable=True)
    descricao = Column(String(180), nullable=False)
    valor = Column(Numeric(14, 2), nullable=False)
    data_vencimento = Column(Date, nullable=False)
    data_recebimento = Column(Date, nullable=True)
    status = Column(String(30), nullable=False, default='em_aberto')
