from src.shared.utils.crud_repository import CRUDRepository
from .cotacao_model import Cotacao


class CotacaoRepository(CRUDRepository[Cotacao]):
    def __init__(self):
        super().__init__(Cotacao)
