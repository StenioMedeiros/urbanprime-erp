from sqlalchemy import Column, Integer, String, Text, UniqueConstraint

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class Permissao(TimestampMixin, Base):
    __tablename__ = "permissoes"
    __table_args__ = (UniqueConstraint("modulo", "acao", name="uq_permissao_modulo_acao"),)

    id = Column(Integer, primary_key=True)
    modulo = Column(String(80), nullable=False)
    acao = Column(String(80), nullable=False)
    descricao = Column(Text, nullable=True)
