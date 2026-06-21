from src.shared.utils.crud_repository import CRUDRepository
from .movimentacao_estoque_model import MovimentacaoEstoque


class MovimentacaoEstoqueRepository(CRUDRepository[MovimentacaoEstoque]):
    def __init__(self):
        super().__init__(MovimentacaoEstoque)
