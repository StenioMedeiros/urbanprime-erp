from src.shared.utils.crud_repository import CRUDRepository
from .diario_obra_model import DiarioObra


class DiarioObraRepository(CRUDRepository[DiarioObra]):
    def __init__(self):
        super().__init__(DiarioObra)
