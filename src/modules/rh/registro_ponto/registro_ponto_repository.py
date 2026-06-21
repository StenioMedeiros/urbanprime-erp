from src.shared.utils.crud_repository import CRUDRepository
from .registro_ponto_model import RegistroPonto


class RegistroPontoRepository(CRUDRepository[RegistroPonto]):
    def __init__(self):
        super().__init__(RegistroPonto)
