from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, func

from src.core.database.base import Base


class SessaoUsuario(Base):
    __tablename__ = "sessoes_usuario"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    token_sessao_hash = Column(String(255), nullable=False)
    ip_origem = Column(String(80), nullable=True)
    user_agent = Column(Text, nullable=True)
    data_login = Column(DateTime, server_default=func.now(), nullable=False)
    data_expiracao = Column(DateTime, nullable=False)
    ativo = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
