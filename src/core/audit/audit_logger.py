from sqlalchemy.orm import Session

from src.core.audit.log_auditoria_model import LogAuditoria


def log_action(db: Session, *, usuario_id: int | None, modulo: str, acao: str, entidade: str | None = None, entidade_id: int | None = None, descricao: str | None = None, nivel: str = "info", dados_anteriores: dict | None = None, dados_novos: dict | None = None) -> LogAuditoria:
    log = LogAuditoria(
        usuario_id=usuario_id,
        modulo=modulo,
        acao=acao,
        entidade=entidade,
        entidade_id=entidade_id,
        nivel=nivel,
        descricao=descricao,
        dados_anteriores=dados_anteriores,
        dados_novos=dados_novos,
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log
