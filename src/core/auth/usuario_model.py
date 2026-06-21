from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

from src.core.database.base import Base
from src.shared.mixins.timestamp_mixin import TimestampMixin


class Usuario(TimestampMixin, Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"), nullable=False)
    username = Column(String(80), unique=True, nullable=False, index=True)
    email = Column(String(180), unique=True, nullable=False, index=True)
    senha_hash = Column(String(255), nullable=False)
    ativo = Column(Boolean, default=True, nullable=False)
    bloqueado = Column(Boolean, default=False, nullable=False)
    tentativas_login = Column(Integer, default=0, nullable=False)
    ultimo_login = Column(DateTime, nullable=True)
    data_criacao = Column(DateTime, nullable=True)
