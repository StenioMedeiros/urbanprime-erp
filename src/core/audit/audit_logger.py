from datetime import date, datetime, time
from decimal import Decimal
from typing import Any

from sqlalchemy.orm import Session

from src.core.audit.log_auditoria_model import LogAuditoria


SENSITIVE_FIELDS = {
    "senha",
    "password",
    "senha_hash",
    "token_hash",
    "token_sessao_hash",
    "access_token",
    "refresh_token",
    "secret_key",
    "fernet_key",
}


def set_audit_context(
    db: Session,
    *,
    usuario_id: int | None,
    modulo: str,
    origem: str,
) -> None:
    db.info["audit_context"] = {
        "usuario_id": usuario_id,
        "modulo": modulo,
        "origem": origem,
    }


def get_audit_context(db: Session) -> dict[str, Any] | None:
    return db.info.get("audit_context")


def _json_value(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, (date, datetime, time)):
        return value.isoformat()
    if isinstance(value, dict):
        return {str(key): _json_value(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_json_value(item) for item in value]
    return str(value)


def model_snapshot(item: Any) -> dict[str, Any]:
    return {
        column.name: _json_value(getattr(item, column.name))
        for column in item.__table__.columns
        if column.name.casefold() not in SENSITIVE_FIELDS
    }


def add_audit_log(
    db: Session,
    *,
    usuario_id: int | None,
    modulo: str,
    acao: str,
    entidade: str | None = None,
    entidade_id: int | None = None,
    descricao: str | None = None,
    nivel: str = "info",
    dados_anteriores: dict | None = None,
    dados_novos: dict | None = None,
    ip_origem: str | None = None,
    user_agent: str | None = None,
) -> LogAuditoria:
    log = LogAuditoria(
        usuario_id=usuario_id,
        modulo=modulo,
        acao=acao,
        entidade=entidade,
        entidade_id=entidade_id,
        nivel=nivel,
        descricao=descricao,
        ip_origem=ip_origem,
        user_agent=user_agent,
        dados_anteriores=_json_value(dados_anteriores),
        dados_novos=_json_value(dados_novos),
    )
    db.add(log)
    return log


def log_action(
    db: Session,
    *,
    usuario_id: int | None,
    modulo: str,
    acao: str,
    entidade: str | None = None,
    entidade_id: int | None = None,
    descricao: str | None = None,
    nivel: str = "info",
    dados_anteriores: dict | None = None,
    dados_novos: dict | None = None,
    ip_origem: str | None = None,
    user_agent: str | None = None,
) -> LogAuditoria:
    log = add_audit_log(
        db,
        usuario_id=usuario_id,
        modulo=modulo,
        acao=acao,
        entidade=entidade,
        entidade_id=entidade_id,
        nivel=nivel,
        descricao=descricao,
        dados_anteriores=dados_anteriores,
        dados_novos=dados_novos,
        ip_origem=ip_origem,
        user_agent=user_agent,
    )
    db.commit()
    db.refresh(log)
    return log
