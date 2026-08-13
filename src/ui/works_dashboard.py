from __future__ import annotations

from datetime import date, timedelta
from typing import Any, Mapping

import pandas as pd
import streamlit as st
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.core.config.settings import get_settings
from src.shared.utils.brazil_localization import format_currency_br, format_number_br, today_in_timezone
from src.ui.financial_dashboard import _render_monthly_line_chart


APP_SETTINGS = get_settings()


WORKS_OVERVIEW_SQL = """
WITH budgets AS (
    SELECT obra_id, valor_total
    FROM (
        SELECT ob.obra_id, ob.valor_total,
               ROW_NUMBER() OVER (
                   PARTITION BY ob.obra_id
                   ORDER BY CASE WHEN ob.status = 'vigente' THEN 0 ELSE 1 END,
                            ob.versao DESC, ob.id DESC
               ) AS position
        FROM orcamentos_base ob
    ) ranked
    WHERE position = 1
), costs AS (
    SELECT obra_id, SUM(valor_total)::numeric AS custo_realizado
    FROM apropriacoes_custo GROUP BY obra_id
), measurements AS (
    SELECT obra_id, SUM(valor_medido)::numeric AS valor_medido,
           COUNT(*)::numeric AS total_medicoes
    FROM medicoes GROUP BY obra_id
), schedules AS (
    SELECT obra_id, COUNT(*)::numeric AS total_etapas,
           COUNT(*) FILTER (WHERE status = 'concluido' OR percentual_concluido >= 100)::numeric AS etapas_concluidas,
           COUNT(*) FILTER (
               WHERE data_fim < CURRENT_DATE
                 AND percentual_concluido < 100
                 AND status <> 'concluido'
           )::numeric AS etapas_atrasadas,
           AVG(percentual_concluido)::numeric AS progresso_cronograma
    FROM cronogramas GROUP BY obra_id
), calls AS (
    SELECT obra_id,
           COUNT(*) FILTER (WHERE status NOT IN ('resolvido', 'fechado', 'cancelado'))::numeric AS chamados_abertos,
           COUNT(*) FILTER (
               WHERE status NOT IN ('resolvido', 'fechado', 'cancelado')
                 AND prioridade = 'critica'
           )::numeric AS chamados_criticos
    FROM chamados_tecnicos GROUP BY obra_id
), revisions AS (
    SELECT projeto_id, COUNT(*)::numeric AS total_revisoes,
           COUNT(*) FILTER (WHERE aprovado = false)::numeric AS revisoes_pendentes
    FROM revisoes_projeto GROUP BY projeto_id
)
SELECT
    o.id AS obra_id,
    o.nome AS obra,
    o.status,
    o.percentual_fisico::numeric AS percentual_fisico,
    o.data_inicio,
    o.data_previsao_fim,
    o.data_fim,
    o.cidade,
    o.estado,
    p.id AS projeto_id,
    p.nome AS projeto,
    p.status AS status_projeto,
    f.nome AS responsavel,
    cl.nome AS cliente,
    COALESCE(b.valor_total, 0)::numeric AS orcamento,
    COALESCE(c.custo_realizado, 0)::numeric AS custo_realizado,
    COALESCE(m.valor_medido, 0)::numeric AS valor_medido,
    COALESCE(m.total_medicoes, 0)::numeric AS total_medicoes,
    COALESCE(s.total_etapas, 0)::numeric AS total_etapas,
    COALESCE(s.etapas_concluidas, 0)::numeric AS etapas_concluidas,
    COALESCE(s.etapas_atrasadas, 0)::numeric AS etapas_atrasadas,
    COALESCE(s.progresso_cronograma, 0)::numeric AS progresso_cronograma,
    COALESCE(ca.chamados_abertos, 0)::numeric AS chamados_abertos,
    COALESCE(ca.chamados_criticos, 0)::numeric AS chamados_criticos,
    COALESCE(r.total_revisoes, 0)::numeric AS total_revisoes,
    COALESCE(r.revisoes_pendentes, 0)::numeric AS revisoes_pendentes
FROM obras o
JOIN projetos p ON p.id = o.projeto_id
JOIN contratos ct ON ct.id = o.contrato_id
JOIN clientes cl ON cl.id = ct.cliente_id
LEFT JOIN funcionarios f ON f.id = o.responsavel_id
LEFT JOIN budgets b ON b.obra_id = o.id
LEFT JOIN costs c ON c.obra_id = o.id
LEFT JOIN measurements m ON m.obra_id = o.id
LEFT JOIN schedules s ON s.obra_id = o.id
LEFT JOIN calls ca ON ca.obra_id = o.id
LEFT JOIN revisions r ON r.projeto_id = p.id
ORDER BY o.nome
"""


