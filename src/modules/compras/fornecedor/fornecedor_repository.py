from src.shared.utils.crud_repository import CRUDRepository
from .fornecedor_model import Fornecedor


class FornecedorRepository(CRUDRepository[Fornecedor]):
    def __init__(self):
        super().__init__(Fornecedor)
