from __future__ import annotations

from datetime import date, datetime, time
from decimal import Decimal
from pathlib import Path
from typing import Any
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

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
from src.core.audit.audit_logger import (
    add_audit_log,
    log_action,
    model_snapshot,
    set_audit_context,
)
from src.core.audit.log_auditoria_model import LogAuditoria
from src.core.config.settings import get_settings
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
from src.shared.utils.brazil_localization import (
    BRAZIL_STATES,
    format_cep,
    format_cnpj,
    format_competence_br,
    format_cpf,
    format_cpf_cnpj,
    format_currency_br,
    format_date_br,
    format_datetime_br,
    format_number_br,
    format_phone_br,
    normalize_brazilian_field,
    now_in_timezone,
    now_local_naive,
    today_in_timezone,
)
from src.modules.financeiro.gestao_financeira.gestao_financeira_model import (
    AbastecimentoFrota, AlocacaoFuncionarioObra, ApropriacaoCusto, CategoriaFinanceira,
    CentroCusto, ContaBancaria, Fatura, ItemOrcamento, ManutencaoFrota,
    MetaIndicador, MovimentacaoCaixa, UtilizacaoFrota,
)
from src.modules.financeiro.gestao_financeira.gestao_financeira_schema import (
    AbastecimentoFrotaCreate, AbastecimentoFrotaUpdate,
    AlocacaoFuncionarioObraCreate, AlocacaoFuncionarioObraUpdate,
    ApropriacaoCustoCreate, ApropriacaoCustoUpdate,
    CategoriaFinanceiraCreate, CategoriaFinanceiraUpdate,
    CentroCustoCreate, CentroCustoUpdate,
    ContaBancariaCreate, ContaBancariaUpdate,
    FaturaCreate, FaturaUpdate,
    ItemOrcamentoCreate, ItemOrcamentoUpdate,
    ManutencaoFrotaCreate, ManutencaoFrotaUpdate,
    MetaIndicadorCreate, MetaIndicadorUpdate,
    MovimentacaoCaixaCreate, MovimentacaoCaixaUpdate,
    UtilizacaoFrotaCreate, UtilizacaoFrotaUpdate,
)
from src.modules.financeiro.gestao_financeira.gestao_financeira_service import GestaoFinanceiraService
from src.ui.dashboard_hub import render_dashboard_hub
from src.ui.financial_dashboard import render_financial_area


st.set_page_config(page_title="UrbanPrime ERP", page_icon="🏗️", layout="wide", initial_sidebar_state="expanded")
st.markdown(
    """
    <style>
    .block-container {padding-top: 2rem; padding-bottom: 3rem; max-width: 1500px;}
    [data-testid="stSidebar"] {border-right: 1px solid #e5e7eb;}
    [data-testid="stMetric"] {background: #ffffff; border: 1px solid #e5e7eb; padding: 1rem; border-radius: .75rem;}
    .stButton > button, .stFormSubmitButton > button {border-radius: .55rem; font-weight: 600;}
    h1, h2, h3 {letter-spacing: -.02em;}
    </style>
    """,
    unsafe_allow_html=True,
)


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
    "emitida",
    "conciliada",
    "em_manutencao",
]

APP_SETTINGS = get_settings()

FIELD_LABELS = {
    "id": "ID",
    "cliente_id": "Cliente",
    "contrato_id": "Contrato",
    "projeto_id": "Projeto",
    "obra_id": "Obra",
    "funcionario_id": "Funcionário",
    "responsavel_id": "Responsável",
    "solicitante_id": "Solicitante",
    "aprovado_por_id": "Aprovado por",
    "fornecedor_id": "Fornecedor",
    "ordem_compra_id": "Ordem de compra",
    "insumo_id": "Insumo",
    "medicao_id": "Medição",
    "usuario_id": "Usuário",
    "nome": "Nome",
    "descricao": "Descrição",
    "status": "Status",
    "valor_total": "Valor total",
    "valor": "Valor",
    "data_vencimento": "Data de vencimento",
    "cpf_cnpj": "CPF/CNPJ", "data_inicio": "Data de início", "data_fim": "Data de término",
    "data_previsao_fim": "Previsão de término", "data_previsao_entrega": "Previsão de entrega",
    "data_assinatura": "Data de assinatura", "data_visita": "Data da visita",
    "razao_social": "Razão social", "nome_fantasia": "Nome fantasia",
    "numero_contrato": "Número do contrato", "tipo_pessoa": "Tipo de pessoa",
    "tipo_projeto": "Tipo de projeto", "data_registro": "Data do registro",
    "valor_medido": "Valor medido", "data_medicao": "Data da medição",
    "data_aprovacao": "Data da aprovação", "unidade_medida": "Unidade",
    "quantidade_atual": "Quantidade atual", "estoque_minimo": "Estoque mínimo",
    "valor_unitario": "Valor unitário", "data_movimentacao": "Data da movimentação",
    "data_cotacao": "Data da cotação", "data_emissao": "Data de emissão",
    "percentual_concluido": "Percentual concluído", "salario_base": "Salário-base",
    "salario_bruto": "Salário bruto", "salario_liquido": "Salário líquido",
    "data_admissao": "Data de admissão", "data_demissao": "Data de demissão",
    "data_nascimento": "Data de nascimento", "email_corporativo": "E-mail corporativo",
    "observacoes": "Observações", "observacao": "Observação", "ocorrencias": "Ocorrências",
    "categoria_financeira_id": "Categoria financeira", "categoria_pai_id": "Categoria superior",
    "centro_custo_id": "Centro de custo", "conta_bancaria_id": "Conta bancária",
    "conta_pagar_id": "Conta a pagar", "conta_receber_id": "Conta a receber",
    "fatura_id": "Fatura", "orcamento_base_id": "Orçamento-base", "frota_id": "Veículo ou equipamento",
    "cotacao_id": "Cotação de origem", "numero_documento": "Número do documento",
    "data_competencia": "Data de competência", "competencia": "Competência",
    "valor_bruto": "Valor bruto", "valor_liquido": "Valor líquido", "impostos": "Impostos",
    "retencoes": "Retenções", "saldo_inicial": "Saldo inicial", "data_saldo_inicial": "Data do saldo inicial",
    "numero_conta": "Número da conta", "tipo_conta": "Tipo de conta", "forma_pagamento": "Forma de pagamento",
    "conciliado": "Conciliado", "data_conciliacao": "Data da conciliação",
    "codigo_indicador": "Código do indicador", "valor_meta": "Valor da meta",
    "percentual_fisico": "Avanço físico", "peso_percentual": "Peso da atividade",
    "data_apropriacao": "Data da apropriação", "tipo_custo": "Tipo de custo", "origem": "Origem",
    "data_entrada": "Data de entrada", "data_saida": "Data de saída", "custo": "Custo",
    "data_abastecimento": "Data do abastecimento", "litros": "Litros",
    "quilometragem_horimetro": "Quilometragem ou horímetro", "data_utilizacao": "Data da utilização",
    "horas_utilizadas": "Horas utilizadas", "custo_hora": "Custo por hora",
    "horimetro_inicial": "Horímetro inicial", "horimetro_final": "Horímetro final",
    "ano_fabricacao": "Ano de fabricação", "data_aquisicao": "Data de aquisição",
    "valor_aquisicao": "Valor de aquisição", "horimetro_atual": "Horímetro atual",
    "agencia": "Agência", "aprovado": "Aprovado", "arquivo_contrato": "Arquivo do contrato",
    "arquivo_projeto": "Arquivo do projeto", "arquivo_revisao": "Arquivo da revisão",
    "atividade": "Atividade", "atividades": "Atividades", "ativo": "Ativo",
    "banco": "Banco", "cargo": "Cargo", "cep": "CEP", "cidade": "Cidade",
    "clima": "Clima", "cnpj": "CNPJ", "codigo": "Código", "contabilizavel": "Contabilizável",
    "cpf": "CPF", "data": "Data", "data_entrega": "Data de entrega",
    "data_pagamento": "Data do pagamento", "data_recebimento": "Data do recebimento",
    "data_revisao": "Data da revisão", "descontos": "Descontos", "email": "E-mail",
    "endereco": "Endereço", "entrada": "Entrada", "estado": "UF", "etapa": "Etapa",
    "funcao": "Função", "horario": "Horário", "horimetro": "Horímetro",
    "identificacao": "Identificação", "local_visita": "Local da visita", "marca": "Marca",
    "modelo": "Modelo", "motivo": "Motivo", "numero": "Número",
    "numero_revisao": "Número da revisão", "placa": "Placa", "prioridade": "Prioridade",
    "quantidade": "Quantidade", "retorno_intervalo": "Retorno do intervalo", "rg": "RG",
    "saida": "Saída", "saida_intervalo": "Saída para intervalo", "setor": "Setor",
    "telefone": "Telefone", "tipo": "Tipo", "titulo": "Título", "unidade": "Unidade",
    "versao": "Versão", "modulo": "Módulo", "acao": "Ação", "nivel": "Nível",
    "entidade": "Entidade", "entidade_id": "Registro relacionado",
    "data_criacao": "Data de criação", "ultimo_login": "Último acesso",
}

