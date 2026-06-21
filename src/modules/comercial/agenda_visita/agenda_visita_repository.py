from src.shared.utils.crud_repository import CRUDRepository
from .agenda_visita_model import AgendaVisita


class AgendaVisitaRepository(CRUDRepository[AgendaVisita]):
    def __init__(self):
        super().__init__(AgendaVisita)
