from src.shared.utils.crud_repository import CRUDRepository
from .item_ordem_compra_model import ItemOrdemCompra


class ItemOrdemCompraRepository(CRUDRepository[ItemOrdemCompra]):
    def __init__(self):
        super().__init__(ItemOrdemCompra)
