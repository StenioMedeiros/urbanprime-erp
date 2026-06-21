from sqlalchemy import Column, DateTime, ForeignKey, Integer, JSON, String, Text, func

from src.core.database.base import Base


class LogAuditoria(Base):
    __tablename__ = "logs_auditoria"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    modulo = Column(String(80), nullable=False)
    acao = Column(String(80), nullable=False)
    entidade = Column(String(120), nullable=True)
    entidade_id = Column(Integer, nullable=True)
    nivel = Column(String(30), default="info", nullable=False)
    descricao = Column(Text, nullable=True)
    ip_origem = Column(String(80), nullable=True)
    user_agent = Column(Text, nullable=True)
    dados_anteriores = Column(JSON, nullable=True)
    dados_novos = Column(JSON, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
