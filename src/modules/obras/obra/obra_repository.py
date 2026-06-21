from src.shared.utils.crud_repository import CRUDRepository
from .obra_model import Obra


class ObraRepository(CRUDRepository[Obra]):
    def __init__(self):
        super().__init__(Obra)
