from __future__ import annotations

from datetime import date, time
from decimal import Decimal
from typing import Any

import streamlit as st
from sqlalchemy import func, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.core.auth.auth_service import AuthService
from src.core.auth.perfil_model import Perfil
from src.core.auth.perfil_permissao_model import PerfilPermissao
from src.core.auth.permissao_model import Permissao
from src.core.auth.usuario_model import Usuario
from src.core.auth.usuario_perfil_model import UsuarioPerfil
from src.core.audit.log_auditoria_model import LogAuditoria
from src.core.database.connection import SessionLocal
from src.core.security.password_manager import hash_password
from src.modules.comercial.agenda_visita.agenda_visita_model import AgendaVisita
from src.modules.comercial.agenda_visita.agenda_visita_schema import AgendaVisitaCreate, AgendaVisitaUpdate
from src.modules.comercial.agenda_visita.agenda_visita_service import AgendaVisitaService
from src.modules.comercial.cliente.cliente_model import Cliente
from src.modules.comercial.cliente.cliente_schema import ClienteCreate, ClienteUpdate
from src.modules.comercial.cliente.cliente_service import ClienteService
from src.modules.comercial.contrato.contrato_model import Contrato
from src.modules.comercial.contrato.contrato_schema import ContratoCreate, ContratoUpdate
from src.modules.comercial.contrato.contrato_service import ContratoService
from src.modules.compras.cotacao.cotacao_model import Cotacao
from src.modules.compras.cotacao.cotacao_schema import CotacaoCreate, CotacaoUpdate
from src.modules.compras.cotacao.cotacao_service import CotacaoService
from src.modules.compras.fornecedor.fornecedor_model import Fornecedor
from src.modules.compras.fornecedor.fornecedor_schema import FornecedorCreate, FornecedorUpdate
from src.modules.compras.fornecedor.fornecedor_service import FornecedorService
from src.modules.compras.ordem_compra.item_ordem_compra_model import ItemOrdemCompra
from src.modules.compras.ordem_compra.item_ordem_compra_schema import ItemOrdemCompraCreate, ItemOrdemCompraUpdate
from src.modules.compras.ordem_compra.item_ordem_compra_service import ItemOrdemCompraService
from src.modules.compras.ordem_compra.ordem_compra_model import OrdemCompra
from src.modules.compras.ordem_compra.ordem_compra_schema import OrdemCompraCreate, OrdemCompraUpdate
from src.modules.compras.ordem_compra.ordem_compra_service import OrdemCompraService
from src.modules.engenharia.projeto.projeto_model import Projeto
from src.modules.engenharia.projeto.projeto_schema import ProjetoCreate, ProjetoUpdate
from src.modules.engenharia.projeto.projeto_service import ProjetoService
from src.modules.engenharia.revisao_projeto.revisao_projeto_model import RevisaoProjeto
from src.modules.engenharia.revisao_projeto.revisao_projeto_schema import RevisaoProjetoCreate, RevisaoProjetoUpdate
from src.modules.engenharia.revisao_projeto.revisao_projeto_service import RevisaoProjetoService
from src.modules.estoque.insumo.insumo_model import Insumo
from src.modules.estoque.insumo.insumo_schema import InsumoCreate, InsumoUpdate
from src.modules.estoque.insumo.insumo_service import InsumoService
from src.modules.estoque.movimentacao_estoque.movimentacao_estoque_model import MovimentacaoEstoque
from src.modules.estoque.movimentacao_estoque.movimentacao_estoque_schema import MovimentacaoEstoqueCreate, MovimentacaoEstoqueUpdate
from src.modules.estoque.movimentacao_estoque.movimentacao_estoque_service import MovimentacaoEstoqueService
from src.modules.financeiro.conta_pagar.conta_pagar_model import ContaPagar
from src.modules.financeiro.conta_pagar.conta_pagar_schema import ContaPagarCreate, ContaPagarUpdate
from src.modules.financeiro.conta_pagar.conta_pagar_service import ContaPagarService
from src.modules.financeiro.conta_receber.conta_receber_model import ContaReceber
from src.modules.financeiro.conta_receber.conta_receber_schema import ContaReceberCreate, ContaReceberUpdate
from src.modules.financeiro.conta_receber.conta_receber_service import ContaReceberService
from src.modules.financeiro.orcamento_base.orcamento_base_model import OrcamentoBase
from src.modules.financeiro.orcamento_base.orcamento_base_schema import OrcamentoBaseCreate, OrcamentoBaseUpdate
from src.modules.financeiro.orcamento_base.orcamento_base_service import OrcamentoBaseService
from src.modules.obras.chamado_tecnico.chamado_tecnico_model import ChamadoTecnico
from src.modules.obras.chamado_tecnico.chamado_tecnico_schema import ChamadoTecnicoCreate, ChamadoTecnicoUpdate
from src.modules.obras.chamado_tecnico.chamado_tecnico_service import ChamadoTecnicoService
from src.modules.obras.diario_obra.diario_obra_model import DiarioObra
from src.modules.obras.diario_obra.diario_obra_schema import DiarioObraCreate, DiarioObraUpdate
from src.modules.obras.diario_obra.diario_obra_service import DiarioObraService
from src.modules.obras.medicao.medicao_model import Medicao
from src.modules.obras.medicao.medicao_schema import MedicaoCreate, MedicaoUpdate
from src.modules.obras.medicao.medicao_service import MedicaoService
from src.modules.obras.obra.obra_model import Obra
from src.modules.obras.obra.obra_schema import ObraCreate, ObraUpdate
from src.modules.obras.obra.obra_service import ObraService
from src.modules.planejamento.cronograma.cronograma_model import Cronograma
from src.modules.planejamento.cronograma.cronograma_schema import CronogramaCreate, CronogramaUpdate
from src.modules.planejamento.cronograma.cronograma_service import CronogramaService
from src.modules.planejamento.frota.frota_model import Frota
from src.modules.planejamento.frota.frota_schema import FrotaCreate, FrotaUpdate
from src.modules.planejamento.frota.frota_service import FrotaService
from src.modules.rh.folha_pagamento.folha_pagamento_model import FolhaPagamento
from src.modules.rh.folha_pagamento.folha_pagamento_schema import FolhaPagamentoCreate, FolhaPagamentoUpdate
from src.modules.rh.folha_pagamento.folha_pagamento_service import FolhaPagamentoService
from src.modules.rh.funcionario.funcionario_model import Funcionario
from src.modules.rh.funcionario.funcionario_schema import FuncionarioCreate, FuncionarioUpdate
from src.modules.rh.funcionario.funcionario_service import FuncionarioService
from src.modules.rh.registro_ponto.registro_ponto_model import RegistroPonto
from src.modules.rh.registro_ponto.registro_ponto_schema import RegistroPontoCreate, RegistroPontoUpdate
from src.modules.rh.registro_ponto.registro_ponto_service import RegistroPontoService


