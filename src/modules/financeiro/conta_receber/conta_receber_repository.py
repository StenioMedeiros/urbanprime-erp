from src.shared.utils.crud_repository import CRUDRepository
from .conta_receber_model import ContaReceber


class ContaReceberRepository(CRUDRepository[ContaReceber]):
    def __init__(self):
        super().__init__(ContaReceber)
