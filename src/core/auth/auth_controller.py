from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.auth.auth_schema import LoginRequest, TokenResponse
from src.core.auth.auth_service import AuthService
from src.core.audit.audit_logger import log_action
from src.core.database.connection import get_db

router = APIRouter(prefix="/auth", tags=["Autenticacao"])
service = AuthService()


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    usuario, access_token, refresh_token = service.authenticate(db, payload.username, payload.password)
    log_action(db, usuario_id=usuario.id, modulo="auth", acao="login", entidade="usuarios", entidade_id=usuario.id, descricao="Login realizado")
    return TokenResponse(access_token=access_token, refresh_token=refresh_token)