ACTIVITIES_SQL = """
SELECT c.id, c.obra_id, o.nome AS obra, c.atividade, c.data_inicio, c.data_fim,
       c.peso_percentual::numeric AS peso_percentual,
       c.percentual_concluido::numeric AS percentual_concluido,
       c.status,
       (c.data_fim < CURRENT_DATE AND c.percentual_concluido < 100 AND c.status <> 'concluido') AS atrasada
FROM cronogramas c
JOIN obras o ON o.id = c.obra_id
ORDER BY c.data_fim, o.nome, c.atividade
"""


CALLS_SQL = """
SELECT ch.id, ch.obra_id, o.nome AS obra, ch.titulo, ch.prioridade, ch.status,
       f.nome AS solicitante, ch.created_at
FROM chamados_tecnicos ch
JOIN obras o ON o.id = ch.obra_id
LEFT JOIN funcionarios f ON f.id = ch.solicitante_id
ORDER BY ch.created_at DESC, ch.id DESC
"""


REVISIONS_SQL = """
SELECT rp.id, o.id AS obra_id, o.nome AS obra, p.nome AS projeto,
       rp.numero_revisao, rp.data_revisao, rp.aprovado, f.nome AS responsavel,
       rp.descricao, rp.motivo
FROM revisoes_projeto rp
JOIN projetos p ON p.id = rp.projeto_id
LEFT JOIN obras o ON o.projeto_id = p.id
LEFT JOIN funcionarios f ON f.id = rp.responsavel_id
ORDER BY rp.data_revisao DESC, rp.numero_revisao DESC
"""


STATUS_LABELS = {
    "planejada": "Planejada",
    "em_andamento": "Em andamento",
    "concluida": "Concluída",
    "cancelada": "Cancelada",
    "planejado": "Planejado",
    "concluido": "Concluído",
    "aprovado": "Aprovado",
    "em_elaboracao": "Em elaboração",
    "em_revisao": "Em revisão",
    "aberto": "Aberto",
    "em_atendimento": "Em atendimento",
    "resolvido": "Resolvido",
}


PRIORITY_LABELS = {
    "baixa": "Baixa",
    "media": "Média",
    "alta": "Alta",
    "critica": "Crítica",
}


NUMERIC_COLUMNS = (
    "percentual_fisico",
    "orcamento",
    "custo_realizado",
    "valor_medido",
    "total_medicoes",
    "total_etapas",
    "etapas_concluidas",
    "etapas_atrasadas",
    "progresso_cronograma",
    "chamados_abertos",
    "chamados_criticos",
    "total_revisoes",
    "revisoes_pendentes",
)


def _query_frame(db: Session, sql: str) -> pd.DataFrame:
    return pd.read_sql_query(text(sql), db.connection())