st.set_page_config(page_title="UrbanPrime ERP", layout="wide")


STATUSES = [
    "ativo",
    "inativo",
    "planejada",
    "em_andamento",
    "concluida",
    "cancelado",
    "em_aberto",
    "pago",
    "recebido",
    "pendente",
    "aprovado",
    "aberto",
    "fechado",
    "vigente",
    "disponivel",
    "agendada",
    "em_elaboracao",
    "aberta",
    "planejado",
]

FIELD_LABELS = {
    "id": "ID",
    "cliente_id": "Cliente",
    "contrato_id": "Contrato",
    "projeto_id": "Projeto",
    "obra_id": "Obra",
    "funcionario_id": "Funcionario",
    "responsavel_id": "Responsavel",
    "solicitante_id": "Solicitante",
    "aprovado_por_id": "Aprovado por",
    "fornecedor_id": "Fornecedor",
    "ordem_compra_id": "Ordem de compra",
    "insumo_id": "Insumo",
    "medicao_id": "Medicao",
    "nome": "Nome",
    "descricao": "Descricao",
    "status": "Status",
    "valor_total": "Valor total",
    "valor": "Valor",
    "data_vencimento": "Data de vencimento",
}

FK_CONFIG = {
    "cliente_id": (Cliente, "nome"),
    "contrato_id": (Contrato, "numero_contrato"),
    "projeto_id": (Projeto, "nome"),
    "obra_id": (Obra, "nome"),
    "funcionario_id": (Funcionario, "nome"),
    "responsavel_id": (Funcionario, "nome"),
    "solicitante_id": (Funcionario, "nome"),
    "aprovado_por_id": (Funcionario, "nome"),
    "fornecedor_id": (Fornecedor, "razao_social"),
    "ordem_compra_id": (OrdemCompra, "numero"),
    "insumo_id": (Insumo, "nome"),
    "medicao_id": (Medicao, "competencia"),
}


