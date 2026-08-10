from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src.core.auth.auth_repository import AuthRepository
from src.core.auth.usuario_model import Usuario
from src.core.config.settings import get_settings
from src.core.database.connection import get_db
from src.core.security.jwt_manager import create_access_token, create_refresh_token, decode_token
from src.core.security.password_manager import verify_password
from src.shared.utils.brazil_localization import now_local_naive

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
MAX_LOGIN_ATTEMPTS = 5
settings = get_settings()


class AuthService:
    def __init__(self, repository: AuthRepository | None = None):
        self.repository = repository or AuthRepository()

    def authenticate(self, db: Session, username: str, password: str) -> tuple[Usuario, str, str]:
        usuario = self.repository.get_by_username(db, username)
        if usuario is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
        if usuario.bloqueado or not usuario.ativo:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Usuário bloqueado ou inativo")
        if not verify_password(password, usuario.senha_hash):
            usuario.tentativas_login += 1
            if usuario.tentativas_login >= MAX_LOGIN_ATTEMPTS:
                usuario.bloqueado = True
            self.repository.save(db, usuario)
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
        usuario.tentativas_login = 0
        usuario.ultimo_login = now_local_naive(settings.app_timezone)
        self.repository.save(db, usuario)
        access = create_access_token(str(usuario.id), {"username": usuario.username})
        refresh = create_refresh_token(str(usuario.id))
        return usuario, access, refresh


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> Usuario:
    try:
        payload = decode_token(token)
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido") from exc
    if payload.get("type") != "access":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
    usuario = db.get(Usuario, int(payload["sub"]))
    if usuario is None or not usuario.ativo or usuario.bloqueado:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário inválido")
    return usuario
