from enum import StrEnum


class FinanceiroEnum(StrEnum):
    EM_ABERTO = 'em_aberto'
    PAGO = 'pago'
    VENCIDO = 'vencido'
    CANCELADO = 'cancelado'
