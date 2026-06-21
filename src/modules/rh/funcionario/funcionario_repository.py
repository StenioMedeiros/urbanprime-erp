from src.shared.utils.crud_repository import CRUDRepository
from .funcionario_model import Funcionario


class FuncionarioRepository(CRUDRepository[Funcionario]):
    def __init__(self):
        super().__init__(Funcionario)