def load_works_dashboard_data(db: Session) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    works = _query_frame(db, WORKS_OVERVIEW_SQL)
    for column in ("data_inicio", "data_previsao_fim", "data_fim"):
        works[column] = pd.to_datetime(works[column], errors="coerce")
    for column in NUMERIC_COLUMNS:
        works[column] = pd.to_numeric(works[column], errors="coerce").fillna(0.0)

    activities = _query_frame(db, ACTIVITIES_SQL)
    for column in ("data_inicio", "data_fim"):
        activities[column] = pd.to_datetime(activities[column], errors="coerce")
    for column in ("peso_percentual", "percentual_concluido"):
        activities[column] = pd.to_numeric(activities[column], errors="coerce").fillna(0.0)

    calls = _query_frame(db, CALLS_SQL)
    calls["created_at"] = pd.to_datetime(calls["created_at"], errors="coerce")
    revisions = _query_frame(db, REVISIONS_SQL)
    revisions["data_revisao"] = pd.to_datetime(revisions["data_revisao"], errors="coerce")
    return works, activities, calls, revisions


def _date_value(value: Any) -> date | None:
    if value is None or pd.isna(value):
        return None
    if isinstance(value, pd.Timestamp):
        return value.date()
    if isinstance(value, date):
        return value
    parsed = pd.to_datetime(value, errors="coerce")
    return None if pd.isna(parsed) else parsed.date()


def work_attention(
    status: str,
    progress: float,
    forecast: Any,
    late_activities: float,
    end_date: Any,
    critical_calls: float,
    today: date,
) -> str:
    forecast_date = _date_value(forecast)
    actual_end = _date_value(end_date)
    if status in {"cancelada", "cancelado"}:
        return "Cancelada"
    if status == "concluida":
        if progress < 100:
            return "Dados inconsistentes"
        if actual_end is None:
            return "Sem data de conclusão"
        return "Concluída"
    if forecast_date is not None and forecast_date < today:
        return "Atrasada"
    if late_activities > 0:
        return "Etapas atrasadas"
    if critical_calls > 0:
        return "Atenção técnica"
    if forecast_date is not None and forecast_date <= today + timedelta(days=30) and progress < 90:
        return "Prazo próximo"
    return "Em dia"


def analysis_period_bounds(period: str, today: date, works: pd.DataFrame) -> tuple[date, date]:
    if period == "Ano atual":
        return date(today.year, 1, 1), today
    if period == "Últimos 12 meses":
        start = (pd.Timestamp(today).to_period("M").start_time - pd.DateOffset(months=11)).date()
        return start, today
    dates = []
    if not works.empty:
        dates.extend(works["data_inicio"].dropna().tolist())
        dates.extend(works["data_previsao_fim"].dropna().tolist())
        dates.extend(works["data_fim"].dropna().tolist())
    if not dates:
        return date(today.year, 1, 1), today
    return min(dates).date(), max(max(dates).date(), today)


def filter_works(
    works: pd.DataFrame,
    start: date,
    end: date,
    selected_works: list[str],
    selected_responsibles: list[str],
    selected_statuses: list[str],
) -> pd.DataFrame:
    if works.empty:
        return works
    filtered = works.copy()
    period_start, period_end = pd.Timestamp(start), pd.Timestamp(end)
    finish = filtered["data_fim"].fillna(filtered["data_previsao_fim"]).fillna(period_end)
    starts_before_end = filtered["data_inicio"].isna() | filtered["data_inicio"].le(period_end)
    finishes_after_start = finish.ge(period_start)
    filtered = filtered[starts_before_end & finishes_after_start]
    if selected_works:
        filtered = filtered[filtered["obra"].isin(selected_works)]
    if selected_responsibles:
        filtered = filtered[filtered["responsavel"].isin(selected_responsibles)]
    if selected_statuses:
        filtered = filtered[filtered["status"].isin(selected_statuses)]
    return filtered.copy()


