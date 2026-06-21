from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sqlalchemy.orm import Session

from src.core.auth.perfil_model import Perfil
from src.core.auth.usuario_model import Usuario
from src.core.auth.usuario_perfil_model import UsuarioPerfil
from src.core.database.connection import SessionLocal
from src.core.security.password_manager import hash_password
from src.modules.rh.funcionario.funcionario_model import Funcionario


def main() -> None:
    db: Session = SessionLocal()
    try:
        funcionario = db.query(Funcionario).filter_by(email_corporativo="admin@urbanprime.com").first()
        if funcionario is None:
            funcionario = Funcionario(nome="Administrador UrbanPrime", email_corporativo="admin@urbanprime.com", cargo="Administrador do Sistema", setor="administrativo")
            db.add(funcionario)
            db.commit()
            db.refresh(funcionario)
        usuario = db.query(Usuario).filter_by(username="admin").first()
        if usuario is None:
            usuario = Usuario(funcionario_id=funcionario.id, username="admin", email="admin@urbanprime.com", senha_hash=hash_password("Admin@123"))
            db.add(usuario)
            db.commit()
            db.refresh(usuario)
        perfil = db.query(Perfil).filter_by(nome="administrador").first()
        if perfil and not db.query(UsuarioPerfil).filter_by(usuario_id=usuario.id, perfil_id=perfil.id).first():
            db.add(UsuarioPerfil(usuario_id=usuario.id, perfil_id=perfil.id))
            db.commit()
        print("Administrador pronto: admin / Admin@123")
    finally:
        db.close()


if __name__ == "__main__":
    main()
