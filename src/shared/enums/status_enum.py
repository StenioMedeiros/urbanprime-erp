from enum import StrEnum


class StatusEnum(StrEnum):
    ATIVO = 'ativo'
    INATIVO = 'inativo'
    EM_ABERTO = 'em_aberto'
    PAGO = 'pago'
    RECEBIDO = 'recebido'