def build_work_start_series(works: pd.DataFrame) -> pd.DataFrame:
    if works.empty or works["data_inicio"].dropna().empty:
        return pd.DataFrame(columns=["data", "Novas obras", "Total acumulado"])
    series = works.dropna(subset=["data_inicio"]).copy()
    series["data"] = series["data_inicio"].dt.to_period("M").dt.to_timestamp()
    series = series.groupby("data", as_index=False).size().rename(columns={"size": "Novas obras"})
    calendar = pd.DataFrame({"data": pd.date_range(series["data"].min(), series["data"].max(), freq="MS")})
    series = calendar.merge(series, on="data", how="left").fillna({"Novas obras": 0})
    series["Total acumulado"] = series["Novas obras"].cumsum()
    return series


def _metric_totals(works: pd.DataFrame) -> Mapping[str, float]:
    budget = float(works["orcamento"].sum()) if not works.empty else 0.0
    cost = float(works["custo_realizado"].sum()) if not works.empty else 0.0
    return {
        "budget": budget,
        "cost": cost,
        "measured": float(works["valor_medido"].sum()) if not works.empty else 0.0,
        "consumption": (cost / budget * 100) if budget else 0.0,
    }


def _add_attention(works: pd.DataFrame, today: date) -> pd.DataFrame:
    result = works.copy()
    result["atencao"] = result.apply(
        lambda row: work_attention(
            str(row["status"]),
            float(row["percentual_fisico"]),
            row["data_previsao_fim"],
            float(row["etapas_atrasadas"]),
            row["data_fim"],
            float(row["chamados_criticos"]),
            today,
        ),
        axis=1,
    )
    return result


def _format_status(value: Any) -> str:
    return STATUS_LABELS.get(str(value), str(value).replace("_", " ").title())


def _render_top_metrics(works: pd.DataFrame) -> None:
    delayed = works["atencao"].isin(["Atrasada", "Etapas atrasadas"]).sum() if not works.empty else 0
    data_issues = works["atencao"].isin(["Dados inconsistentes", "Sem data de conclusão"]).sum() if not works.empty else 0
    totals = _metric_totals(works)

    first_row = st.columns(4)
    first_row[0].metric("Obras analisadas", len(works))
    first_row[1].metric("Em andamento", int((works["status"] == "em_andamento").sum()))
    first_row[2].metric("Atrasadas", int(delayed), delta_color="inverse")
    first_row[3].metric("Concluídas", int((works["status"] == "concluida").sum()))

    second_row = st.columns(3)
    second_row[0].metric("Orçamento vigente", format_currency_br(totals["budget"]))
    second_row[1].metric("Custo apropriado", format_currency_br(totals["cost"]))
    second_row[2].metric("Total medido", format_currency_br(totals["measured"]))

    third_row = st.columns(4)
    progress = float(works["percentual_fisico"].mean()) if not works.empty else 0.0
    third_row[0].metric("Avanço físico médio", f"{format_number_br(progress, 1)}%")
    third_row[1].metric("Orçamento consumido", f"{format_number_br(totals['consumption'], 1)}%")
    third_row[2].metric("Chamados em aberto", int(works["chamados_abertos"].sum()))
    third_row[3].metric("Pendências cadastrais", int(data_issues), delta_color="inverse")

    if data_issues:
        st.warning(
            f"{int(data_issues)} obra(s) concluída(s) apresentam avanço inferior a 100% ou não possuem data real de conclusão. "
            "Revise esses cadastros antes de utilizar os indicadores em decisões oficiais."
        )


def _render_overview(works: pd.DataFrame) -> None:
    left, right = st.columns(2)
    with left:
        st.subheader("Situação das obras")
        status = works.assign(Situação=works["status"].map(_format_status)).groupby("Situação").size().sort_values(ascending=False)
        st.bar_chart(status, horizontal=True, height=300)
    with right:
        st.subheader("Obras por responsável")
        responsibles = works["responsavel"].fillna("Sem responsável").value_counts().head(12)
        st.bar_chart(responsibles, horizontal=True, height=300)

    st.subheader("Crescimento da carteira de obras")
    series = build_work_start_series(works)
    if series.empty:
        st.info("Não existem datas de início suficientes para montar a evolução.")
    else:
        _render_monthly_line_chart(series.set_index("data")[["Novas obras", "Total acumulado"]], height=350, monetary=False)

    st.subheader("Avanço físico por obra")
    progress = works[["obra", "percentual_fisico"]].sort_values("percentual_fisico", ascending=False).set_index("obra")
    st.bar_chart(progress, horizontal=True, height=max(320, min(650, 32 * len(progress))))


