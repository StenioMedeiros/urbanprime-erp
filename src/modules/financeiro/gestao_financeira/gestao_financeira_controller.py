from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.database.connection import get_db
from src.core.security.permissions import require_permission
from .gestao_financeira_model import (
    AbastecimentoFrota, AlocacaoFuncionarioObra, ApropriacaoCusto, CategoriaFinanceira,
    CentroCusto, ContaBancaria, Fatura, HistoricoStatus, ItemOrcamento, ManutencaoFrota,
    MetaIndicador, MovimentacaoCaixa, UtilizacaoFrota,
)
from .gestao_financeira_schema import (
    AbastecimentoFrotaCreate, AbastecimentoFrotaRead, AbastecimentoFrotaUpdate,
    AlocacaoFuncionarioObraCreate, AlocacaoFuncionarioObraRead, AlocacaoFuncionarioObraUpdate,
    ApropriacaoCustoCreate, ApropriacaoCustoRead, ApropriacaoCustoUpdate,
    CategoriaFinanceiraCreate, CategoriaFinanceiraRead, CategoriaFinanceiraUpdate,
    CentroCustoCreate, CentroCustoRead, CentroCustoUpdate,
    ContaBancariaCreate, ContaBancariaRead, ContaBancariaUpdate,
    FaturaCreate, FaturaRead, FaturaUpdate,
    HistoricoStatusCreate, HistoricoStatusRead, HistoricoStatusUpdate,
    ItemOrcamentoCreate, ItemOrcamentoRead, ItemOrcamentoUpdate,
    ManutencaoFrotaCreate, ManutencaoFrotaRead, ManutencaoFrotaUpdate,
    MetaIndicadorCreate, MetaIndicadorRead, MetaIndicadorUpdate,
    MovimentacaoCaixaCreate, MovimentacaoCaixaRead, MovimentacaoCaixaUpdate,
    UtilizacaoFrotaCreate, UtilizacaoFrotaRead, UtilizacaoFrotaUpdate,
)
from .gestao_financeira_service import GestaoFinanceiraService


router = APIRouter()


def crud_router(prefix, tag, model, create_schema, update_schema, read_schema, permission_module):
    entity_router = APIRouter(prefix=prefix, tags=[tag])
    service = GestaoFinanceiraService(model)
    slug = prefix.strip("/").replace("-", "_")

    def list_items(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db),
        _user=Depends(require_permission(permission_module, "visualizar")),
    ):
        return service.list(db, skip=skip, limit=limit)

    def get_item(
        item_id: int,
        db: Session = Depends(get_db),
        _user=Depends(require_permission(permission_module, "visualizar")),
    ):
        item = service.get(db, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro não encontrado")
        return item

    def create_item(
        payload: create_schema,
        db: Session = Depends(get_db),
        _user=Depends(require_permission(permission_module, "criar")),
    ):
        return service.create(db, payload)

    def update_item(
        item_id: int,
        payload: update_schema,
        db: Session = Depends(get_db),
        _user=Depends(require_permission(permission_module, "editar")),
    ):
        item = service.update(db, item_id, payload)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro não encontrado")
        return item

    def delete_item(
        item_id: int,
        db: Session = Depends(get_db),
        _user=Depends(require_permission(permission_module, "excluir")),
    ):
        if not service.delete(db, item_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro não encontrado")

    entity_router.add_api_route("/", list_items, methods=["GET"], response_model=list[read_schema], operation_id=f"list_{slug}")
    entity_router.add_api_route("/{item_id}", get_item, methods=["GET"], response_model=read_schema, operation_id=f"get_{slug}")
    entity_router.add_api_route("/", create_item, methods=["POST"], response_model=read_schema, status_code=201, operation_id=f"create_{slug}")
    entity_router.add_api_route("/{item_id}", update_item, methods=["PUT"], response_model=read_schema, operation_id=f"update_{slug}")
    entity_router.add_api_route("/{item_id}", delete_item, methods=["DELETE"], status_code=204, operation_id=f"delete_{slug}")
    return entity_router


ROUTES = (
    ("/categorias-financeiras", "Financeiro - Categorias", CategoriaFinanceira, CategoriaFinanceiraCreate, CategoriaFinanceiraUpdate, CategoriaFinanceiraRead, "financeiro"),
    ("/centros-custo", "Financeiro - Centros de custo", CentroCusto, CentroCustoCreate, CentroCustoUpdate, CentroCustoRead, "financeiro"),
    ("/contas-bancarias", "Financeiro - Contas bancárias", ContaBancaria, ContaBancariaCreate, ContaBancariaUpdate, ContaBancariaRead, "financeiro"),
    ("/faturas", "Financeiro - Faturamento", Fatura, FaturaCreate, FaturaUpdate, FaturaRead, "financeiro"),
    ("/movimentacoes-caixa", "Financeiro - Caixa", MovimentacaoCaixa, MovimentacaoCaixaCreate, MovimentacaoCaixaUpdate, MovimentacaoCaixaRead, "financeiro"),
    ("/itens-orcamento", "Financeiro - Itens de orçamento", ItemOrcamento, ItemOrcamentoCreate, ItemOrcamentoUpdate, ItemOrcamentoRead, "financeiro"),
    ("/apropriacoes-custo", "Financeiro - Custos por obra", ApropriacaoCusto, ApropriacaoCustoCreate, ApropriacaoCustoUpdate, ApropriacaoCustoRead, "financeiro"),
    ("/metas-indicadores", "Gestão - Metas e indicadores", MetaIndicador, MetaIndicadorCreate, MetaIndicadorUpdate, MetaIndicadorRead, "financeiro"),
    ("/historicos-status", "Gestão - Histórico de status", HistoricoStatus, HistoricoStatusCreate, HistoricoStatusUpdate, HistoricoStatusRead, "auditoria"),
    ("/manutencoes-frota", "Frota - Manutenções", ManutencaoFrota, ManutencaoFrotaCreate, ManutencaoFrotaUpdate, ManutencaoFrotaRead, "planejamento"),
    ("/abastecimentos-frota", "Frota - Abastecimentos", AbastecimentoFrota, AbastecimentoFrotaCreate, AbastecimentoFrotaUpdate, AbastecimentoFrotaRead, "planejamento"),
    ("/utilizacoes-frota", "Frota - Utilizações", UtilizacaoFrota, UtilizacaoFrotaCreate, UtilizacaoFrotaUpdate, UtilizacaoFrotaRead, "planejamento"),
    ("/alocacoes-funcionarios", "RH - Alocações em obras", AlocacaoFuncionarioObra, AlocacaoFuncionarioObraCreate, AlocacaoFuncionarioObraUpdate, AlocacaoFuncionarioObraRead, "rh"),
)

for route_config in ROUTES:
    router.include_router(crud_router(*route_config))
