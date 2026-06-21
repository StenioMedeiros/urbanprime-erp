from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, Time

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class FolhaPagamento(TimestampMixin, Base):
    __tablename__ = "folha_pagamento"

    id = Column(Integer, primary_key=True, index=True)
    funcionario_id = Column(ForeignKey('funcionarios.id'), nullable=False)
    competencia = Column(String(7), nullable=False)
    salario_bruto = Column(Numeric(14, 2), nullable=False)
    descontos = Column(Numeric(14, 2), nullable=False, default=0)
    salario_liquido = Column(Numeric(14, 2), nullable=False)
    status = Column(String(30), nullable=False, default='aberta')
