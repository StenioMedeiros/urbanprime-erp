from __future__ import annotations

from datetime import date, timedelta
from typing import Any

import pandas as pd
import streamlit as st
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.core.config.settings import get_settings
from src.shared.utils.brazil_localization import (
    format_currency_br,
    format_number_br,
    today_in_timezone,
)
from src.ui.financial_dashboard import (
    _filter_period,
    load_financial_data,
    render_dashboard_trends,
    render_financial_area,
)
from src.ui.works_dashboard import render_works_dashboard


APP_SETTINGS = get_settings()


DASHBOARD_CATALOG = (
    {
        "name": "Executivo",
        "status": "disponivel",
        "description": "Visão consolidada da construtora para acompanhamento da diretoria.",
        "indicators": (
            "faturamento, recebimentos, gastos e saldo operacional",
            "obras, carteira de contratos, equipe, estoque e frota",
            "tendências e projeções dos principais resultados",
        ),
    },
    {
        "name": "Financeiro e Fluxo de Caixa",
        "status": "disponivel",
        "description": "Faturamento, custos, rentabilidade, obrigações, caixa, metas e projeções.",
        "indicators": (
            "faturamento bruto e líquido, custos, investimentos e margem",
            "contas a pagar e receber, vencimentos e fluxo de caixa",
            "rentabilidade por obra, projeto ou cliente e metas financeiras",
        ),
    },
    {
        "name": "Obras e Engenharia",
        "status": "disponivel",
        "description": "Prazo, avanço físico, medições, orçamento e situação das obras.",
        "indicators": (
            "obras planejadas, em andamento, atrasadas e concluídas",
            "avanço físico, atividades atrasadas e previsão de conclusão",
            "orçamento consumido, medições, chamados e revisões",
        ),
    },
    {
        "name": "Compras e Fornecedores",
        "status": "planejado",
        "description": "Compras, cotações, fornecedores, prazos e economia obtida.",
        "indicators": (
            "compras por período, obra e fornecedor",
            "ordens abertas, aprovadas, recebidas e atrasadas",
            "prazo médio, economia das cotações e concentração de fornecedores",
        ),
    },
    {
        "name": "Estoque",
        "status": "planejado",
        "description": "Valor armazenado, consumo, giro e risco de falta de materiais.",
        "indicators": (
            "valor total e materiais abaixo do estoque mínimo",
            "entradas, saídas e consumo por obra",
            "giro, itens sem movimentação e previsão de falta",
        ),
    },
    {
        "name": "Frota e Maquinário",
        "status": "planejado",
        "description": "Disponibilidade, uso, manutenção e custo dos equipamentos.",
        "indicators": (
            "equipamentos disponíveis, em uso ou em manutenção",
            "custos de combustível, manutenção e utilização",
            "horas trabalhadas, tempo parado e produtividade",
        ),
    },
    {
        "name": "Recursos Humanos",
        "status": "planejado",
        "description": "Quadro de pessoal, folha, jornada e alocação das equipes.",
        "indicators": (
            "funcionários ativos, admissões, desligamentos e crescimento do quadro",
            "folha, horas trabalhadas, faltas e horas extras",
            "custo e produtividade das equipes por obra",
        ),
    },
)


EXECUTIVE_SNAPSHOT_SQL = """
SELECT
    (SELECT COUNT(*) FROM obras WHERE status = 'em_andamento')::numeric AS obras_em_andamento,
    (SELECT COUNT(*) FROM obras WHERE status = 'planejada')::numeric AS obras_planejadas,
    (SELECT COUNT(*) FROM obras WHERE status = 'concluida')::numeric AS obras_concluidas,
    (
        SELECT COALESCE(SUM(GREATEST(
            c.valor_total - COALESCE((
                SELECT SUM(f.valor_liquido)
                FROM faturas f
                WHERE f.contrato_id = c.id AND f.status <> 'cancelada'
            ), 0),
            0
        )), 0)
        FROM contratos c
        WHERE c.status IN ('ativo', 'em_aberto')
    )::numeric AS carteira_a_executar,
    (SELECT COUNT(*) FROM funcionarios WHERE status = 'ativo')::numeric AS funcionarios_ativos,
    (SELECT COALESCE(SUM(quantidade_atual * COALESCE(valor_unitario, 0)), 0) FROM insumos)::numeric AS valor_estoque,
    (SELECT COUNT(*) FROM insumos WHERE quantidade_atual <= estoque_minimo)::numeric AS itens_criticos,
    (SELECT COUNT(*) FROM frotas)::numeric AS frota_total,
    (SELECT COUNT(*) FROM frotas WHERE status = 'disponivel')::numeric AS frota_disponivel,
    (SELECT COUNT(*) FROM frotas WHERE status = 'em_uso')::numeric AS frota_em_uso,
    (SELECT COUNT(*) FROM frotas WHERE status = 'em_manutencao')::numeric AS frota_manutencao,
    (SELECT COUNT(*) FROM obras WHERE status NOT IN ('concluida', 'cancelada') AND data_previsao_fim < CURRENT_DATE)::numeric AS obras_atrasadas,
    (SELECT COUNT(*) FROM contas_pagar WHERE status NOT IN ('pago', 'cancelado') AND data_vencimento < CURRENT_DATE)::numeric AS pagamentos_atrasados,
    (SELECT COUNT(*) FROM contas_receber WHERE status NOT IN ('recebido', 'cancelado') AND data_vencimento < CURRENT_DATE)::numeric AS recebimentos_atrasados
"""


