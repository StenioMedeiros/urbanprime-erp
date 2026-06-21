from src.shared.utils.crud_repository import CRUDRepository
from .projeto_model import Projeto


class ProjetoRepository(CRUDRepository[Projeto]):
    def __init__(self):
        super().__init__(Projeto)
