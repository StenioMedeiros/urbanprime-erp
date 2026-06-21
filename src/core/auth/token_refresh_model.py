from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, func

from src.core.database.base import Base


class TokenRefresh(Base):
    __tablename__ = "tokens_refresh"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    token_hash = Column(String(255), nullable=False)
    data_criacao = Column(DateTime, server_default=func.now(), nullable=False)
    data_expiracao = Column(DateTime, nullable=False)
    revogado = Column(Boolean, default=False, nullable=False)
    ip_origem = Column(String(80), nullable=True)
    user_agent = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
