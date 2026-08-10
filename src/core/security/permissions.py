from collections.abc import Callable

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.auth.auth_service import get_current_user
from src.core.auth.perfil_model import Perfil
from src.core.auth.perfil_permissao_model import PerfilPermissao
from src.core.auth.permissao_model import Permissao
from src.core.auth.usuario_model import Usuario
from src.core.auth.usuario_perfil_model import UsuarioPerfil
from src.core.database.connection import get_db


def user_has_permission(db: Session, usuario_id: int, modulo: str, acao: str) -> bool:
    query = (
        db.query(Permissao)
        .join(PerfilPermissao, PerfilPermissao.permissao_id == Permissao.id)
        .join(Perfil, Perfil.id == PerfilPermissao.perfil_id)
        .join(UsuarioPerfil, UsuarioPerfil.perfil_id == Perfil.id)
        .filter(UsuarioPerfil.usuario_id == usuario_id, Permissao.modulo == modulo, Permissao.acao == acao, Perfil.ativo.is_(True))
    )
    return db.query(query.exists()).scalar()


def require_permission(modulo: str, acao: str) -> Callable:
    def checker(user: Usuario = Depends(get_current_user), db: Session = Depends(get_db)) -> Usuario:
        if user_has_permission(db, user.id, modulo, acao):
            return user
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permissão insuficiente")

    return checker