HIDDEN_LIST_FIELDS = {
    "id", "created_at", "updated_at", "senha_hash", "token_hash", "token_sessao_hash",
    "dados_anteriores", "dados_novos", "user_agent", "ip_origem",
}

STATUS_LABELS = {
    "ativo": "Ativo", "inativo": "Inativo", "planejada": "Planejada",
    "em_andamento": "Em andamento", "concluida": "Concluída", "concluido": "Concluído",
    "cancelado": "Cancelado", "cancelada": "Cancelada", "em_aberto": "Em aberto",
    "pago": "Pago", "recebido": "Recebido", "pendente": "Pendente",
    "aprovado": "Aprovado", "aprovada": "Aprovada", "aberto": "Aberto",
    "aberta": "Aberta", "fechado": "Fechado", "vigente": "Vigente",
    "disponivel": "Disponível", "em_uso": "Em uso", "agendada": "Agendada",
    "realizada": "Realizada", "em_elaboracao": "Em elaboração", "em_revisao": "Em revisão",
    "planejado": "Planejado", "faturada": "Faturada", "recebida": "Recebida",
    "resolvido": "Resolvido", "em_atendimento": "Em atendimento", "recusada": "Recusada",
    "emitida": "Emitida", "conciliada": "Conciliada", "em_manutencao": "Em manutenção",
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
    "usuario_id": (Usuario, "username"),
    "categoria_financeira_id": (CategoriaFinanceira, "nome"),
    "categoria_pai_id": (CategoriaFinanceira, "nome"),
    "centro_custo_id": (CentroCusto, "nome"),
    "conta_bancaria_id": (ContaBancaria, "numero_conta"),
    "fatura_id": (Fatura, "numero_documento"),
    "orcamento_base_id": (OrcamentoBase, "descricao"),
    "conta_pagar_id": (ContaPagar, "descricao"),
    "conta_receber_id": (ContaReceber, "descricao"),
    "frota_id": (Frota, "identificacao"),
    "cotacao_id": (Cotacao, "descricao"),
}


