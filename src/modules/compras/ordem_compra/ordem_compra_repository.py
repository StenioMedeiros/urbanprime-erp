from src.shared.utils.crud_repository import CRUDRepository
from .ordem_compra_model import OrdemCompra


class OrdemCompraRepository(CRUDRepository[OrdemCompra]):
    def __init__(self):
        super().__init__(OrdemCompra)
