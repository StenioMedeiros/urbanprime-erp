from sqlalchemy.orm import Session

from src.core.auth.usuario_model import Usuario


class AuthRepository:
    def get_by_username(self, db: Session, username: str) -> Usuario | None:
        return db.query(Usuario).filter(Usuario.username == username).first()

    def save(self, db: Session, usuario: Usuario) -> Usuario:
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