PAGES: dict[str, dict[str, Any]] = {
    "Dashboard": {"description": "Indicadores operacionais e financeiros em tempo real."},
    "Area Financeira": {"description": "Faturamento, custos, rentabilidade, caixa e projeções em uma única área."},
    "Gestao Usuarios": {"description": "Crie usuários internos vinculados a funcionários e perfis."},
    "Gestao Perfis": {"description": "Administre perfis e permissões de acesso."},
    "Auditoria": {"description": "Consulte os últimos eventos críticos registrados no sistema."},
    "Funcionarios": {"model": Funcionario, "service": FuncionarioService(), "create": FuncionarioCreate, "update": FuncionarioUpdate, "description": "Cadastro interno de colaboradores da UrbanPrime."},
    "Clientes": {"model": Cliente, "service": ClienteService(), "create": ClienteCreate, "update": ClienteUpdate, "description": "Cadastro comercial de clientes. Clientes não acessam o sistema."},
    "Contratos": {"model": Contrato, "service": ContratoService(), "create": ContratoCreate, "update": ContratoUpdate, "description": "Contratos vinculados a clientes, sem vínculo direto com a obra."},
    "Agenda Visitas": {"model": AgendaVisita, "service": AgendaVisitaService(), "create": AgendaVisitaCreate, "update": AgendaVisitaUpdate, "description": "Agenda comercial e técnica relacionada a clientes."},
    "Projetos": {"model": Projeto, "service": ProjetoService(), "create": ProjetoCreate, "update": ProjetoUpdate, "description": "Projetos nascidos a partir de contratos."},
    "Revisoes Projeto": {"model": RevisaoProjeto, "service": RevisaoProjetoService(), "create": RevisaoProjetoCreate, "update": RevisaoProjetoUpdate, "description": "Controle de revisões técnicas dos projetos."},
    "Obras": {"model": Obra, "service": ObraService(), "create": ObraCreate, "update": ObraUpdate, "description": "Obras vinculadas a contrato e projeto. O orçamento oficial fica em Orçamentos-base."},
    "Diarios Obra": {"model": DiarioObra, "service": DiarioObraService(), "create": DiarioObraCreate, "update": DiarioObraUpdate, "description": "Registros diários de atividades, clima e ocorrências da obra."},
    "Medicoes": {"model": Medicao, "service": MedicaoService(), "create": MedicaoCreate, "update": MedicaoUpdate, "description": "Medições por obra e competência."},
    "Chamados Tecnicos": {"model": ChamadoTecnico, "service": ChamadoTecnicoService(), "create": ChamadoTecnicoCreate, "update": ChamadoTecnicoUpdate, "description": "Chamados técnicos relacionados às obras."},
    "Orcamentos Base": {"model": OrcamentoBase, "service": OrcamentoBaseService(), "create": OrcamentoBaseCreate, "update": OrcamentoBaseUpdate, "description": "Fonte oficial do orçamento aprovado da obra."},
    "Itens Orcamento": {"model": ItemOrcamento, "service": GestaoFinanceiraService(ItemOrcamento), "create": ItemOrcamentoCreate, "update": ItemOrcamentoUpdate, "description": "Detalhamento do orçamento previsto por etapa, categoria e item."},
    "Categorias Financeiras": {"model": CategoriaFinanceira, "service": GestaoFinanceiraService(CategoriaFinanceira), "create": CategoriaFinanceiraCreate, "update": CategoriaFinanceiraUpdate, "description": "Plano gerencial de receitas e despesas utilizado nas análises financeiras."},
    "Centros Custo": {"model": CentroCusto, "service": GestaoFinanceiraService(CentroCusto), "create": CentroCustoCreate, "update": CentroCustoUpdate, "description": "Centros de responsabilidade para separar custos de obras, frota e administração."},
    "Contas Bancarias": {"model": ContaBancaria, "service": GestaoFinanceiraService(ContaBancaria), "create": ContaBancariaCreate, "update": ContaBancariaUpdate, "description": "Contas utilizadas no controle de caixa e conciliação."},
    "Faturas": {"model": Fatura, "service": GestaoFinanceiraService(Fatura), "create": FaturaCreate, "update": FaturaUpdate, "description": "Documentos de faturamento vinculados a clientes, contratos, obras e medições."},
    "Movimentacoes Caixa": {"model": MovimentacaoCaixa, "service": GestaoFinanceiraService(MovimentacaoCaixa), "create": MovimentacaoCaixaCreate, "update": MovimentacaoCaixaUpdate, "description": "Entradas e saídas efetivamente realizadas nas contas bancárias."},
    "Apropriacoes Custo": {"model": ApropriacaoCusto, "service": GestaoFinanceiraService(ApropriacaoCusto), "create": ApropriacaoCustoCreate, "update": ApropriacaoCustoUpdate, "description": "Custos realizados atribuídos a obras e centros de custo."},
    "Metas Indicadores": {"model": MetaIndicador, "service": GestaoFinanceiraService(MetaIndicador), "create": MetaIndicadorCreate, "update": MetaIndicadorUpdate, "description": "Metas mensais utilizadas para comparar planejado e realizado."},
    "Contas Pagar": {"model": ContaPagar, "service": ContaPagarService(), "create": ContaPagarCreate, "update": ContaPagarUpdate, "description": "Contas a pagar, incluindo vínculo com ordem de compra."},
    "Contas Receber": {"model": ContaReceber, "service": ContaReceberService(), "create": ContaReceberCreate, "update": ContaReceberUpdate, "description": "Contas a receber vinculadas a clientes, contratos ou medições."},
    "Insumos": {"model": Insumo, "service": InsumoService(), "create": InsumoCreate, "update": InsumoUpdate, "description": "Cadastro de insumos e controle de estoque mínimo."},
    "Movimentacoes Estoque": {"model": MovimentacaoEstoque, "service": MovimentacaoEstoqueService(), "create": MovimentacaoEstoqueCreate, "update": MovimentacaoEstoqueUpdate, "description": "Entradas e saídas de insumos por obra."},
    "Fornecedores": {"model": Fornecedor, "service": FornecedorService(), "create": FornecedorCreate, "update": FornecedorUpdate, "description": "Cadastro de fornecedores. Fornecedores não acessam o sistema."},
    "Cotacoes": {"model": Cotacao, "service": CotacaoService(), "create": CotacaoCreate, "update": CotacaoUpdate, "description": "Cotações de compras por fornecedor e obra."},
    "Ordens Compra": {"model": OrdemCompra, "service": OrdemCompraService(), "create": OrdemCompraCreate, "update": OrdemCompraUpdate, "description": "Ordens de compra que podem alimentar contas a pagar."},
    "Itens Ordem Compra": {"model": ItemOrdemCompra, "service": ItemOrdemCompraService(), "create": ItemOrdemCompraCreate, "update": ItemOrdemCompraUpdate, "description": "Itens detalhados das ordens de compra."},
    "Frotas": {"model": Frota, "service": FrotaService(), "create": FrotaCreate, "update": FrotaUpdate, "description": "Controle de frota e alocação em obras."},
    "Manutencoes Frota": {"model": ManutencaoFrota, "service": GestaoFinanceiraService(ManutencaoFrota), "create": ManutencaoFrotaCreate, "update": ManutencaoFrotaUpdate, "description": "Custos, prazos e ocorrências de manutenção da frota."},
    "Abastecimentos Frota": {"model": AbastecimentoFrota, "service": GestaoFinanceiraService(AbastecimentoFrota), "create": AbastecimentoFrotaCreate, "update": AbastecimentoFrotaUpdate, "description": "Consumo e custo de combustível por equipamento e obra."},
    "Utilizacoes Frota": {"model": UtilizacaoFrota, "service": GestaoFinanceiraService(UtilizacaoFrota), "create": UtilizacaoFrotaCreate, "update": UtilizacaoFrotaUpdate, "description": "Horas utilizadas e custo operacional da frota."},
    "Cronogramas": {"model": Cronograma, "service": CronogramaService(), "create": CronogramaCreate, "update": CronogramaUpdate, "description": "Planejamento de atividades por obra."},
    "Registro Ponto": {"model": RegistroPonto, "service": RegistroPontoService(), "create": RegistroPontoCreate, "update": RegistroPontoUpdate, "description": "Registro da jornada dos funcionários."},
    "Folha Pagamento": {"model": FolhaPagamento, "service": FolhaPagamentoService(), "create": FolhaPagamentoCreate, "update": FolhaPagamentoUpdate, "description": "Folha de pagamento por competência."},
    "Alocacoes Equipe": {"model": AlocacaoFuncionarioObra, "service": GestaoFinanceiraService(AlocacaoFuncionarioObra), "create": AlocacaoFuncionarioObraCreate, "update": AlocacaoFuncionarioObraUpdate, "description": "Alocação de funcionários, funções e custos de mão de obra por obra."},
}

