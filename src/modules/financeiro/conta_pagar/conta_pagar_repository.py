from src.shared.utils.crud_repository import CRUDRepository
from .conta_pagar_model import ContaPagar


class ContaPagarRepository(CRUDRepository[ContaPagar]):
    def __init__(self):
        super().__init__(ContaPagar)