PAGES: dict[str, dict[str, Any]] = {
    "Dashboard": {"description": "Indicadores operacionais e financeiros em tempo real."},
    "Gestao Usuarios": {"description": "Crie usuarios internos vinculados a funcionarios e perfis."},
    "Gestao Perfis": {"description": "Administre perfis e permissoes de acesso."},
    "Auditoria": {"description": "Consulte os ultimos eventos criticos registrados no sistema."},
    "Funcionarios": {"model": Funcionario, "service": FuncionarioService(), "create": FuncionarioCreate, "update": FuncionarioUpdate, "description": "Cadastro interno de colaboradores da UrbanPrime."},
    "Clientes": {"model": Cliente, "service": ClienteService(), "create": ClienteCreate, "update": ClienteUpdate, "description": "Cadastro comercial de clientes. Clientes nao fazem login."},
    "Contratos": {"model": Contrato, "service": ContratoService(), "create": ContratoCreate, "update": ContratoUpdate, "description": "Contratos vinculados a clientes, sem vinculo direto com obra."},
    "Agenda Visitas": {"model": AgendaVisita, "service": AgendaVisitaService(), "create": AgendaVisitaCreate, "update": AgendaVisitaUpdate, "description": "Agenda comercial e tecnica relacionada a clientes."},
    "Projetos": {"model": Projeto, "service": ProjetoService(), "create": ProjetoCreate, "update": ProjetoUpdate, "description": "Projetos nascidos a partir de contratos."},
    "Revisoes Projeto": {"model": RevisaoProjeto, "service": RevisaoProjetoService(), "create": RevisaoProjetoCreate, "update": RevisaoProjetoUpdate, "description": "Controle de revisoes tecnicas dos projetos."},
    "Obras": {"model": Obra, "service": ObraService(), "create": ObraCreate, "update": ObraUpdate, "description": "Obras vinculadas a contrato e projeto. O orcamento oficial fica em Orcamentos Base."},
    "Diarios Obra": {"model": DiarioObra, "service": DiarioObraService(), "create": DiarioObraCreate, "update": DiarioObraUpdate, "description": "Registros diarios de atividades, clima e ocorrencias da obra."},
    "Medicoes": {"model": Medicao, "service": MedicaoService(), "create": MedicaoCreate, "update": MedicaoUpdate, "description": "Medicoes por obra e competencia."},
    "Chamados Tecnicos": {"model": ChamadoTecnico, "service": ChamadoTecnicoService(), "create": ChamadoTecnicoCreate, "update": ChamadoTecnicoUpdate, "description": "Chamados tecnicos relacionados as obras."},
    "Orcamentos Base": {"model": OrcamentoBase, "service": OrcamentoBaseService(), "create": OrcamentoBaseCreate, "update": OrcamentoBaseUpdate, "description": "Fonte oficial do orcamento aprovado da obra."},
    "Contas Pagar": {"model": ContaPagar, "service": ContaPagarService(), "create": ContaPagarCreate, "update": ContaPagarUpdate, "description": "Contas a pagar, incluindo vinculo com ordem de compra."},
    "Contas Receber": {"model": ContaReceber, "service": ContaReceberService(), "create": ContaReceberCreate, "update": ContaReceberUpdate, "description": "Contas a receber vinculadas a clientes, contratos ou medicoes."},
    "Insumos": {"model": Insumo, "service": InsumoService(), "create": InsumoCreate, "update": InsumoUpdate, "description": "Cadastro de insumos e controle de estoque minimo."},
    "Movimentacoes Estoque": {"model": MovimentacaoEstoque, "service": MovimentacaoEstoqueService(), "create": MovimentacaoEstoqueCreate, "update": MovimentacaoEstoqueUpdate, "description": "Entradas e saidas de insumos por obra."},
    "Fornecedores": {"model": Fornecedor, "service": FornecedorService(), "create": FornecedorCreate, "update": FornecedorUpdate, "description": "Cadastro de fornecedores. Fornecedores nao fazem login."},
    "Cotacoes": {"model": Cotacao, "service": CotacaoService(), "create": CotacaoCreate, "update": CotacaoUpdate, "description": "Cotacoes de compras por fornecedor e obra."},
    "Ordens Compra": {"model": OrdemCompra, "service": OrdemCompraService(), "create": OrdemCompraCreate, "update": OrdemCompraUpdate, "description": "Ordens de compra que podem alimentar contas a pagar."},
    "Itens Ordem Compra": {"model": ItemOrdemCompra, "service": ItemOrdemCompraService(), "create": ItemOrdemCompraCreate, "update": ItemOrdemCompraUpdate, "description": "Itens detalhados das ordens de compra."},
    "Frotas": {"model": Frota, "service": FrotaService(), "create": FrotaCreate, "update": FrotaUpdate, "description": "Controle de frota e alocacao em obras."},
    "Cronogramas": {"model": Cronograma, "service": CronogramaService(), "create": CronogramaCreate, "update": CronogramaUpdate, "description": "Planejamento de atividades por obra."},
    "Registro Ponto": {"model": RegistroPonto, "service": RegistroPontoService(), "create": RegistroPontoCreate, "update": RegistroPontoUpdate, "description": "Registro de jornada dos funcionarios."},
    "Folha Pagamento": {"model": FolhaPagamento, "service": FolhaPagamentoService(), "create": FolhaPagamentoCreate, "update": FolhaPagamentoUpdate, "description": "Folha de pagamento por competencia."},
}


