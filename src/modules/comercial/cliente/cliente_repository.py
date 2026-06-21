from src.shared.utils.crud_repository import CRUDRepository
from .cliente_model import Cliente


class ClienteRepository(CRUDRepository[Cliente]):
    def __init__(self):
        super().__init__(Cliente)
