from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import src.core.database.all_models  # noqa: F401
from src.core.auth.auth_service import AuthService
from src.core.auth.usuario_model import Usuario
from src.core.database.base import Base
from src.core.security.password_manager import hash_password
from src.modules.rh.funcionario.funcionario_model import Funcionario


def test_login_funcionario():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    db = sessionmaker(bind=engine)()
    funcionario = Funcionario(nome="Admin", email_corporativo="admin@urbanprime.com")
    db.add(funcionario)
    db.commit()
    db.refresh(funcionario)
    db.add(Usuario(funcionario_id=funcionario.id, username="admin", email="admin@urbanprime.com", senha_hash=hash_password("Admin@123")))
    db.commit()
    _user, access, refresh = AuthService().authenticate(db, "admin", "Admin@123")
    assert access
    assert refresh


def test_bloqueio_por_tentativas_invalidas():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    db = sessionmaker(bind=engine)()
    funcionario = Funcionario(nome="Admin", email_corporativo="admin@urbanprime.com")
    db.add(funcionario)
    db.commit()
    db.refresh(funcionario)
    db.add(Usuario(funcionario_id=funcionario.id, username="admin", email="admin@urbanprime.com", senha_hash=hash_password("Admin@123")))
    db.commit()
    service = AuthService()
    for _ in range(5):
        try:
            service.authenticate(db, "admin", "errada")
        except HTTPException:
            pass
    user = db.query(Usuario).filter_by(username="admin").first()
    assert user.bloqueado is True