def get_db() -> Session:
    return SessionLocal()


def label_for(field: str) -> str:
    return FIELD_LABELS.get(field, field.replace("_", " ").title())


def model_columns(model: Any) -> list[str]:
    return [column.name for column in model.__table__.columns]


def editable_columns(model: Any) -> list[str]:
    blocked = {"id", "created_at", "updated_at", "data_criacao", "ultimo_login"}
    return [name for name in model_columns(model) if name not in blocked]


def rows_as_dicts(rows: list[Any]) -> list[dict[str, Any]]:
    result = []
    for row in rows:
        item = {}
        for name in model_columns(type(row)):
            value = getattr(row, name)
            item[name] = str(value) if isinstance(value, Decimal) else value
        result.append(item)
    return result


def option_label(row: Any, label_field: str) -> str:
    label = getattr(row, label_field, None) or getattr(row, "nome", None) or getattr(row, "id")
    return f"{row.id} - {label}"


def fk_input(db: Session, field: str, required: bool, default: int | None = None, key: str = "") -> int | None:
    model, label_field = FK_CONFIG[field]
    rows = db.query(model).order_by(model.id.desc()).limit(200).all()
    options: list[int | None] = [None] if not required else []
    options.extend([row.id for row in rows])
    labels = {None: "Nenhum"}
    labels.update({row.id: option_label(row, label_field) for row in rows})
    if required and not rows:
        st.warning(f"Cadastre primeiro: {label_for(field)}.")
        return None
    index = options.index(default) if default in options else 0
    return st.selectbox(label_for(field), options, format_func=lambda value: labels.get(value, str(value)), index=index, key=key)


def value_input(db: Session, model: Any, field: str, default: Any = None, key: str = "") -> Any:
    column = model.__table__.columns[field]
    required = not column.nullable and column.default is None and field != "id"
    label = label_for(field)
    if field in FK_CONFIG:
        return fk_input(db, field, required, default, key)
    if field == "status":
        options = STATUSES
        current = default if default in options else (column.default.arg if column.default is not None and isinstance(column.default.arg, str) else options[0])
        return st.selectbox(label, options, index=options.index(current), key=key)
    python_type = getattr(column.type, "python_type", str)
    if python_type is bool:
        return st.checkbox(label, value=bool(default), key=key)
    if python_type is int:
        return st.number_input(label, min_value=0, step=1, value=int(default or 0), key=key)
    if python_type is Decimal:
        value = float(default or 0)
        return Decimal(str(st.number_input(label, min_value=0.0, step=0.01, value=value, key=key)))
    if python_type is date:
        value = default if isinstance(default, date) else date.today()
        return st.date_input(label, value=value, key=key)
    if python_type is time:
        value = default if isinstance(default, time) else time(8, 0)
        return st.time_input(label, value=value, key=key)
    if "descricao" in field or "observa" in field or field in {"endereco", "atividades", "ocorrencias", "motivo"}:
        value = "" if default is None else str(default)
        text_value = st.text_area(label, value=value, key=key)
    else:
        value = "" if default is None else str(default)
        text_value = st.text_input(label, value=value, key=key)
    if not text_value and not required:
        return None
    return text_value


