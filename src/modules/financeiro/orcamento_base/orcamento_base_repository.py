from src.shared.utils.crud_repository import CRUDRepository
from .orcamento_base_model import OrcamentoBase


class OrcamentoBaseRepository(CRUDRepository[OrcamentoBase]):
    def __init__(self):
        super().__init__(OrcamentoBase)
