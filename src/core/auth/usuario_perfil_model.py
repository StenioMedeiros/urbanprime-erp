from sqlalchemy import Column, DateTime, ForeignKey, Integer, func

from src.core.database.base import Base


class UsuarioPerfil(Base):
    __tablename__ = "usuario_perfil"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    perfil_id = Column(Integer, ForeignKey("perfis.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