def safe_count(db: Session, sql: str) -> int:
    try:
        return int(db.execute(text(sql)).scalar() or 0)
    except SQLAlchemyError:
        return 0


def login_screen() -> None:
    st.title("UrbanPrime ERP")
    st.caption("Acesso interno exclusivo para funcionarios da UrbanPrime.")
    with st.form("login_form"):
        username = st.text_input("Usuario")
        password = st.text_input("Senha", type="password")
        submitted = st.form_submit_button("Entrar")
    if submitted:
        db = get_db()
        try:
            user, access_token, refresh_token = AuthService().authenticate(db, username, password)
            st.session_state["authenticated"] = True
            st.session_state["user_id"] = user.id
            st.session_state["username"] = user.username
            st.session_state["access_token"] = access_token
            st.session_state["refresh_token"] = refresh_token
            st.success("Login realizado com sucesso.")
            st.rerun()
        except Exception as exc:
            st.error(f"Nao foi possivel entrar: {exc}")
        finally:
            db.close()


def sidebar_menu() -> str:
    st.sidebar.title("UrbanPrime ERP")
    st.sidebar.caption(f"Usuario: {st.session_state.get('username', '')}")
    selected = st.sidebar.radio("Menu", list(PAGES.keys()))
    if st.sidebar.button("Sair"):
        st.session_state.clear()
        st.rerun()
    return selected


def require_login() -> bool:
    if not st.session_state.get("authenticated"):
        login_screen()
        return False
    return True


def render_dashboard() -> None:
    st.title("Dashboard")
    st.write(PAGES["Dashboard"]["description"])
    db = get_db()
    try:
        cols = st.columns(6)
        cols[0].metric("Obras", safe_count(db, "SELECT COUNT(*) FROM obras"))
        cols[1].metric("Contratos ativos", safe_count(db, "SELECT COUNT(*) FROM contratos WHERE status = 'ativo'"))
        cols[2].metric("Pagar em aberto", safe_count(db, "SELECT COUNT(*) FROM contas_pagar WHERE status = 'em_aberto'"))
        cols[3].metric("Receber em aberto", safe_count(db, "SELECT COUNT(*) FROM contas_receber WHERE status = 'em_aberto'"))
        cols[4].metric("Estoque minimo", safe_count(db, "SELECT COUNT(*) FROM insumos WHERE quantidade_atual <= estoque_minimo"))
        cols[5].metric("Usuarios ativos", safe_count(db, "SELECT COUNT(*) FROM usuarios WHERE ativo = true"))
        st.subheader("Fluxo principal")
        flow_cols = st.columns(5)
        flow_cols[0].metric("Clientes", safe_count(db, "SELECT COUNT(*) FROM clientes"))
        flow_cols[1].metric("Contratos", safe_count(db, "SELECT COUNT(*) FROM contratos"))
        flow_cols[2].metric("Projetos", safe_count(db, "SELECT COUNT(*) FROM projetos"))
        flow_cols[3].metric("Obras", safe_count(db, "SELECT COUNT(*) FROM obras"))
        flow_cols[4].metric("Orcamentos Base", safe_count(db, "SELECT COUNT(*) FROM orcamentos_base"))
        st.subheader("Ultimos logs de auditoria")
        logs = db.query(LogAuditoria).order_by(LogAuditoria.created_at.desc()).limit(20).all()
        if logs:
            st.dataframe(rows_as_dicts(logs), width="stretch", hide_index=True)
        else:
            st.info("Nenhum registro encontrado.")
    except Exception as exc:
        st.error(f"Erro ao carregar dashboard: {exc}")
    finally:
        db.close()


def render_listing(db: Session, cfg: dict[str, Any]) -> None:
    rows = cfg["service"].list(db, skip=0, limit=500)
    if rows:
        st.dataframe(rows_as_dicts(rows), width="stretch", hide_index=True)
    else:
        st.info("Nenhum registro encontrado.")


def render_create_form(db: Session, cfg: dict[str, Any], page_name: str) -> None:
    model = cfg["model"]
    create_schema = cfg["create"]
    with st.form(f"create_{page_name}"):
        st.subheader("Cadastrar")
        payload: dict[str, Any] = {}
        for field in editable_columns(model):
            payload[field] = value_input(db, model, field, key=f"create_{page_name}_{field}")
        submitted = st.form_submit_button("Salvar")
    if submitted:
        try:
            cleaned = {key: value for key, value in payload.items() if value is not None}
            item = cfg["service"].create(db, create_schema(**cleaned))
            st.success(f"Registro salvo com ID {item.id}.")
            st.rerun()
        except Exception as exc:
            db.rollback()
            st.error(f"Erro ao salvar: {exc}")