def _ranking_table(works: pd.DataFrame) -> pd.DataFrame:
    display = works.copy()
    attention_order = {
        "Atrasada": 0,
        "Etapas atrasadas": 1,
        "Dados inconsistentes": 2,
        "Sem data de conclusão": 3,
        "Atenção técnica": 4,
        "Prazo próximo": 5,
        "Em dia": 6,
        "Concluída": 7,
    }
    display["ordem_atencao"] = display["atencao"].map(attention_order).fillna(99)
    display = display.sort_values(["ordem_atencao", "data_previsao_fim", "obra"])
    display["status"] = display["status"].map(_format_status)
    display["percentual_fisico"] = display["percentual_fisico"].map(lambda value: f"{format_number_br(value, 1)}%")
    display["orcamento"] = display["orcamento"].map(format_currency_br)
    display["custo_realizado"] = display["custo_realizado"].map(format_currency_br)
    display["valor_medido"] = display["valor_medido"].map(format_currency_br)
    return display[
        [
            "atencao", "obra", "projeto", "responsavel", "status", "percentual_fisico",
            "data_previsao_fim", "orcamento", "custo_realizado", "valor_medido",
            "etapas_atrasadas", "chamados_abertos", "revisoes_pendentes",
        ]
    ].rename(
        columns={
            "atencao": "Situação gerencial",
            "obra": "Obra",
            "projeto": "Projeto",
            "responsavel": "Responsável",
            "status": "Status",
            "percentual_fisico": "Avanço físico",
            "data_previsao_fim": "Previsão de término",
            "orcamento": "Orçamento",
            "custo_realizado": "Custo realizado",
            "valor_medido": "Valor medido",
            "etapas_atrasadas": "Etapas atrasadas",
            "chamados_abertos": "Chamados abertos",
            "revisoes_pendentes": "Revisões pendentes",
        }
    )


def _render_schedule(works: pd.DataFrame, activities: pd.DataFrame) -> None:
    st.subheader("Ranking gerencial das obras")
    st.caption("Prioriza atrasos, inconsistências de cadastro, pendências técnicas e proximidade do prazo.")
    st.dataframe(
        _ranking_table(works),
        width="stretch",
        hide_index=True,
        column_config={"Previsão de término": st.column_config.DateColumn(format="DD/MM/YYYY")},
    )

    total = len(activities)
    completed = int(((activities["status"] == "concluido") | (activities["percentual_concluido"] >= 100)).sum()) if total else 0
    late = int(activities["atrasada"].fillna(False).sum()) if total else 0
    average = float(activities["percentual_concluido"].mean()) if total else 0.0
    columns = st.columns(4)
    columns[0].metric("Etapas", total)
    columns[1].metric("Etapas concluídas", completed)
    columns[2].metric("Etapas atrasadas", late, delta_color="inverse")
    columns[3].metric("Progresso médio", f"{format_number_br(average, 1)}%")

    if activities.empty:
        st.info("Nenhuma etapa de cronograma encontrada para os filtros selecionados.")
        return
    display = activities.copy()
    display["Situação"] = display.apply(lambda row: "Atrasada" if row["atrasada"] else _format_status(row["status"]), axis=1)
    display["Progresso"] = display["percentual_concluido"].map(lambda value: f"{format_number_br(value, 1)}%")
    display = display[["Situação", "obra", "atividade", "data_inicio", "data_fim", "Progresso"]].rename(
        columns={"obra": "Obra", "atividade": "Atividade", "data_inicio": "Início", "data_fim": "Término"}
    )
    st.dataframe(
        display.sort_values(["Situação", "Término"]),
        width="stretch",
        hide_index=True,
        column_config={"Início": st.column_config.DateColumn(format="DD/MM/YYYY"), "Término": st.column_config.DateColumn(format="DD/MM/YYYY")},
    )


