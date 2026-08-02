from sqlalchemy import Column, Date, ForeignKey, Index, Integer, Numeric, String

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class ContaReceber(TimestampMixin, Base):
    __tablename__ = "contas_receber"
    __table_args__ = (Index("ix_conta_receber_competencia", "data_competencia"),)

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(ForeignKey("clientes.id"), nullable=True)
    contrato_id = Column(ForeignKey("contratos.id"), nullable=True)
    medicao_id = Column(ForeignKey("medicoes.id"), nullable=True)
    fatura_id = Column(ForeignKey("faturas.id", ondelete="SET NULL"), nullable=True)
    categoria_financeira_id = Column(ForeignKey("categorias_financeiras.id", ondelete="SET NULL"), nullable=True)
    centro_custo_id = Column(ForeignKey("centros_custo.id", ondelete="SET NULL"), nullable=True)
    numero_documento = Column(String(60), nullable=True)
    descricao = Column(String(180), nullable=False)
    valor = Column(Numeric(14, 2), nullable=False)
    data_competencia = Column(Date, nullable=True)
    data_vencimento = Column(Date, nullable=False)
    data_recebimento = Column(Date, nullable=True)
    status = Column(String(30), nullable=False, default="em_aberto")
