from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class UsuarioRead(BaseModel):
    id: int
    funcionario_id: int
    username: str
    email: EmailStr
    ativo: bool
    bloqueado: bool
