from src.shared.utils.crud_repository import CRUDRepository
from .insumo_model import Insumo


class InsumoRepository(CRUDRepository[Insumo]):
    def __init__(self):
        super().__init__(Insumo)
