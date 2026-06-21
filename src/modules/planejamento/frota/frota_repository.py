from src.shared.utils.crud_repository import CRUDRepository
from .frota_model import Frota


class FrotaRepository(CRUDRepository[Frota]):
    def __init__(self):
        super().__init__(Frota)