WORKS_DETAIL_SQL = """
SELECT data_inicio AS data, status, nome
FROM obras
WHERE data_inicio IS NOT NULL
ORDER BY data_inicio
"""


EMPLOYEES_DETAIL_SQL = """
SELECT data_admissao, data_demissao, status
FROM funcionarios
WHERE data_admissao IS NOT NULL
"""


def dashboard_names() -> list[str]:
    return [str(item["name"]) for item in DASHBOARD_CATALOG]


def dashboard_is_available(name: str) -> bool:
    return any(item["name"] == name and item["status"] == "disponivel" for item in DASHBOARD_CATALOG)


def _dashboard_label(name: str) -> str:
    status = "Disponível" if dashboard_is_available(name) else "Próxima etapa"
    return f"{name} — {status}"


def executive_period_bounds(period: str, today: date) -> tuple[date, date]:
    if period == "Mês atual":
        return today.replace(day=1), today
    if period == "Últimos 6 meses":
        start = (pd.Timestamp(today).to_period("M").start_time - pd.DateOffset(months=5)).date()
        return start, today
    if period == "Todo o histórico":
        return date(1900, 1, 1), today
    start = (pd.Timestamp(today).to_period("M").start_time - pd.DateOffset(months=11)).date()
    return start, today


def previous_period_bounds(start: date, end: date) -> tuple[date, date]:
    duration = end - start
    previous_end = start - timedelta(days=1)
    return previous_end - duration, previous_end


def executive_previous_period_bounds(period: str, start: date, end: date) -> tuple[date, date]:
    months = {"Mês atual": 1, "Últimos 6 meses": 6, "Últimos 12 meses": 12}.get(period)
    if months is None:
        return previous_period_bounds(start, end)
    return (
        (pd.Timestamp(start) - pd.DateOffset(months=months)).date(),
        (pd.Timestamp(end) - pd.DateOffset(months=months)).date(),
    )


def percent_delta(current: float, previous: float) -> float | None:
    if previous == 0:
        return None if current == 0 else 100.0
    return (current - previous) / abs(previous) * 100


def _delta_label(current: float, previous: float) -> str | None:
    delta = percent_delta(current, previous)
    if delta is None:
        return None
    sign = "+" if delta > 0 else ""
    return f"{sign}{format_number_br(delta, 1)}% vs. período anterior"


def _load_snapshot(db: Session) -> dict[str, float]:
    row = db.execute(text(EXECUTIVE_SNAPSHOT_SQL)).mappings().one()
    return {key: float(value or 0) for key, value in row.items()}


def _load_works(db: Session) -> pd.DataFrame:
    frame = pd.read_sql_query(text(WORKS_DETAIL_SQL), db.connection())
    frame["data"] = pd.to_datetime(frame["data"], errors="coerce")
    return frame


def _load_employees(db: Session) -> pd.DataFrame:
    frame = pd.read_sql_query(text(EMPLOYEES_DETAIL_SQL), db.connection())
    frame["data_admissao"] = pd.to_datetime(frame["data_admissao"], errors="coerce")
    frame["data_demissao"] = pd.to_datetime(frame["data_demissao"], errors="coerce")
    return frame


def _headcount_at(employees: pd.DataFrame, reference_date: date) -> int:
    if employees.empty:
        return 0
    reference = pd.Timestamp(reference_date)
    active = employees["data_admissao"].le(reference) & (
        employees["data_demissao"].isna() | employees["data_demissao"].gt(reference)
    )
    return int(active.sum())


def _sum_operating_expenses(expenses: pd.DataFrame) -> float:
    if expenses.empty:
        return 0.0
    operating = expenses[expenses["natureza"] != "Investimento"]
    return float(operating["valor"].sum())


def _sum_cash(cash: pd.DataFrame, movement_type: str) -> float:
    if cash.empty:
        return 0.0
    return float(cash.loc[cash["tipo"] == movement_type, "valor"].sum())


