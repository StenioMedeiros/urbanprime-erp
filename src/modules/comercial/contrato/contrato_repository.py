from src.shared.utils.crud_repository import CRUDRepository
from .contrato_model import Contrato


class ContratoRepository(CRUDRepository[Contrato]):
    def __init__(self):
        super().__init__(Contrato)