def render_edit_form(db: Session, cfg: dict[str, Any], page_name: str) -> None:
    model = cfg["model"]
    update_schema = cfg["update"]
    st.subheader("Consultar ou editar")
    item_id = st.number_input("ID do registro", min_value=1, step=1, key=f"edit_id_{page_name}")
    if st.button("Consultar por ID", key=f"lookup_{page_name}"):
        st.session_state[f"selected_{page_name}"] = int(item_id)
    selected_id = st.session_state.get(f"selected_{page_name}", int(item_id))
    item = cfg["service"].get(db, int(selected_id)) if selected_id else None
    if not item:
        st.warning("Informe um ID existente para editar.")
        return
    st.caption(f"Editando registro ID {item.id}")
    with st.form(f"edit_{page_name}_{item.id}"):
        payload: dict[str, Any] = {}
        for field in editable_columns(model):
            payload[field] = value_input(db, model, field, getattr(item, field), key=f"edit_{page_name}_{item.id}_{field}")
        submitted = st.form_submit_button("Salvar alteracoes")
    if submitted:
        try:
            cleaned = {key: value for key, value in payload.items() if value is not None}
            cfg["service"].update(db, item.id, update_schema(**cleaned))
            st.success("Registro atualizado com sucesso.")
            st.rerun()
        except Exception as exc:
            db.rollback()
            st.error(f"Erro ao atualizar: {exc}")


def render_crud_page(page_name: str, cfg: dict[str, Any]) -> None:
    st.title(page_name)
    st.write(cfg["description"])
    if st.button("Atualizar / Recarregar", key=f"reload_{page_name}"):
        st.rerun()
    db = get_db()
    try:
        st.subheader("Registros")
        render_listing(db, cfg)
        left, right = st.columns(2)
        with left:
            render_create_form(db, cfg, page_name)
        with right:
            render_edit_form(db, cfg, page_name)
    except Exception as exc:
        st.error(f"Erro ao carregar pagina: {exc}")
    finally:
        db.close()


def render_users() -> None:
    st.title("Gestao de Usuarios")
    st.write(PAGES["Gestao Usuarios"]["description"])
    db = get_db()
    try:
        if st.button("Atualizar / Recarregar", key="reload_users"):
            st.rerun()
        rows = db.query(Usuario).order_by(Usuario.id.desc()).limit(500).all()
        if rows:
            st.dataframe(rows_as_dicts(rows), width="stretch", hide_index=True)
        else:
            st.info("Nenhum registro encontrado.")
        with st.form("create_user"):
            st.subheader("Cadastrar usuario interno")
            funcionario_id = fk_input(db, "funcionario_id", True, key="user_funcionario")
            username = st.text_input("Usuario")
            email = st.text_input("Email")
            password = st.text_input("Senha inicial", type="password")
            perfil_options = db.query(Perfil).filter(Perfil.ativo.is_(True)).order_by(Perfil.nome).all()
            perfil_id = st.selectbox("Perfil", [p.id for p in perfil_options], format_func=lambda pid: next((p.nome for p in perfil_options if p.id == pid), str(pid))) if perfil_options else None
            ativo = st.checkbox("Ativo", value=True)
            submitted = st.form_submit_button("Salvar")
        if submitted:
            if not funcionario_id or not username or not email or not password:
                st.error("Preencha funcionario, usuario, email e senha.")
            else:
                user = Usuario(funcionario_id=funcionario_id, username=username, email=email, senha_hash=hash_password(password), ativo=ativo, bloqueado=False)
                db.add(user)
                db.commit()
                db.refresh(user)
                if perfil_id:
                    db.add(UsuarioPerfil(usuario_id=user.id, perfil_id=perfil_id))
                    db.commit()
                st.success(f"Usuario criado com ID {user.id}.")
                st.rerun()
        st.subheader("Editar status do usuario")
        edit_id = st.number_input("ID do usuario", min_value=1, step=1, key="user_edit_id")
        user = db.get(Usuario, int(edit_id))
        if user:
            ativo = st.checkbox("Ativo", value=user.ativo, key="user_edit_ativo")
            bloqueado = st.checkbox("Bloqueado", value=user.bloqueado, key="user_edit_bloqueado")
            if st.button("Salvar status do usuario"):
                user.ativo = ativo
                user.bloqueado = bloqueado
                db.commit()
                st.success("Usuario atualizado.")
                st.rerun()
        else:
            st.warning("Informe um ID existente para editar.")
    except Exception as exc:
        db.rollback()
        st.error(f"Erro em usuarios: {exc}")
    finally:
        db.close()


