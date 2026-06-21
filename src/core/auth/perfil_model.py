from sqlalchemy import Boolean, Column, Integer, String, Text

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class Perfil(TimestampMixin, Base):
    __tablename__ = "perfis"

    id = Column(Integer, primary_key=True)
    nome = Column(String(80), unique=True, nullable=False)
    descricao = Column(Text, nullable=True)
    nivel_acesso = Column(Integer, default=1, nullable=False)
    ativo = Column(Boolean, default=True, nullable=False)