def _render_budget(works: pd.DataFrame) -> None:
    st.subheader("Orçamento, custo e medição por obra")
    chart = works[["obra", "orcamento", "custo_realizado", "valor_medido"]].rename(
        columns={"obra": "Obra", "orcamento": "Orçamento", "custo_realizado": "Custo realizado", "valor_medido": "Valor medido"}
    )
    st.bar_chart(chart.set_index("Obra"), horizontal=True, height=max(380, min(720, 42 * len(chart))))

    display = works.copy()
    display["saldo_orcamento"] = display["orcamento"] - display["custo_realizado"]
    display["consumo"] = display.apply(lambda row: row["custo_realizado"] / row["orcamento"] * 100 if row["orcamento"] else 0.0, axis=1)
    display = display.sort_values("consumo", ascending=False)
    for column in ("orcamento", "custo_realizado", "saldo_orcamento", "valor_medido"):
        display[column] = display[column].map(format_currency_br)
    display["consumo"] = display["consumo"].map(lambda value: f"{format_number_br(value, 1)}%")
    st.dataframe(
        display[["obra", "orcamento", "custo_realizado", "consumo", "saldo_orcamento", "valor_medido"]].rename(
            columns={"obra": "Obra", "orcamento": "Orçamento", "custo_realizado": "Custo realizado", "consumo": "Consumo", "saldo_orcamento": "Saldo do orçamento", "valor_medido": "Valor medido"}
        ),
        width="stretch",
        hide_index=True,
    )


def _render_engineering(works: pd.DataFrame, calls: pd.DataFrame, revisions: pd.DataFrame) -> None:
    open_calls = calls[~calls["status"].isin(["resolvido", "fechado", "cancelado"])] if not calls.empty else calls
    critical = open_calls[open_calls["prioridade"] == "critica"] if not open_calls.empty else open_calls
    pending_revisions = revisions[~revisions["aprovado"]] if not revisions.empty else revisions
    columns = st.columns(4)
    columns[0].metric("Chamados em aberto", len(open_calls))
    columns[1].metric("Chamados críticos", len(critical), delta_color="inverse")
    columns[2].metric("Revisões pendentes", len(pending_revisions), delta_color="inverse")
    columns[3].metric("Revisões aprovadas", int(revisions["aprovado"].sum()) if not revisions.empty else 0)

    left, right = st.columns(2)
    with left:
        st.subheader("Chamados por prioridade")
        if calls.empty:
            st.info("Nenhum chamado encontrado.")
        else:
            priorities = calls["prioridade"].map(lambda value: PRIORITY_LABELS.get(str(value), str(value).title())).value_counts()
            st.bar_chart(priorities, horizontal=True, height=280)
    with right:
        st.subheader("Situação dos projetos")
        projects = works["status_projeto"].map(_format_status).value_counts()
        st.bar_chart(projects, horizontal=True, height=280)

    st.subheader("Chamados que exigem acompanhamento")
    if open_calls.empty:
        st.success("Não existem chamados técnicos em aberto para o recorte selecionado.")
    else:
        display = open_calls.copy()
        display["prioridade"] = display["prioridade"].map(lambda value: PRIORITY_LABELS.get(str(value), str(value).title()))
        display["status"] = display["status"].map(_format_status)
        st.dataframe(
            display[["obra", "titulo", "prioridade", "status", "solicitante", "created_at"]].rename(
                columns={"obra": "Obra", "titulo": "Chamado", "prioridade": "Prioridade", "status": "Status", "solicitante": "Solicitante", "created_at": "Registrado em"}
            ),
            width="stretch",
            hide_index=True,
            column_config={"Registrado em": st.column_config.DatetimeColumn(format="DD/MM/YYYY HH:mm")},
        )

    st.subheader("Revisões de projeto")
    if revisions.empty:
        st.info("Nenhuma revisão encontrada para o recorte selecionado.")
    else:
        display = revisions.copy()
        display["Situação"] = display["aprovado"].map({True: "Aprovada", False: "Pendente"})
        st.dataframe(
            display[["Situação", "obra", "projeto", "numero_revisao", "data_revisao", "responsavel", "descricao"]].rename(
                columns={"obra": "Obra", "projeto": "Projeto", "numero_revisao": "Revisão", "data_revisao": "Data", "responsavel": "Responsável", "descricao": "Descrição"}
            ),
            width="stretch",
            hide_index=True,
            column_config={"Data": st.column_config.DateColumn(format="DD/MM/YYYY")},
        )