NAVIGATION_MODULES: dict[str, tuple[str, ...]] = {
    "Dashboard": ("Dashboard",),
    "Administrativo e Seguranca": (
        "Gestao Usuarios",
        "Gestao Perfis",
        "Auditoria",
    ),
    "Comercial": (
        "Clientes",
        "Contratos",
        "Agenda Visitas",
    ),
    "Engenharia e Projetos": (
        "Projetos",
        "Revisoes Projeto",
    ),
    "Gestao de Obras": (
        "Obras",
        "Cronogramas",
        "Diarios Obra",
        "Medicoes",
        "Chamados Tecnicos",
        "Orcamentos Base",
        "Itens Orcamento",
    ),
    "Financeiro": (
        "Area Financeira",
        "Categorias Financeiras",
        "Centros Custo",
        "Contas Bancarias",
        "Faturas",
        "Movimentacoes Caixa",
        "Apropriacoes Custo",
        "Metas Indicadores",
        "Contas Pagar",
        "Contas Receber",
    ),
    "Compras e Estoque": (
        "Fornecedores",
        "Cotacoes",
        "Ordens Compra",
        "Itens Ordem Compra",
        "Insumos",
        "Movimentacoes Estoque",
    ),
    "Frota e Equipamentos": (
        "Frotas",
        "Manutencoes Frota",
        "Abastecimentos Frota",
        "Utilizacoes Frota",
    ),
    "Recursos Humanos": (
        "Funcionarios",
        "Registro Ponto",
        "Folha Pagamento",
        "Alocacoes Equipe",
    ),
}

VALUE_LABELS = {
    "juridica": "Pessoa jurídica", "fisica": "Pessoa física",
    "entrada": "Entrada", "saida": "Saída", "receita": "Receita", "despesa": "Despesa",
    "direto": "Direto", "indireto": "Indireto", "conta_pagar": "Conta a pagar",
    "manual": "Lançamento manual", "folha": "Folha de pagamento", "frota": "Frota",
    "obra": "Obra", "estoque": "Estoque", "administrativo": "Administrativo",
    "corrente": "Conta corrente", "poupanca": "Poupança", "caixa": "Caixa",
    "investimento": "Investimento", "transferencia": "Transferência", "pix": "PIX",
    "boleto": "Boleto bancário", "dinheiro": "Dinheiro", "cartao": "Cartão",
    "numero": "Número", "percentual": "Percentual", "reais": "Reais (R$)",
    "ensolarado": "Ensolarado", "nublado": "Nublado", "chuvoso": "Chuvoso",
    "residencial": "Residencial", "comercial": "Comercial", "industrial": "Industrial",
    "hospitalar": "Hospitalar", "hoteleiro": "Hoteleiro", "educacional": "Educacional",
    "preventiva": "Preventiva", "corretiva": "Corretiva", "preditiva": "Preditiva",
    "auth": "Autenticação", "usuarios": "Usuários", "perfis": "Perfis e permissões",
    "engenharia": "Engenharia", "financeiro": "Financeiro", "compras": "Compras",
    "obras": "Obras", "planejamento": "Planejamento", "rh": "Recursos Humanos",
    "auditoria": "Auditoria", "visualizar": "Visualizar", "criar": "Criar",
    "editar": "Editar", "excluir": "Excluir", "aprovar": "Aprovar", "cancelar": "Cancelar",
    "login": "Acesso ao sistema", "logout": "Saída do sistema",
    "login_falhou": "Tentativa de acesso sem sucesso",
    "vincular_permissao": "Vincular permissão", "info": "Informação",
    "warning": "Atenção", "cadastro": "Cadastro",
}

TRANSLATED_VALUE_FIELDS = {
    "tipo", "tipo_pessoa", "tipo_projeto", "tipo_conta", "tipo_custo", "origem",
    "forma_pagamento", "unidade", "clima", "modulo", "acao", "nivel", "entidade",
}

MONEY_FIELDS = {
    "valor", "valor_total", "valor_unitario", "valor_medido", "valor_bruto",
    "valor_liquido", "valor_aquisicao", "saldo_inicial", "salario_base", "salario_bruto",
    "salario_liquido", "impostos", "retencoes", "descontos", "custo", "custo_hora",
}

MODEL_FIELD_CHOICES = {
    ("clientes", "tipo_pessoa"): ("juridica", "fisica"),
    ("projetos", "tipo_projeto"): ("residencial", "comercial", "industrial", "hospitalar", "hoteleiro", "educacional"),
    ("diarios_obra", "clima"): ("ensolarado", "nublado", "chuvoso"),
    ("movimentacoes_estoque", "tipo"): ("entrada", "saida"),
    ("categorias_financeiras", "tipo"): ("receita", "despesa"),
    ("centros_custo", "tipo"): ("obra", "frota", "estoque", "administrativo"),
    ("contas_bancarias", "tipo_conta"): ("corrente", "poupanca", "caixa", "investimento"),
    ("movimentacoes_caixa", "tipo"): ("entrada", "saida"),
    ("movimentacoes_caixa", "forma_pagamento"): ("pix", "transferencia", "boleto", "dinheiro", "cartao"),
    ("apropriacoes_custo", "tipo_custo"): ("direto", "indireto"),
    ("apropriacoes_custo", "origem"): ("manual", "conta_pagar", "folha", "frota", "estoque"),
    ("metas_indicadores", "unidade"): ("numero", "percentual", "reais"),
    ("manutencoes_frota", "tipo"): ("preventiva", "corretiva", "preditiva"),
}

