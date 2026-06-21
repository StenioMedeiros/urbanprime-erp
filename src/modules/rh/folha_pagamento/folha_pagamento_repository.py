from src.shared.utils.crud_repository import CRUDRepository
from .folha_pagamento_model import FolhaPagamento


class FolhaPagamentoRepository(CRUDRepository[FolhaPagamento]):
    def __init__(self):
        super().__init__(FolhaPagamento)
