from sqlalchemy import Column, DateTime, ForeignKey, Integer, func

from src.core.database.base import Base


class PerfilPermissao(Base):
    __tablename__ = "perfil_permissao"

    id = Column(Integer, primary_key=True)
    perfil_id = Column(Integer, ForeignKey("perfis.id"), nullable=False)
    permissao_id = Column(Integer, ForeignKey("permissoes.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
