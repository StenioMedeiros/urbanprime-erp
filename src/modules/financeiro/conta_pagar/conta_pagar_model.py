from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class ContaPagar(TimestampMixin, Base):
    __tablename__ = "contas_pagar"

    id = Column(Integer, primary_key=True, index=True)
    fornecedor_id = Column(ForeignKey('fornecedores.id'), nullable=True)
    ordem_compra_id = Column(ForeignKey('ordens_compra.id'), nullable=True)
    obra_id = Column(ForeignKey('obras.id'), nullable=True)
    descricao = Column(String(180), nullable=False)
    valor = Column(Numeric(14, 2), nullable=False)
    data_vencimento = Column(Date, nullable=False)
    data_pagamento = Column(Date, nullable=True)
    status = Column(String(30), nullable=False, default='em_aberto')