def _render_executive_kpis(
    expenses: pd.DataFrame,
    revenue: pd.DataFrame,
    cash: pd.DataFrame,
    previous_expenses: pd.DataFrame,
    previous_revenue: pd.DataFrame,
    previous_cash: pd.DataFrame,
) -> None:
    billing = float(revenue["valor_liquido"].sum()) if not revenue.empty else 0.0
    previous_billing = float(previous_revenue["valor_liquido"].sum()) if not previous_revenue.empty else 0.0
    receipts = _sum_cash(cash, "entrada")
    previous_receipts = _sum_cash(previous_cash, "entrada")
    expenses_total = _sum_operating_expenses(expenses)
    previous_expenses_total = _sum_operating_expenses(previous_expenses)
    balance = receipts - _sum_cash(cash, "saida")
    previous_balance = previous_receipts - _sum_cash(previous_cash, "saida")

    first_row = st.columns(2)
    first_row[0].metric(
        "Faturamento líquido",
        format_currency_br(billing),
        delta=_delta_label(billing, previous_billing),
        help="Valor líquido das faturas emitidas no período selecionado.",
    )
    first_row[1].metric(
        "Recebimentos",
        format_currency_br(receipts),
        delta=_delta_label(receipts, previous_receipts),
        help="Dinheiro que efetivamente entrou no caixa no período.",
    )
    second_row = st.columns(2)
    second_row[0].metric(
        "Gastos operacionais",
        format_currency_br(expenses_total),
        delta=_delta_label(expenses_total, previous_expenses_total),
        delta_color="inverse",
        help="Custos operacionais consolidados; investimentos são apresentados separadamente no Financeiro.",
    )
    second_row[1].metric(
        "Saldo operacional de caixa",
        format_currency_br(balance),
        delta=_delta_label(balance, previous_balance),
        help="Entradas recebidas menos saídas pagas no período.",
    )


def _render_operational_snapshot(
    snapshot: dict[str, float],
    works: pd.DataFrame,
    employees: pd.DataFrame,
    start: date,
    end: date,
    previous_start: date,
    previous_end: date,
) -> None:
    new_works = int(_filter_period(works, start, end).shape[0])
    previous_new_works = int(_filter_period(works, previous_start, previous_end).shape[0])
    current_headcount = _headcount_at(employees, end)
    previous_headcount = _headcount_at(employees, previous_end)

    st.subheader("Operação da empresa")
    first_row = st.columns(2)
    first_row[0].metric("Obras em andamento", int(snapshot["obras_em_andamento"]))
    first_row[1].metric("Novas obras no período", new_works, delta=new_works - previous_new_works)
    second_row = st.columns(2)
    second_row[0].metric(
        "Carteira contratada a executar",
        format_currency_br(snapshot["carteira_a_executar"]),
        help="Saldo dos contratos ativos ou em aberto depois do faturamento já registrado.",
    )
    second_row[1].metric(
        "Funcionários no encerramento",
        current_headcount,
        delta=current_headcount - previous_headcount,
        help="Quadro no último dia do período comparado com o encerramento do período anterior.",
    )

    third_row = st.columns(2)
    third_row[0].metric("Valor do estoque", format_currency_br(snapshot["valor_estoque"]))
    third_row[1].metric(
        "Frota disponível",
        f"{int(snapshot['frota_disponivel'])} de {int(snapshot['frota_total'])}",
        help="Veículos e equipamentos disponíveis em relação ao total cadastrado.",
    )
    fourth_row = st.columns(2)
    fourth_row[0].metric(
        "Materiais críticos",
        int(snapshot["itens_criticos"]),
        delta_color="inverse",
        help="Itens com quantidade atual igual ou inferior ao estoque mínimo.",
    )
    fourth_row[1].metric(
        "Frota em manutenção",
        int(snapshot["frota_manutencao"]),
        delta_color="inverse",
    )

    left, right = st.columns(2)
    with left:
        st.caption("Situação atual das obras")
        works_status = pd.DataFrame(
            {
                "Situação": ["Planejadas", "Em andamento", "Concluídas"],
                "Quantidade": [
                    int(snapshot["obras_planejadas"]),
                    int(snapshot["obras_em_andamento"]),
                    int(snapshot["obras_concluidas"]),
                ],
            }
        )
        st.bar_chart(works_status.set_index("Situação")["Quantidade"], horizontal=True, height=230)
    with right:
        st.caption("Situação atual da frota")
        fleet_status = pd.DataFrame(
            {
                "Situação": ["Disponível", "Em uso", "Em manutenção"],
                "Quantidade": [
                    int(snapshot["frota_disponivel"]),
                    int(snapshot["frota_em_uso"]),
                    int(snapshot["frota_manutencao"]),
                ],
            }
        )
        st.bar_chart(fleet_status.set_index("Situação")["Quantidade"], horizontal=True, height=230)

    st.subheader("Pontos de atenção")
    alerts = []
    if snapshot["obras_atrasadas"]:
        alerts.append(f"{int(snapshot['obras_atrasadas'])} obra(s) ultrapassaram a previsão de conclusão.")
    if snapshot["pagamentos_atrasados"]:
        alerts.append(f"{int(snapshot['pagamentos_atrasados'])} conta(s) a pagar estão vencidas.")
    if snapshot["recebimentos_atrasados"]:
        alerts.append(f"{int(snapshot['recebimentos_atrasados'])} conta(s) a receber estão vencidas.")
    if snapshot["itens_criticos"]:
        alerts.append(f"{int(snapshot['itens_criticos'])} material(is) atingiram o estoque mínimo.")
    if snapshot["frota_manutencao"]:
        alerts.append(f"{int(snapshot['frota_manutencao'])} equipamento(s) estão em manutenção.")
    if alerts:
        for alert in alerts:
            st.warning(alert)
    else:
        st.success("Nenhum alerta crítico foi identificado nos registros atuais.")


