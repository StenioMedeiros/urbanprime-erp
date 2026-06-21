from src.shared.utils.crud_repository import CRUDRepository
from .medicao_model import Medicao


class MedicaoRepository(CRUDRepository[Medicao]):
    def __init__(self):
        super().__init__(Medicao)
