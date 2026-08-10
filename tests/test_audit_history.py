from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import src.core.database.all_models  # noqa: F401
from src.core.audit.audit_logger import log_action, model_snapshot, set_audit_context
from src.core.audit.log_auditoria_model import LogAuditoria
from src.core.auth.usuario_model import Usuario
from src.core.database.base import Base
from src.modules.comercial.cliente.cliente_model import Cliente
from src.modules.rh.funcionario.funcionario_model import Funcionario
from src.shared.utils.crud_repository import CRUDRepository


def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()


def create_user(db):
    employee = Funcionario(nome="Administrador", email_corporativo="admin@urbanprime.com")
    db.add(employee)
    db.flush()
    user = Usuario(
        funcionario_id=employee.id,
        username="admin",
        email="admin@urbanprime.com",
        senha_hash="hash-secreto",
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def test_crud_operations_create_a_complete_audit_trail():
    db = session()
    try:
        user = create_user(db)
        set_audit_context(db, usuario_id=user.id, modulo="Clientes", origem="teste")
        repository = CRUDRepository(Cliente)

        client = repository.create(db, {"nome": "Cliente inicial", "tipo_pessoa": "juridica"})
        repository.update(db, client.id, {"nome": "Cliente atualizado"})
        repository.delete(db, client.id)

        logs = db.query(LogAuditoria).order_by(LogAuditoria.id).all()
        assert [log.acao for log in logs] == ["criar", "editar", "excluir"]
        assert all(log.usuario_id == user.id for log in logs)
        assert logs[0].dados_novos["nome"] == "Cliente inicial"
        assert logs[1].dados_anteriores["nome"] == "Cliente inicial"
        assert logs[1].dados_novos["nome"] == "Cliente atualizado"
        assert logs[2].dados_anteriores["nome"] == "Cliente atualizado"
    finally:
        db.close()


def test_each_login_is_preserved_as_a_separate_record():
    db = session()
    try:
        user = create_user(db)
        for _ in range(2):
            log_action(
                db,
                usuario_id=user.id,
                modulo="auth",
                acao="login",
                entidade="usuarios",
                entidade_id=user.id,
                descricao="Login realizado no Streamlit",
            )

        logs = db.query(LogAuditoria).filter_by(usuario_id=user.id, acao="login").all()
        assert len(logs) == 2
        assert logs[0].id != logs[1].id
    finally:
        db.close()


def test_sensitive_values_are_not_copied_to_audit_data():
    db = session()
    try:
        user = create_user(db)
        snapshot = model_snapshot(user)
        assert "senha_hash" not in snapshot
        assert "hash-secreto" not in str(snapshot)
    finally:
        db.close()