MODULE_ICONS = {
    "Dashboard": "📊",
    "Administrativo e Seguranca": "🔐",
    "Comercial": "🤝",
    "Engenharia e Projetos": "📐",
    "Gestao de Obras": "🏗️",
    "Financeiro": "💰",
    "Compras e Estoque": "📦",
    "Frota e Equipamentos": "🚜",
    "Recursos Humanos": "👥",
}

MODULE_TITLES = {
    "Administrativo e Seguranca": "Administrativo e Segurança",
    "Gestao de Obras": "Gestão de Obras",
}


PAGE_TITLES = {
    "Area Financeira": "Área financeira",
    "Gestao Usuarios": "Gestão de usuários", "Gestao Perfis": "Gestão de perfis",
    "Funcionarios": "Funcionários", "Agenda Visitas": "Agenda de visitas",
    "Revisoes Projeto": "Revisões de projeto", "Diarios Obra": "Diários de obra",
    "Medicoes": "Medições", "Chamados Tecnicos": "Chamados técnicos",
    "Orcamentos Base": "Orçamentos-base", "Contas Pagar": "Contas a pagar",
    "Contas Receber": "Contas a receber", "Movimentacoes Estoque": "Movimentações de estoque",
    "Cotacoes": "Cotações", "Ordens Compra": "Ordens de compra",
    "Itens Ordem Compra": "Itens das ordens de compra", "Registro Ponto": "Registro de ponto",
    "Folha Pagamento": "Folha de pagamento",
    "Itens Orcamento": "Itens do orçamento", "Centros Custo": "Centros de custo",
    "Contas Bancarias": "Contas bancárias", "Movimentacoes Caixa": "Movimentações de caixa",
    "Apropriacoes Custo": "Custos por obra", "Metas Indicadores": "Metas e indicadores",
    "Manutencoes Frota": "Manutenções da frota", "Abastecimentos Frota": "Abastecimentos da frota",
    "Utilizacoes Frota": "Utilização da frota", "Alocacoes Equipe": "Alocação das equipes",
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


def page_title(page_name: str) -> str:
    return PAGE_TITLES.get(page_name, page_name)


def module_title(module_name: str) -> str:
    return MODULE_TITLES.get(module_name, module_name)


def validate_navigation_structure() -> None:
    grouped_pages = [
        page_name
        for module_pages in NAVIGATION_MODULES.values()
        for page_name in module_pages
    ]
    duplicated_pages = {
        page_name for page_name in grouped_pages if grouped_pages.count(page_name) > 1
    }
    missing_pages = set(PAGES) - set(grouped_pages)
    unknown_pages = set(grouped_pages) - set(PAGES)
    if duplicated_pages or missing_pages or unknown_pages:
        raise RuntimeError(
            "Navegação inconsistente. "
            f"Duplicadas: {sorted(duplicated_pages)}; "
            f"ausentes: {sorted(missing_pages)}; "
            f"desconhecidas: {sorted(unknown_pages)}"
        )


validate_navigation_structure()


def human_value(field: str, value: Any) -> Any:
    if value is None:
        return "—"
    if field == "status":
        return STATUS_LABELS.get(str(value), str(value).replace("_", " ").title())
    if isinstance(value, str):
        if field == "competencia":
            return format_competence_br(value)
        if field == "cpf":
            return format_cpf(value)
        if field == "cnpj":
            return format_cnpj(value)
        if field == "cpf_cnpj":
            return format_cpf_cnpj(value)
        if field == "cep":
            return format_cep(value)
        if field == "telefone":
            return format_phone_br(value)
        if field in TRANSLATED_VALUE_FIELDS:
            return VALUE_LABELS.get(value, value.replace("_", " ").capitalize())
    if isinstance(value, datetime):
        return format_datetime_br(value, APP_SETTINGS.app_timezone)
    if isinstance(value, date):
        return format_date_br(value)
    if isinstance(value, time):
        return value.strftime("%H:%M")
    if isinstance(value, Decimal):
        if field in MONEY_FIELDS:
            return format_currency_br(value)
        if "percentual" in field:
            return f"{format_number_br(value, 2)}%"
        decimal_places = 3 if field in {"quantidade", "litros", "horas_utilizadas"} else 2
        return format_number_br(value, decimal_places)
    if isinstance(value, bool):
        return "Sim" if value else "Não"
    return value


def fk_label_maps(db: Session, model: Any) -> dict[str, dict[int, str]]:
    result: dict[str, dict[int, str]] = {}
    for field in model_columns(model):
        if field not in FK_CONFIG:
            continue
        related_model, label_field = FK_CONFIG[field]
        result[field] = {
            row.id: str(getattr(row, label_field, None) or getattr(row, "nome", None) or row.id)
            for row in db.query(related_model).order_by(related_model.id).all()
        }
    return result


def friendly_rows(db: Session, rows: list[Any]) -> list[dict[str, Any]]:
    if not rows:
        return []
    model = type(rows[0])
    related = fk_label_maps(db, model)
    result = []
    for row in rows:
        item: dict[str, Any] = {}
        for field in model_columns(model):
            if field in HIDDEN_LIST_FIELDS:
                continue
            value = getattr(row, field)
            if field in related:
                value = related[field].get(value, "—")
            item[label_for(field)] = human_value(field, value)
        result.append(item)
    return result


def record_label(row: Any) -> str:
    for field in ("nome", "razao_social", "numero_contrato", "numero", "identificacao", "titulo", "descricao", "competencia", "email"):
        value = getattr(row, field, None)
        if value:
            return str(value)
    return f"Registro {row.id}"


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
        return st.selectbox(
            label,
            options,
            index=options.index(current),
            format_func=lambda value: STATUS_LABELS.get(value, value.replace("_", " ").title()),
            key=key,
        )
    choice_values = MODEL_FIELD_CHOICES.get((model.__tablename__, field))
    if field == "estado":
        choice_values = BRAZIL_STATES
        default = default or APP_SETTINGS.default_state
    if choice_values:
        options = list(choice_values)
        configured_default = column.default.arg if column.default is not None and isinstance(column.default.arg, str) else None
        current = default or configured_default
        if current and current not in options:
            options.insert(0, current)
        if not required and current is None:
            options.insert(0, None)
        index = options.index(current) if current in options else 0
        return st.selectbox(
            label,
            options,
            index=index,
            format_func=lambda value: "Não informado" if value is None else VALUE_LABELS.get(value, value),
            key=key,
        )
    python_type = getattr(column.type, "python_type", str)
    if python_type is bool:
        return st.checkbox(label, value=bool(default), key=key)
    if python_type is int:
        return st.number_input(label, min_value=0, step=1, value=int(default or 0), key=key)
    if python_type is Decimal:
        value = float(default or 0)
        return Decimal(str(st.number_input(label, min_value=0.0, step=0.01, value=value, key=key)))
    if python_type is datetime:
        current = default if isinstance(default, datetime) else now_local_naive(APP_SETTINGS.app_timezone)
        date_column, time_column = st.columns(2)
        selected_date = date_column.date_input(f"{label} — data", value=current.date(), key=f"{key}_date")
        selected_time = time_column.time_input(f"{label} — hora", value=current.time().replace(microsecond=0), key=f"{key}_time")
        return datetime.combine(selected_date, selected_time)
    if python_type is date:
        value = default if isinstance(default, date) else today_in_timezone(APP_SETTINGS.app_timezone)
        return st.date_input(label, value=value, key=key)
    if python_type is time:
        value = default if isinstance(default, time) else time(8, 0)
        return st.time_input(label, value=value, key=key)
    if "descricao" in field or "observa" in field or field in {"endereco", "atividades", "ocorrencias", "motivo"}:
        value = "" if default is None else str(default)
        text_value = st.text_area(label, value=value, key=key)
    else:
        if field == "cidade" and default is None:
            default = APP_SETTINGS.default_city
        value = "" if default is None else str(default)
        text_value = st.text_input(label, value=value, key=key)
    if not text_value and not required:
        return None
    return normalize_brazilian_field(field, text_value)


def safe_count(db: Session, sql: str) -> int:
    try:
        return int(db.execute(text(sql)).scalar() or 0)
    except SQLAlchemyError:
        return 0


def login_screen() -> None:
    left, center, right = st.columns([1, 1.15, 1])
    with center:
        st.title("🏗️ UrbanPrime ERP")
        st.caption("Gestão integrada de obras, projetos e operações.")
        with st.form("login_form"):
            username = st.text_input("Usuário", placeholder="Digite seu usuário")
            password = st.text_input("Senha", type="password", placeholder="Digite sua senha")
            submitted = st.form_submit_button("Entrar no sistema", use_container_width=True)
    if submitted:
        db = get_db()
        try:
            user, access_token, refresh_token = AuthService().authenticate(
                db,
                username,
                password,
                origem="streamlit",
            )
            st.session_state["authenticated"] = True
            st.session_state["user_id"] = user.id
            st.session_state["username"] = user.username
            st.session_state["access_token"] = access_token
            st.session_state["refresh_token"] = refresh_token
            st.success("Login realizado com sucesso.")
            st.rerun()
        except Exception as exc:
            st.error(f"Não foi possível entrar: {exc}")
        finally:
            db.close()


def sidebar_menu() -> str:
    st.sidebar.title("🏗️ UrbanPrime ERP")
    st.sidebar.caption(f"Acesso como **{st.session_state.get('username', '')}**")
    local_now = now_in_timezone(APP_SETTINGS.app_timezone)
    st.sidebar.caption(f"Horário de Brasília: {format_datetime_br(local_now, APP_SETTINGS.app_timezone)}")
    st.sidebar.markdown("---")
    selected_module = st.sidebar.radio(
        "Módulos principais",
        list(NAVIGATION_MODULES),
        format_func=lambda module_name: (
            f"{MODULE_ICONS[module_name]} {module_title(module_name)}"
        ),
        help="Escolha a área responsável pela operação.",
        key="main_module",
    )
    module_pages = NAVIGATION_MODULES[selected_module]
    if selected_module == "Dashboard":
        selected = "Dashboard"
    else:
        selected = st.sidebar.selectbox(
            "Funcionalidade",
            module_pages,
            format_func=page_title,
            help="Escolha o recurso que deseja consultar ou atualizar.",
            key=f"module_page_{selected_module}",
        )
        st.sidebar.caption(PAGES[selected]["description"])
    st.sidebar.caption(
        "Use a pesquisa da funcionalidade para localizar registros por nome ou descrição."
    )
    st.sidebar.markdown("---")
    if st.sidebar.button("Sair do sistema", use_container_width=True):
        db = get_db()
        try:
            log_action(
                db,
                usuario_id=st.session_state.get("user_id"),
                modulo="auth",
                acao="logout",
                entidade="usuarios",
                entidade_id=st.session_state.get("user_id"),
                descricao="Saída do sistema pelo Streamlit",
                dados_novos={"origem": "streamlit"},
            )
        except Exception:
            db.rollback()
        finally:
            db.close()
        st.session_state.clear()
        st.rerun()
    return selected


def require_login() -> bool:
    if not st.session_state.get("authenticated"):
        login_screen()
        return False
    return True


def render_dashboard() -> None:
    db = get_db()
    try:
        selected_dashboard = render_dashboard_hub(db)
        if selected_dashboard == "Executivo":
            st.subheader("Atividades recentes")
            logs = (
                db.query(LogAuditoria)
                .order_by(LogAuditoria.created_at.desc(), LogAuditoria.id.desc())
                .limit(20)
                .all()
            )
            if logs:
                st.dataframe(friendly_rows(db, logs), width="stretch", hide_index=True)
            else:
                st.info("Nenhum registro encontrado.")
    except Exception as exc:
        st.error(f"Erro ao carregar dashboard: {exc}")
    finally:
        db.close()


def render_listing(db: Session, cfg: dict[str, Any], rows: list[Any]) -> None:
    st.subheader("Consulte antes de abrir a lista")
    st.caption("Pesquise por nome, descrição, número, cidade, responsável ou qualquer informação visível.")
    search = st.text_input(
        "O que você procura?",
        placeholder="Ex.: residência em Heliópolis, galpão, Ana Paula...",
        key=f"search_{cfg['model'].__tablename__}",
    ).strip().casefold()
    statuses = sorted({str(getattr(row, "status")) for row in rows if getattr(row, "status", None)})
    selected_status = "Todos"
    if statuses:
        selected_status = st.selectbox(
            "Situação",
            ["Todos", *statuses],
            format_func=lambda value: "Todas as situações" if value == "Todos" else STATUS_LABELS.get(value, value.replace("_", " ").title()),
            key=f"status_{cfg['model'].__tablename__}",
        )
    display_rows = friendly_rows(db, rows)
    filtered = []
    for row, display in zip(rows, display_rows):
        if selected_status != "Todos" and str(getattr(row, "status", "")) != selected_status:
            continue
        haystack = " ".join(str(value) for value in display.values()).casefold()
        if search and search not in haystack:
            continue
        filtered.append(display)
    st.caption(f"{len(filtered)} registro(s) encontrado(s) de {len(rows)} no total.")
    if filtered:
        st.dataframe(filtered, width="stretch", hide_index=True)
    else:
        st.info("Nenhum registro corresponde à pesquisa. Tente outra palavra ou limpe os filtros.")


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
            set_audit_context(
                db,
                usuario_id=st.session_state.get("user_id"),
                modulo=page_title(page_name),
                origem="streamlit",
            )
            item = cfg["service"].create(db, create_schema(**cleaned))
            st.success(f"Registro salvo com ID {item.id}.")
            st.rerun()
        except Exception as exc:
            db.rollback()
            st.error(f"Erro ao salvar: {exc}")


def render_edit_form(db: Session, cfg: dict[str, Any], page_name: str, rows: list[Any]) -> None:
    model = cfg["model"]
    update_schema = cfg["update"]
    st.subheader("Escolha pelo nome ou pela descrição")
    if not rows:
        st.info("Ainda não há registros disponíveis para edição.")
        return
    selected_id = st.selectbox(
        "Registro",
        [row.id for row in rows],
        format_func=lambda item_id: next((record_label(row) for row in rows if row.id == item_id), str(item_id)),
        key=f"edit_select_{page_name}",
    )
    item = next(row for row in rows if row.id == selected_id)
    st.caption(f"Editando: {record_label(item)}")
    with st.form(f"edit_{page_name}_{item.id}"):
        payload: dict[str, Any] = {}
        for field in editable_columns(model):
            payload[field] = value_input(db, model, field, getattr(item, field), key=f"edit_{page_name}_{item.id}_{field}")
        submitted = st.form_submit_button("Salvar alterações")
    if submitted:
        try:
            cleaned = {key: value for key, value in payload.items() if value is not None}
            set_audit_context(
                db,
                usuario_id=st.session_state.get("user_id"),
                modulo=page_title(page_name),
                origem="streamlit",
            )
            cfg["service"].update(db, item.id, update_schema(**cleaned))
            st.success("Registro atualizado com sucesso.")
            st.rerun()
        except Exception as exc:
            db.rollback()
            st.error(f"Erro ao atualizar: {exc}")


def render_crud_page(page_name: str, cfg: dict[str, Any]) -> None:
    st.title(page_title(page_name))
    st.write(cfg["description"])
    if st.button("Atualizar dados", key=f"reload_{page_name}"):
        st.rerun()
    db = get_db()
    try:
        rows = cfg["service"].list(db, skip=0, limit=500)
        consult_tab, create_tab, edit_tab = st.tabs(["🔎 Consultar", "➕ Cadastrar", "✏️ Editar"])
        with consult_tab:
            render_listing(db, cfg, rows)
        with create_tab:
            render_create_form(db, cfg, page_name)
        with edit_tab:
            render_edit_form(db, cfg, page_name, rows)
    except Exception as exc:
        st.error(f"Erro ao carregar página: {exc}")
    finally:
        db.close()


def render_users() -> None:
    st.title("Gestão de usuários")
    st.write(PAGES["Gestao Usuarios"]["description"])
    db = get_db()
    try:
        if st.button("Atualizar / Recarregar", key="reload_users"):
            st.rerun()
        rows = (
            db.query(Usuario)
            .order_by(
                Usuario.updated_at.desc(),
                Usuario.ultimo_login.desc().nullslast(),
                Usuario.created_at.desc(),
                Usuario.id.desc(),
            )
            .limit(500)
            .all()
        )
        if rows:
            search = st.text_input("Pesquisar usuário", placeholder="Digite o nome de usuário ou e-mail")
            display = friendly_rows(db, rows)
            if search:
                display = [item for item in display if search.casefold() in " ".join(map(str, item.values())).casefold()]
            st.dataframe(display, width="stretch", hide_index=True)
        else:
            st.info("Nenhum registro encontrado.")
        with st.form("create_user"):
            st.subheader("Cadastrar usuário interno")
            funcionario_id = fk_input(db, "funcionario_id", True, key="user_funcionario")
            username = st.text_input("Usuário")
            email = st.text_input("E-mail")
            password = st.text_input("Senha inicial", type="password")
            perfil_options = db.query(Perfil).filter(Perfil.ativo.is_(True)).order_by(Perfil.nome).all()
            perfil_id = st.selectbox("Perfil", [p.id for p in perfil_options], format_func=lambda pid: next((p.nome for p in perfil_options if p.id == pid), str(pid))) if perfil_options else None
            ativo = st.checkbox("Ativo", value=True)
            submitted = st.form_submit_button("Salvar")
        if submitted:
            if not funcionario_id or not username or not email or not password:
                st.error("Preencha funcionário, usuário, e-mail e senha.")
            else:
                user = Usuario(funcionario_id=funcionario_id, username=username, email=email, senha_hash=hash_password(password), ativo=ativo, bloqueado=False)
                db.add(user)
                db.flush()
                if perfil_id:
                    db.add(UsuarioPerfil(usuario_id=user.id, perfil_id=perfil_id))
                new_data = model_snapshot(user)
                new_data["perfil_id"] = perfil_id
                add_audit_log(
                    db,
                    usuario_id=st.session_state.get("user_id"),
                    modulo="Gestão de usuários",
                    acao="criar",
                    entidade="usuarios",
                    entidade_id=user.id,
                    descricao=f"Usuário {username} criado",
                    dados_novos=new_data,
                )
                db.commit()
                db.refresh(user)
                st.success(f"Usuário criado com ID {user.id}.")
                st.rerun()
        st.subheader("Editar situação do usuário")
        edit_id = st.number_input("ID do usuário", min_value=1, step=1, key="user_edit_id")
        user = db.get(Usuario, int(edit_id))
        if user:
            ativo = st.checkbox("Ativo", value=user.ativo, key="user_edit_ativo")
            bloqueado = st.checkbox("Bloqueado", value=user.bloqueado, key="user_edit_bloqueado")
            if st.button("Salvar situação do usuário"):
                before = model_snapshot(user)
                user.ativo = ativo
                user.bloqueado = bloqueado
                db.flush()
                add_audit_log(
                    db,
                    usuario_id=st.session_state.get("user_id"),
                    modulo="Gestão de usuários",
                    acao="editar",
                    entidade="usuarios",
                    entidade_id=user.id,
                    descricao=f"Situação do usuário {user.username} alterada",
                    dados_anteriores=before,
                    dados_novos=model_snapshot(user),
                )
                db.commit()
                st.success("Usuário atualizado.")
                st.rerun()
        else:
            st.warning("Informe um ID existente para editar.")
    except Exception as exc:
        db.rollback()
        st.error(f"Erro em usuários: {exc}")
    finally:
        db.close()


def render_profiles() -> None:
    st.title("Gestão de perfis")
    st.write(PAGES["Gestao Perfis"]["description"])
    db = get_db()
    try:
        if st.button("Atualizar / Recarregar", key="reload_profiles"):
            st.rerun()
        profiles = (
            db.query(Perfil)
            .order_by(Perfil.updated_at.desc(), Perfil.created_at.desc(), Perfil.id.desc())
            .all()
        )
        if profiles:
            st.dataframe(friendly_rows(db, profiles), width="stretch", hide_index=True)
        else:
            st.info("Nenhum registro encontrado.")
        with st.form("create_profile"):
            st.subheader("Cadastrar perfil")
            nome = st.text_input("Nome")
            descricao = st.text_area("Descrição")
            nivel = st.number_input("Nível de acesso", min_value=1, max_value=100, value=10, step=1)
            ativo = st.checkbox("Ativo", value=True)
            submitted = st.form_submit_button("Salvar")
        if submitted:
            profile = Perfil(nome=nome, descricao=descricao, nivel_acesso=nivel, ativo=ativo)
            db.add(profile)
            db.flush()
            add_audit_log(
                db,
                usuario_id=st.session_state.get("user_id"),
                modulo="Gestão de perfis",
                acao="criar",
                entidade="perfis",
                entidade_id=profile.id,
                descricao=f"Perfil {nome} criado",
                dados_novos=model_snapshot(profile),
            )
            db.commit()
            st.success("Perfil criado com sucesso.")
            st.rerun()
        st.subheader("Permissões")
        permissions = (
            db.query(Permissao)
            .order_by(
                Permissao.updated_at.desc(),
                Permissao.created_at.desc(),
                Permissao.id.desc(),
            )
            .all()
        )
        if permissions:
            st.dataframe(friendly_rows(db, permissions), width="stretch", hide_index=True)
        else:
            st.info("Nenhum registro encontrado.")
        st.subheader("Vincular permissão a perfil")
        if profiles and permissions:
            perfil_id = st.selectbox("Perfil", [p.id for p in profiles], format_func=lambda pid: next((p.nome for p in profiles if p.id == pid), str(pid)), key="pp_perfil")
            permissao_id = st.selectbox(
                "Permissão",
                [p.id for p in permissions],
                format_func=lambda pid: next(
                    (f"{human_value('modulo', p.modulo)}: {human_value('acao', p.acao)}" for p in permissions if p.id == pid),
                    str(pid),
                ),
                key="pp_perm",
            )
            if st.button("Salvar permissão no perfil"):
                exists = db.query(PerfilPermissao).filter_by(perfil_id=perfil_id, permissao_id=permissao_id).first()
                if exists:
                    st.warning("Permissão já vinculada.")
                else:
                    db.add(PerfilPermissao(perfil_id=perfil_id, permissao_id=permissao_id))
                    add_audit_log(
                        db,
                        usuario_id=st.session_state.get("user_id"),
                        modulo="Gestão de perfis",
                        acao="vincular_permissao",
                        entidade="perfil_permissao",
                        entidade_id=perfil_id,
                        descricao="Permissão vinculada ao perfil",
                        dados_novos={"perfil_id": perfil_id, "permissao_id": permissao_id},
                    )
                    db.commit()
                    st.success("Permissão vinculada.")
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
        logs = (
            db.query(LogAuditoria)
            .order_by(LogAuditoria.created_at.desc(), LogAuditoria.id.desc())
            .limit(500)
            .all()
        )
        if logs:
            search = st.text_input("Pesquisar atividade", placeholder="Digite usuário, módulo, ação ou descrição")
            display = friendly_rows(db, logs)
            if search:
                display = [item for item in display if search.casefold() in " ".join(map(str, item.values())).casefold()]
            st.dataframe(display, width="stretch", hide_index=True)

            access_logs = [log for log in logs if log.acao in {"login", "login_falhou", "logout"}]
            st.subheader("Histórico de acessos")
            if access_logs:
                st.caption("Cada entrada, tentativa sem sucesso e saída permanece registrada em uma linha própria.")
                st.dataframe(friendly_rows(db, access_logs), width="stretch", hide_index=True)
            else:
                st.info("Ainda não há acessos reais registrados.")

            st.subheader("Detalhes da atividade")
            selected_log_id = st.selectbox(
                "Atividade",
                [log.id for log in logs],
                format_func=lambda log_id: next(
                    (
                        f"{format_datetime_br(log.created_at, APP_SETTINGS.app_timezone)} · "
                        f"{human_value('acao', log.acao)} · {log.descricao or log.entidade or 'Atividade'}"
                        for log in logs
                        if log.id == log_id
                    ),
                    str(log_id),
                ),
                key="audit_detail_id",
            )
            selected_log = next(log for log in logs if log.id == selected_log_id)
            selected_user = db.get(Usuario, selected_log.usuario_id) if selected_log.usuario_id else None
            detail_columns = st.columns(3)
            detail_columns[0].metric("Usuário", selected_user.username if selected_user else "Não identificado")
            detail_columns[1].metric("Módulo", human_value("modulo", selected_log.modulo))
            detail_columns[2].metric("Ação", human_value("acao", selected_log.acao))
            before_column, after_column = st.columns(2)
            with before_column:
                st.caption("Dados anteriores")
                if selected_log.dados_anteriores:
                    st.json(selected_log.dados_anteriores)
                else:
                    st.write("—")
            with after_column:
                st.caption("Dados novos")
                if selected_log.dados_novos:
                    st.json(selected_log.dados_novos)
                else:
                    st.write("—")
        else:
            st.info("Nenhum registro encontrado.")
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
    elif page_name == "Area Financeira":
        render_financial_area()
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
