from src.shared.utils.crud_repository import CRUDRepository
from .revisao_projeto_model import RevisaoProjeto


class RevisaoProjetoRepository(CRUDRepository[RevisaoProjeto]):
    def __init__(self):
        super().__init__(RevisaoProjeto)