def render_works_dashboard(db: Session) -> None:
    st.header("Dashboard de Obras e Engenharia", anchor="dashboard-obras-engenharia")
    st.caption("Acompanhe prazo, avanço físico, cronograma, orçamento, medições, chamados e revisões sem procurar códigos internos.")
    works, activities, calls, revisions = load_works_dashboard_data(db)
    today = today_in_timezone(APP_SETTINGS.app_timezone)

    st.subheader("Filtros da análise")
    period = st.selectbox("Período", ["Ano atual", "Últimos 12 meses", "Todo o histórico", "Personalizado"], key="works_dashboard_period")
    default_start, default_end = analysis_period_bounds(period, today, works)
    if period == "Personalizado":
        date_columns = st.columns(2)
        start = date_columns[0].date_input("Data inicial", value=default_start, key="works_dashboard_start")
        end = date_columns[1].date_input("Data final", value=default_end, key="works_dashboard_end")
    else:
        start, end = default_start, default_end
        st.caption(f"Período considerado: {start.strftime('%d/%m/%Y')} a {end.strftime('%d/%m/%Y')}")
    if start > end:
        st.error("A data inicial precisa ser anterior à data final.")
        return

    work_options = sorted(works["obra"].dropna().astype(str).unique().tolist())
    responsible_options = sorted(works["responsavel"].dropna().astype(str).unique().tolist())
    status_options = sorted(works["status"].dropna().astype(str).unique().tolist())
    filter_columns = st.columns(3)
    selected_works = filter_columns[0].multiselect("Obras", work_options, placeholder="Todas as obras", key="works_dashboard_works")
    selected_responsibles = filter_columns[1].multiselect("Responsáveis", responsible_options, placeholder="Todos os responsáveis", key="works_dashboard_responsibles")
    selected_status_labels = filter_columns[2].multiselect(
        "Situações",
        [_format_status(value) for value in status_options],
        placeholder="Todas as situações",
        key="works_dashboard_statuses",
    )
    reverse_status = {_format_status(value): value for value in status_options}
    selected_statuses = [reverse_status[label] for label in selected_status_labels]

    works = filter_works(works, start, end, selected_works, selected_responsibles, selected_statuses)
    if works.empty:
        st.info("Nenhuma obra corresponde aos filtros selecionados.")
        return
    works = _add_attention(works, today)
    work_ids = works["obra_id"].astype(int).tolist()
    activities = activities[activities["obra_id"].isin(work_ids)].copy()
    calls = calls[calls["obra_id"].isin(work_ids)].copy()
    revisions = revisions[revisions["obra_id"].isin(work_ids)].copy()

    _render_top_metrics(works)
    tabs = st.tabs(["Visão geral", "Prazo e execução", "Orçamento e medições", "Engenharia e chamados"])
    with tabs[0]:
        _render_overview(works)
    with tabs[1]:
        _render_schedule(works, activities)
    with tabs[2]:
        _render_budget(works)
    with tabs[3]:
        _render_engineering(works, calls, revisions)