def render_profiles() -> None:
    st.title("Gestao de Perfis")
    st.write(PAGES["Gestao Perfis"]["description"])
    db = get_db()
    try:
        if st.button("Atualizar / Recarregar", key="reload_profiles"):
            st.rerun()
        profiles = db.query(Perfil).order_by(Perfil.id).all()
        if profiles:
            st.dataframe(rows_as_dicts(profiles), width="stretch", hide_index=True)
        else:
            st.info("Nenhum registro encontrado.")
        with st.form("create_profile"):
            st.subheader("Cadastrar perfil")
            nome = st.text_input("Nome")
            descricao = st.text_area("Descricao")
            nivel = st.number_input("Nivel de acesso", min_value=1, max_value=100, value=10, step=1)
            ativo = st.checkbox("Ativo", value=True)
            submitted = st.form_submit_button("Salvar")
        if submitted:
            db.add(Perfil(nome=nome, descricao=descricao, nivel_acesso=nivel, ativo=ativo))
            db.commit()
            st.success("Perfil criado com sucesso.")
            st.rerun()
        st.subheader("Permissoes")
        permissions = db.query(Permissao).order_by(Permissao.modulo, Permissao.acao).all()
        if permissions:
            st.dataframe(rows_as_dicts(permissions), width="stretch", hide_index=True)
        else:
            st.info("Nenhum registro encontrado.")
        st.subheader("Vincular permissao a perfil")
        if profiles and permissions:
            perfil_id = st.selectbox("Perfil", [p.id for p in profiles], format_func=lambda pid: next((p.nome for p in profiles if p.id == pid), str(pid)), key="pp_perfil")
            permissao_id = st.selectbox("Permissao", [p.id for p in permissions], format_func=lambda pid: next((f"{p.modulo}:{p.acao}" for p in permissions if p.id == pid), str(pid)), key="pp_perm")
            if st.button("Salvar permissao no perfil"):
                exists = db.query(PerfilPermissao).filter_by(perfil_id=perfil_id, permissao_id=permissao_id).first()
                if exists:
                    st.warning("Permissao ja vinculada.")
                else:
                    db.add(PerfilPermissao(perfil_id=perfil_id, permissao_id=permissao_id))
                    db.commit()
                    st.success("Permissao vinculada.")
                    st.rerun()
    except Exception as exc:
        db.rollback()
        st.error(f"Erro em perfis: {exc}")
    finally:
        db.close()


def render_audit() -> None:
    st.title("Auditoria")
    st.write(PAGES["Auditoria"]["description"])
    db = get_db()
    try:
        if st.button("Atualizar / Recarregar", key="reload_audit"):
            st.rerun()
        total = db.query(func.count(LogAuditoria.id)).scalar() or 0
        st.metric("Total de logs", total)
        logs = db.query(LogAuditoria).order_by(LogAuditoria.created_at.desc()).limit(500).all()
        if logs:
            st.dataframe(rows_as_dicts(logs), width="stretch", hide_index=True)
        else:
            st.info("Nenhum registro encontrado.")
        with st.form("audit_lookup"):
            log_id = st.number_input("Consultar log por ID", min_value=1, step=1)
            submitted = st.form_submit_button("Consultar")
        if submitted:
            log = db.get(LogAuditoria, int(log_id))
            if log:
                st.json(rows_as_dicts([log])[0])
            else:
                st.warning("Nenhum registro encontrado.")
    except Exception as exc:
        st.error(f"Erro em auditoria: {exc}")
    finally:
        db.close()


def main() -> None:
    if not require_login():
        return
    page_name = sidebar_menu()
    if page_name == "Dashboard":
        render_dashboard()
    elif page_name == "Gestao Usuarios":
        render_users()
    elif page_name == "Gestao Perfis":
        render_profiles()
    elif page_name == "Auditoria":
        render_audit()
    else:
        render_crud_page(page_name, PAGES[page_name])


if __name__ == "__main__":
    main()