def render_executive_dashboard(db: Session) -> None:
    st.header("Dashboard Executivo", anchor="dashboard-executivo")
    st.caption("Acompanhe o resultado geral da empresa e identifique rapidamente crescimento, queda ou pontos de atenção.")
    today = today_in_timezone(APP_SETTINGS.app_timezone)
    period = st.selectbox(
        "Período da análise executiva",
        ["Mês atual", "Últimos 6 meses", "Últimos 12 meses", "Todo o histórico"],
        index=2,
        key="executive_period",
    )
    start, end = executive_period_bounds(period, today)
    previous_start, previous_end = executive_previous_period_bounds(period, start, end)
    if period == "Todo o histórico":
        st.caption(f"Valores registrados até {end.strftime('%d/%m/%Y')}.")
    else:
        st.caption(
            f"Período atual: {start.strftime('%d/%m/%Y')} a {end.strftime('%d/%m/%Y')} · "
            f"comparação: {previous_start.strftime('%d/%m/%Y')} a {previous_end.strftime('%d/%m/%Y')}."
        )

    expenses, revenue, cash = load_financial_data(db)
    current_expenses = _filter_period(expenses, start, end)
    current_revenue = _filter_period(revenue, start, end)
    current_cash = _filter_period(cash, start, end)
    previous_expenses = _filter_period(expenses, previous_start, previous_end)
    previous_revenue = _filter_period(revenue, previous_start, previous_end)
    previous_cash = _filter_period(cash, previous_start, previous_end)
    snapshot = _load_snapshot(db)
    works = _load_works(db)
    employees = _load_employees(db)

    _render_executive_kpis(
        current_expenses,
        current_revenue,
        current_cash,
        previous_expenses,
        previous_revenue,
        previous_cash,
    )
    _render_operational_snapshot(snapshot, works, employees, start, end, previous_start, previous_end)
    render_dashboard_trends(db)


def _render_planned_dashboard(item: dict[str, Any]) -> None:
    st.header(f"Dashboard de {item['name']}")
    st.info("Este painel está organizado na central e será implementado na próxima etapa do projeto.")
    st.write(item["description"])
    st.subheader("Indicadores previstos")
    for indicator in item["indicators"]:
        st.markdown(f"- {indicator}")
    st.caption(
        "Os cadastros e relacionamentos que alimentarão este painel continuam disponíveis nos módulos operacionais. "
        "Nenhum número parcial é apresentado aqui como se fosse um indicador concluído."
    )


def render_dashboard_hub(db: Session) -> str:
    st.title("Central de Dashboards")
    st.write("Escolha a visão gerencial que deseja consultar. Executivo, Financeiro e Obras e Engenharia estão disponíveis.")
    selected = st.selectbox(
        "Qual dashboard você quer visualizar?",
        dashboard_names(),
        format_func=_dashboard_label,
        key="dashboard_selected_view",
    )
    selected_item = next(item for item in DASHBOARD_CATALOG if item["name"] == selected)
    st.caption(selected_item["description"])
    st.divider()

    if selected == "Executivo":
        render_executive_dashboard(db)
    elif selected == "Financeiro e Fluxo de Caixa":
        render_financial_area(db=db, embedded=True)
    elif selected == "Obras e Engenharia":
        render_works_dashboard(db)
    else:
        _render_planned_dashboard(selected_item)
    return selected
