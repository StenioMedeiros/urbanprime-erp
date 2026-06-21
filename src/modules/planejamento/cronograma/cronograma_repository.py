from src.shared.utils.crud_repository import CRUDRepository
from .cronograma_model import Cronograma


class CronogramaRepository(CRUDRepository[Cronograma]):
    def __init__(self):
        super().__init__(Cronograma)
