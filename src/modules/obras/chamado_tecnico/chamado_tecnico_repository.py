from src.shared.utils.crud_repository import CRUDRepository
from .chamado_tecnico_model import ChamadoTecnico


class ChamadoTecnicoRepository(CRUDRepository[ChamadoTecnico]):
    def __init__(self):
        super().__init__(ChamadoTecnico)
