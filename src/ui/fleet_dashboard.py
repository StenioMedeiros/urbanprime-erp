from __future__ import annotations

from datetime import date, timedelta
from typing import Any

import pandas as pd
import streamlit as st
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.core.config.settings import get_settings
from src.shared.utils.brazil_localization import format_currency_br, format_number_br, today_in_timezone
from src.ui.financial_dashboard import _render_monthly_line_chart


APP_SETTINGS = get_settings()


FLEET_SQL = """
SELECT
    frota.id AS frota_id,
    frota.identificacao,
    frota.tipo,
    frota.placa,
    frota.marca,
    frota.modelo,
    frota.ano_fabricacao,
    frota.data_aquisicao,
    frota.valor_aquisicao::numeric AS valor_aquisicao,
    frota.horimetro_atual::numeric AS horimetro_atual,
    frota.status,
    frota.obra_id AS obra_atual_id,
    obra.nome AS obra_atual
FROM frotas frota
LEFT JOIN obras obra ON obra.id = frota.obra_id
ORDER BY frota.identificacao
"""


MAINTENANCE_SQL = """
SELECT
    manutencao.id AS manutencao_id,
    manutencao.frota_id,
    frota.identificacao,
    frota.tipo AS tipo_frota,
    manutencao.fornecedor_id,
    COALESCE(NULLIF(fornecedor.nome_fantasia, ''), fornecedor.razao_social) AS fornecedor,
    manutencao.obra_id,
    obra.nome AS obra,
    manutencao.tipo,
    manutencao.descricao,
    manutencao.data_entrada,
    manutencao.data_saida,
    manutencao.custo::numeric AS custo,
    manutencao.horimetro::numeric AS horimetro,
    manutencao.status
FROM manutencoes_frota manutencao
JOIN frotas frota ON frota.id = manutencao.frota_id
LEFT JOIN fornecedores fornecedor ON fornecedor.id = manutencao.fornecedor_id
LEFT JOIN obras obra ON obra.id = manutencao.obra_id
ORDER BY manutencao.data_entrada DESC, manutencao.id DESC
"""


FUEL_SQL = """
SELECT
    abastecimento.id AS abastecimento_id,
    abastecimento.frota_id,
    frota.identificacao,
    frota.tipo AS tipo_frota,
    abastecimento.obra_id,
    obra.nome AS obra,
    abastecimento.responsavel_id,
    funcionario.nome AS responsavel,
    abastecimento.data_abastecimento,
    abastecimento.litros::numeric AS litros,
    abastecimento.valor_total::numeric AS valor_total,
    abastecimento.quilometragem_horimetro::numeric AS quilometragem_horimetro,
    abastecimento.observacao
FROM abastecimentos_frota abastecimento
JOIN frotas frota ON frota.id = abastecimento.frota_id
LEFT JOIN obras obra ON obra.id = abastecimento.obra_id
LEFT JOIN funcionarios funcionario ON funcionario.id = abastecimento.responsavel_id
ORDER BY abastecimento.data_abastecimento DESC, abastecimento.id DESC
"""


USAGE_SQL = """
SELECT
    utilizacao.id AS utilizacao_id,
    utilizacao.frota_id,
    frota.identificacao,
    frota.tipo AS tipo_frota,
    utilizacao.obra_id,
    obra.nome AS obra,
    utilizacao.funcionario_id,
    funcionario.nome AS operador,
    utilizacao.data_utilizacao,
    utilizacao.horas_utilizadas::numeric AS horas_utilizadas,
    utilizacao.horimetro_inicial::numeric AS horimetro_inicial,
    utilizacao.horimetro_final::numeric AS horimetro_final,
    utilizacao.custo_hora::numeric AS custo_hora,
    (utilizacao.horas_utilizadas * utilizacao.custo_hora)::numeric AS custo_utilizacao,
    utilizacao.observacao
FROM utilizacoes_frota utilizacao
JOIN frotas frota ON frota.id = utilizacao.frota_id
LEFT JOIN obras obra ON obra.id = utilizacao.obra_id
LEFT JOIN funcionarios funcionario ON funcionario.id = utilizacao.funcionario_id
ORDER BY utilizacao.data_utilizacao DESC, utilizacao.id DESC
"""


AVAILABILITY_GOALS_SQL = """
SELECT competencia, valor_meta::numeric AS valor_meta
FROM metas_indicadores
WHERE codigo_indicador = 'DISPONIBILIDADE_FROTA'
  AND ativo = true
ORDER BY competencia
"""


STATUS_LABELS = {
    "disponivel": "Disponível",
    "em_uso": "Em uso",
    "em_manutencao": "Em manutenção",
    "inativo": "Inativo",
    "baixado": "Baixado",
    "concluida": "Concluída",
    "aberta": "Aberta",
    "em_andamento": "Em andamento",
    "cancelada": "Cancelada",
}


FLEET_NUMERIC_COLUMNS = ("valor_aquisicao", "horimetro_atual")
MAINTENANCE_NUMERIC_COLUMNS = ("custo", "horimetro")
FUEL_NUMERIC_COLUMNS = ("litros", "valor_total", "quilometragem_horimetro")
USAGE_NUMERIC_COLUMNS = (
    "horas_utilizadas",
    "horimetro_inicial",
    "horimetro_final",
    "custo_hora",
    "custo_utilizacao",
)


def _query_frame(db: Session, sql: str) -> pd.DataFrame:
    return pd.read_sql_query(text(sql), db.connection())


def load_fleet_dashboard_data(
    db: Session,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    fleet = _query_frame(db, FLEET_SQL)
    fleet["data_aquisicao"] = pd.to_datetime(fleet["data_aquisicao"], errors="coerce")
    for column in FLEET_NUMERIC_COLUMNS:
        fleet[column] = pd.to_numeric(fleet[column], errors="coerce").fillna(0.0)

    maintenance = _query_frame(db, MAINTENANCE_SQL)
    for column in ("data_entrada", "data_saida"):
        maintenance[column] = pd.to_datetime(maintenance[column], errors="coerce")
    for column in MAINTENANCE_NUMERIC_COLUMNS:
        maintenance[column] = pd.to_numeric(maintenance[column], errors="coerce").fillna(0.0)

    fuel = _query_frame(db, FUEL_SQL)
    fuel["data_abastecimento"] = pd.to_datetime(fuel["data_abastecimento"], errors="coerce")
    for column in FUEL_NUMERIC_COLUMNS:
        fuel[column] = pd.to_numeric(fuel[column], errors="coerce").fillna(0.0)

    usage = _query_frame(db, USAGE_SQL)
    usage["data_utilizacao"] = pd.to_datetime(usage["data_utilizacao"], errors="coerce")
    for column in USAGE_NUMERIC_COLUMNS:
        usage[column] = pd.to_numeric(usage[column], errors="coerce").fillna(0.0)

    goals = _query_frame(db, AVAILABILITY_GOALS_SQL)
    goals["valor_meta"] = pd.to_numeric(goals["valor_meta"], errors="coerce").fillna(0.0)
    goals["data"] = pd.to_datetime(goals["competencia"] + "-01", errors="coerce")
    return fleet, maintenance, fuel, usage, goals


def _date_value(value: Any) -> date | None:
    if value is None or pd.isna(value):
        return None
    if isinstance(value, pd.Timestamp):
        return value.date()
    if isinstance(value, date):
        return value
    parsed = pd.to_datetime(value, errors="coerce")
    return None if pd.isna(parsed) else parsed.date()


def fleet_attention(
    status: str,
    open_maintenance: float,
    last_usage: Any,
    current_meter: float,
    last_usage_meter: float,
    today: date,
) -> str:
    last_usage_date = _date_value(last_usage)
    if status in {"inativo", "baixado"}:
        return "Inativo"
    if current_meter > 0 and last_usage_meter > current_meter + 0.01:
        return "Horímetro divergente"
    if open_maintenance > 0 or status == "em_manutencao":
        return "Em manutenção"
    if last_usage_date is None:
        return "Sem utilização no período"
    if last_usage_date < today - timedelta(days=90):
        return "Sem utilização há 90 dias"
    if status == "em_uso":
        return "Em uso"
    if status == "disponivel":
        return "Disponível"
    return "Acompanhar"


def fleet_period_bounds(
    period: str,
    today: date,
    maintenance: pd.DataFrame,
    fuel: pd.DataFrame,
    usage: pd.DataFrame,
) -> tuple[date, date]:
    if period == "Ano atual":
        return date(today.year, 1, 1), today
    if period == "Últimos 90 dias":
        return today - timedelta(days=89), today
    if period == "Últimos 12 meses":
        start = (pd.Timestamp(today).to_period("M").start_time - pd.DateOffset(months=11)).date()
        return start, today
    dates: list[pd.Timestamp] = []
    if not maintenance.empty:
        dates.extend(maintenance["data_entrada"].dropna().tolist())
    if not fuel.empty:
        dates.extend(fuel["data_abastecimento"].dropna().tolist())
    if not usage.empty:
        dates.extend(usage["data_utilizacao"].dropna().tolist())
    historical_dates = [value for value in dates if value.date() <= today]
    if not historical_dates:
        return date(today.year, 1, 1), today
    return min(historical_dates).date(), today


def filter_fleet_data(
    fleet: pd.DataFrame,
    maintenance: pd.DataFrame,
    fuel: pd.DataFrame,
    usage: pd.DataFrame,
    start: date,
    end: date,
    selected_assets: list[str],
    selected_types: list[str],
    selected_statuses: list[str],
    selected_works: list[str],
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    filtered_fleet = fleet.copy()
    if selected_assets:
        filtered_fleet = filtered_fleet[filtered_fleet["identificacao"].isin(selected_assets)]
    if selected_types:
        filtered_fleet = filtered_fleet[filtered_fleet["tipo"].isin(selected_types)]
    if selected_statuses:
        filtered_fleet = filtered_fleet[filtered_fleet["status"].isin(selected_statuses)]

    asset_ids = filtered_fleet["frota_id"].dropna().astype(int).tolist()
    start_ts = pd.Timestamp(start)
    end_ts = pd.Timestamp(end)
    filtered_maintenance = maintenance[
        maintenance["frota_id"].isin(asset_ids)
        & maintenance["data_entrada"].between(start_ts, end_ts, inclusive="both")
    ].copy()
    filtered_fuel = fuel[
        fuel["frota_id"].isin(asset_ids)
        & fuel["data_abastecimento"].between(start_ts, end_ts, inclusive="both")
    ].copy()
    filtered_usage = usage[
        usage["frota_id"].isin(asset_ids)
        & usage["data_utilizacao"].between(start_ts, end_ts, inclusive="both")
    ].copy()

    if selected_works:
        filtered_maintenance = filtered_maintenance[filtered_maintenance["obra"].isin(selected_works)]
        filtered_fuel = filtered_fuel[filtered_fuel["obra"].isin(selected_works)]
        filtered_usage = filtered_usage[filtered_usage["obra"].isin(selected_works)]
        event_asset_ids = set(filtered_maintenance["frota_id"].tolist())
        event_asset_ids.update(filtered_fuel["frota_id"].tolist())
        event_asset_ids.update(filtered_usage["frota_id"].tolist())
        filtered_fleet = filtered_fleet[filtered_fleet["frota_id"].isin(event_asset_ids)]
    return filtered_fleet, filtered_maintenance, filtered_fuel, filtered_usage


def build_fleet_summary(
    fleet: pd.DataFrame,
    maintenance: pd.DataFrame,
    fuel: pd.DataFrame,
    usage: pd.DataFrame,
    today: date,
) -> pd.DataFrame:
    result = fleet.copy()
    maintenance_group = maintenance.groupby("frota_id", as_index=False).agg(
        manutencoes=("manutencao_id", "count"),
        custo_manutencao=("custo", "sum"),
        manutencoes_abertas=("status", lambda values: int((~values.isin(["concluida", "cancelada"])).sum())),
        ultima_manutencao=("data_entrada", "max"),
    )
    fuel_group = fuel.groupby("frota_id", as_index=False).agg(
        abastecimentos=("abastecimento_id", "count"),
        litros=("litros", "sum"),
        custo_combustivel=("valor_total", "sum"),
        ultimo_abastecimento=("data_abastecimento", "max"),
    )
    usage_group = usage.groupby("frota_id", as_index=False).agg(
        utilizacoes=("utilizacao_id", "count"),
        horas_utilizadas=("horas_utilizadas", "sum"),
        custo_utilizacao=("custo_utilizacao", "sum"),
        ultima_utilizacao=("data_utilizacao", "max"),
        ultimo_horimetro_utilizacao=("horimetro_final", "max"),
    )
    for grouped in (maintenance_group, fuel_group, usage_group):
        result = result.merge(grouped, on="frota_id", how="left")
    numeric_columns = (
        "manutencoes", "custo_manutencao", "manutencoes_abertas", "abastecimentos", "litros",
        "custo_combustivel", "utilizacoes", "horas_utilizadas", "custo_utilizacao",
        "ultimo_horimetro_utilizacao",
    )
    for column in numeric_columns:
        result[column] = pd.to_numeric(result[column], errors="coerce").fillna(0.0)
    result["custo_direto"] = result["custo_manutencao"] + result["custo_combustivel"]
    result["custo_direto_hora"] = result.apply(
        lambda row: row["custo_direto"] / row["horas_utilizadas"] if row["horas_utilizadas"] else 0.0,
        axis=1,
    )
    result["consumo_hora"] = result.apply(
        lambda row: row["litros"] / row["horas_utilizadas"] if row["horas_utilizadas"] else 0.0,
        axis=1,
    )
    result["atencao"] = result.apply(
        lambda row: fleet_attention(
            str(row["status"]),
            float(row["manutencoes_abertas"]),
            row["ultima_utilizacao"],
            float(row["horimetro_atual"]),
            float(row["ultimo_horimetro_utilizacao"]),
            today,
        ),
        axis=1,
    )
    return result


def build_fleet_cost_series(
    maintenance: pd.DataFrame,
    fuel: pd.DataFrame,
    usage: pd.DataFrame,
) -> pd.DataFrame:
    pieces: list[pd.DataFrame] = []
    for frame, date_column, value_column, name in (
        (maintenance, "data_entrada", "custo", "Manutenção"),
        (fuel, "data_abastecimento", "valor_total", "Combustível"),
        (usage, "data_utilizacao", "custo_utilizacao", "Custo de utilização"),
    ):
        if frame.empty or frame[date_column].dropna().empty:
            continue
        work = frame.dropna(subset=[date_column]).copy()
        work["data"] = work[date_column].dt.to_period("M").dt.to_timestamp()
        monthly = work.groupby("data", as_index=False)[value_column].sum().rename(columns={value_column: name})
        pieces.append(monthly)
    if not pieces:
        return pd.DataFrame(columns=["data", "Manutenção", "Combustível", "Custo de utilização"])
    series = pieces[0]
    for piece in pieces[1:]:
        series = series.merge(piece, on="data", how="outer")
    series = series.sort_values("data").fillna(0.0)
    calendar = pd.DataFrame({"data": pd.date_range(series["data"].min(), series["data"].max(), freq="MS")})
    return calendar.merge(series, on="data", how="left").fillna(0.0)


def count_future_events(
    maintenance: pd.DataFrame,
    fuel: pd.DataFrame,
    usage: pd.DataFrame,
    today: date,
) -> dict[str, int]:
    reference = pd.Timestamp(today)
    return {
        "manutenções": int(maintenance["data_entrada"].gt(reference).sum()),
        "abastecimentos": int(fuel["data_abastecimento"].gt(reference).sum()),
        "utilizações": int(usage["data_utilizacao"].gt(reference).sum()),
    }


def _status_label(value: Any) -> str:
    return STATUS_LABELS.get(str(value), str(value).replace("_", " ").title())


def _latest_goal(goals: pd.DataFrame, end: date) -> float | None:
    valid = goals[goals["data"].le(pd.Timestamp(end))] if not goals.empty else goals
    if valid.empty:
        return None
    return float(valid.sort_values("data").iloc[-1]["valor_meta"])


def _render_top_metrics(
    summary: pd.DataFrame,
    maintenance: pd.DataFrame,
    fuel: pd.DataFrame,
    usage: pd.DataFrame,
    goals: pd.DataFrame,
    end: date,
) -> None:
    total = len(summary)
    available = int((summary["status"] == "disponivel").sum())
    in_use = int((summary["status"] == "em_uso").sum())
    in_maintenance = int(
        ((summary["status"] == "em_manutencao") | (summary["manutencoes_abertas"] > 0)).sum()
    )
    availability = available / total * 100 if total else 0.0
    goal = _latest_goal(goals, end)
    direct_cost = float(maintenance["custo"].sum() + fuel["valor_total"].sum())
    usage_cost = float(usage["custo_utilizacao"].sum())
    hours = float(usage["horas_utilizadas"].sum())
    liters = float(fuel["litros"].sum())
    average_liter = float(fuel["valor_total"].sum()) / liters if liters else 0.0
    direct_cost_hour = direct_cost / hours if hours else 0.0

    first_row = st.columns(4)
    first_row[0].metric("Ativos analisados", total)
    first_row[1].metric("Disponíveis", available)
    first_row[2].metric("Em uso", in_use)
    first_row[3].metric("Em manutenção", in_maintenance, delta_color="inverse")

    second_row = st.columns(3)
    second_row[0].metric("Disponibilidade atual", f"{format_number_br(availability, 1)}%")
    second_row[1].metric(
        "Meta de disponibilidade",
        f"{format_number_br(goal, 1)}%" if goal is not None else "Não cadastrada",
    )
    second_row[2].metric("Valor de aquisição da frota", format_currency_br(float(summary["valor_aquisicao"].sum())))

    third_row = st.columns(3)
    third_row[0].metric("Custo direto no período", format_currency_br(direct_cost), help="Manutenções mais abastecimentos registrados no período.")
    third_row[1].metric("Custo apropriado de utilização", format_currency_br(usage_cost), help="Horas utilizadas multiplicadas pelo custo por hora informado. Não é somado ao custo direto para evitar dupla contagem.")
    third_row[2].metric("Custo direto por hora", format_currency_br(direct_cost_hour))

    fourth_row = st.columns(3)
    fourth_row[0].metric("Horas utilizadas", f"{format_number_br(hours, 1)} h")
    fourth_row[1].metric("Combustível consumido", f"{format_number_br(liters, 1)} L")
    fourth_row[2].metric("Preço médio por litro", format_currency_br(average_liter))


def _render_overview(summary: pd.DataFrame) -> None:
    left, right = st.columns(2)
    with left:
        st.subheader("Situação atual da frota")
        status = summary["status"].map(_status_label).value_counts()
        st.bar_chart(status, horizontal=True, height=290)
    with right:
        st.subheader("Ativos por tipo")
        types = summary["tipo"].fillna("Não informado").map(lambda value: str(value).title()).value_counts()
        st.bar_chart(types, horizontal=True, height=290)

    left, right = st.columns(2)
    with left:
        st.subheader("Valor de aquisição por tipo")
        values = summary.groupby(summary["tipo"].fillna("Não informado"))["valor_aquisicao"].sum().sort_values(ascending=False)
        values.index = values.index.map(lambda value: str(value).title())
        st.bar_chart(values, horizontal=True, height=300)
    with right:
        st.subheader("Alocação atual por obra")
        allocation = summary["obra_atual"].fillna("Sem obra atual").value_counts().head(12)
        st.bar_chart(allocation, horizontal=True, height=300)


def _fleet_ranking(summary: pd.DataFrame) -> pd.DataFrame:
    attention_order = {
        "Horímetro divergente": 0,
        "Em manutenção": 1,
        "Sem utilização há 90 dias": 2,
        "Sem utilização no período": 3,
        "Em uso": 4,
        "Disponível": 5,
        "Inativo": 6,
    }
    display = summary.copy()
    display["ordem_atencao"] = display["atencao"].map(attention_order).fillna(99)
    display = display.sort_values(["ordem_atencao", "horas_utilizadas", "identificacao"], ascending=[True, True, True])
    display["status"] = display["status"].map(_status_label)
    display["horas_utilizadas"] = display["horas_utilizadas"].map(lambda value: f"{format_number_br(value, 1)} h")
    display["litros"] = display["litros"].map(lambda value: f"{format_number_br(value, 1)} L")
    for column in ("custo_manutencao", "custo_combustivel", "custo_utilizacao", "custo_direto_hora"):
        display[column] = display[column].map(format_currency_br)
    display["ultima_utilizacao"] = display["ultima_utilizacao"].map(
        lambda value: value.strftime("%d/%m/%Y") if pd.notna(value) else "—"
    )
    return display[
        [
            "atencao", "identificacao", "tipo", "marca", "modelo", "status", "obra_atual",
            "horas_utilizadas", "litros", "custo_combustivel", "custo_manutencao",
            "custo_utilizacao", "custo_direto_hora", "ultima_utilizacao",
        ]
    ].rename(
        columns={
            "atencao": "Situação gerencial",
            "identificacao": "Ativo",
            "tipo": "Tipo",
            "marca": "Marca",
            "modelo": "Modelo",
            "status": "Status",
            "obra_atual": "Obra atual",
            "horas_utilizadas": "Horas no período",
            "litros": "Combustível",
            "custo_combustivel": "Custo de combustível",
            "custo_manutencao": "Custo de manutenção",
            "custo_utilizacao": "Custo de utilização",
            "custo_direto_hora": "Custo direto/hora",
            "ultima_utilizacao": "Última utilização",
        }
    )


def _render_usage(summary: pd.DataFrame, usage: pd.DataFrame) -> None:
    st.subheader("Ranking de utilização e produtividade")
    st.dataframe(_fleet_ranking(summary), width="stretch", hide_index=True)

    left, right = st.columns(2)
    with left:
        st.subheader("Horas utilizadas por ativo")
        hours = summary.set_index("identificacao")["horas_utilizadas"].sort_values(ascending=False)
        st.bar_chart(hours, horizontal=True, height=330)
    with right:
        st.subheader("Horas por obra")
        if usage.empty:
            st.info("Não existem utilizações no período selecionado.")
        else:
            by_work = usage.groupby(usage["obra"].fillna("Sem obra"))["horas_utilizadas"].sum().sort_values(ascending=False)
            st.bar_chart(by_work, horizontal=True, height=330)

    st.subheader("Histórico de utilizações")
    if usage.empty:
        st.info("Nenhuma utilização corresponde aos filtros selecionados.")
        return
    display = usage.copy()
    display["horas_utilizadas"] = display["horas_utilizadas"].map(lambda value: f"{format_number_br(value, 1)} h")
    display["custo_hora"] = display["custo_hora"].map(format_currency_br)
    display["custo_utilizacao"] = display["custo_utilizacao"].map(format_currency_br)
    st.dataframe(
        display[["data_utilizacao", "identificacao", "obra", "operador", "horas_utilizadas", "custo_hora", "custo_utilizacao"]].rename(
            columns={
                "data_utilizacao": "Data",
                "identificacao": "Ativo",
                "obra": "Obra",
                "operador": "Operador",
                "horas_utilizadas": "Horas",
                "custo_hora": "Custo por hora",
                "custo_utilizacao": "Custo apropriado",
            }
        ),
        width="stretch",
        hide_index=True,
        column_config={"Data": st.column_config.DateColumn(format="DD/MM/YYYY")},
    )


def _render_costs(summary: pd.DataFrame, maintenance: pd.DataFrame, fuel: pd.DataFrame, usage: pd.DataFrame) -> None:
    st.subheader("Evolução mensal dos custos")
    series = build_fleet_cost_series(maintenance, fuel, usage)
    if series.empty:
        st.info("Não existem custos no período selecionado.")
    else:
        _render_monthly_line_chart(
            series.set_index("data")[["Manutenção", "Combustível", "Custo de utilização"]],
            height=360,
        )
    st.caption("O custo de utilização é exibido separadamente dos desembolsos de manutenção e combustível para evitar dupla contagem.")

    left, right = st.columns(2)
    with left:
        st.subheader("Custo direto por ativo")
        direct = summary.set_index("identificacao")["custo_direto"].sort_values(ascending=False)
        st.bar_chart(direct, horizontal=True, height=340)
    with right:
        st.subheader("Combustível por ativo")
        liters = summary.set_index("identificacao")["litros"].sort_values(ascending=False)
        st.bar_chart(liters, horizontal=True, height=340)

    st.subheader("Abastecimentos")
    if fuel.empty:
        st.info("Nenhum abastecimento corresponde aos filtros selecionados.")
        return
    display = fuel.copy()
    display["litros"] = display["litros"].map(lambda value: f"{format_number_br(value, 3)} L")
    display["valor_total"] = display["valor_total"].map(format_currency_br)
    st.dataframe(
        display[["data_abastecimento", "identificacao", "obra", "responsavel", "litros", "valor_total", "quilometragem_horimetro"]].rename(
            columns={
                "data_abastecimento": "Data",
                "identificacao": "Ativo",
                "obra": "Obra",
                "responsavel": "Responsável",
                "litros": "Litros",
                "valor_total": "Valor",
                "quilometragem_horimetro": "Quilometragem/horímetro",
            }
        ),
        width="stretch",
        hide_index=True,
        column_config={"Data": st.column_config.DateColumn(format="DD/MM/YYYY")},
    )


def _render_maintenance(summary: pd.DataFrame, maintenance: pd.DataFrame) -> None:
    completed = maintenance[maintenance["status"] == "concluida"] if not maintenance.empty else maintenance
    open_records = maintenance[~maintenance["status"].isin(["concluida", "cancelada"])] if not maintenance.empty else maintenance
    duration = (completed["data_saida"] - completed["data_entrada"]).dt.days.dropna() if not completed.empty else pd.Series(dtype=float)
    average_duration = float(duration.mean()) if not duration.empty else 0.0
    assets_without_usage = int(summary["atencao"].isin(["Sem utilização no período", "Sem utilização há 90 dias"]).sum())
    columns = st.columns(4)
    columns[0].metric("Manutenções no período", len(maintenance))
    columns[1].metric("Manutenções abertas", len(open_records), delta_color="inverse")
    columns[2].metric("Tempo médio parado", f"{format_number_br(average_duration, 1)} dias")
    columns[3].metric("Ativos sem utilização", assets_without_usage, delta_color="inverse")

    st.subheader("Alertas operacionais")
    alerts = summary[summary["atencao"].isin(["Horímetro divergente", "Em manutenção", "Sem utilização no período", "Sem utilização há 90 dias"])]
    if alerts.empty:
        st.success("Nenhum alerta operacional foi identificado para o período e os filtros selecionados.")
    else:
        display_alerts = alerts[["atencao", "identificacao", "tipo", "status", "obra_atual", "horimetro_atual", "ultimo_horimetro_utilizacao"]].copy()
        display_alerts["status"] = display_alerts["status"].map(_status_label)
        st.dataframe(
            display_alerts.rename(
                columns={
                    "atencao": "Situação",
                    "identificacao": "Ativo",
                    "tipo": "Tipo",
                    "status": "Status",
                    "obra_atual": "Obra atual",
                    "horimetro_atual": "Horímetro atual",
                    "ultimo_horimetro_utilizacao": "Último horímetro utilizado",
                }
            ),
            width="stretch",
            hide_index=True,
        )

    st.subheader("Histórico de manutenções")
    if maintenance.empty:
        st.info("Nenhuma manutenção corresponde aos filtros selecionados.")
        return
    display = maintenance.copy()
    display["tipo"] = display["tipo"].map(lambda value: str(value).title())
    display["status"] = display["status"].map(_status_label)
    display["custo"] = display["custo"].map(format_currency_br)
    st.dataframe(
        display[["data_entrada", "data_saida", "identificacao", "tipo", "status", "descricao", "fornecedor", "obra", "custo"]].rename(
            columns={
                "data_entrada": "Entrada",
                "data_saida": "Saída",
                "identificacao": "Ativo",
                "tipo": "Tipo",
                "status": "Status",
                "descricao": "Serviço",
                "fornecedor": "Fornecedor",
                "obra": "Obra",
                "custo": "Custo",
            }
        ),
        width="stretch",
        hide_index=True,
        column_config={
            "Entrada": st.column_config.DateColumn(format="DD/MM/YYYY"),
            "Saída": st.column_config.DateColumn(format="DD/MM/YYYY"),
        },
    )


def render_fleet_dashboard(db: Session) -> None:
    st.header("Dashboard de Frota e Maquinário", anchor="dashboard-frota-maquinario")
    st.caption("Acompanhe disponibilidade, utilização, abastecimentos, manutenções, custos e produtividade dos ativos.")
    fleet, maintenance, fuel, usage, goals = load_fleet_dashboard_data(db)
    today = today_in_timezone(APP_SETTINGS.app_timezone)
    future_events = count_future_events(maintenance, fuel, usage, today)

    st.subheader("Filtros da análise")
    period = st.selectbox(
        "Período",
        ["Ano atual", "Últimos 90 dias", "Últimos 12 meses", "Todo o histórico", "Personalizado"],
        key="fleet_dashboard_period",
    )
    default_start, default_end = fleet_period_bounds(period, today, maintenance, fuel, usage)
    if period == "Personalizado":
        date_columns = st.columns(2)
        start = date_columns[0].date_input("Data inicial", value=default_start, key="fleet_dashboard_start")
        end = date_columns[1].date_input("Data final", value=default_end, max_value=today, key="fleet_dashboard_end")
    else:
        start, end = default_start, default_end
        st.caption(f"Período considerado: {start.strftime('%d/%m/%Y')} a {end.strftime('%d/%m/%Y')}")
    if start > end:
        st.error("A data inicial precisa ser anterior à data final.")
        return

    asset_options = sorted(fleet["identificacao"].dropna().astype(str).unique().tolist())
    type_options = sorted(fleet["tipo"].dropna().astype(str).unique().tolist())
    status_options = sorted(fleet["status"].dropna().astype(str).unique().tolist())
    works = pd.concat([maintenance["obra"], fuel["obra"], usage["obra"]], ignore_index=True)
    work_options = sorted(works.dropna().astype(str).unique().tolist())

    first_filters = st.columns(2)
    selected_assets = first_filters[0].multiselect(
        "Veículos e equipamentos", asset_options, placeholder="Todos os ativos", key="fleet_dashboard_assets"
    )
    selected_works = first_filters[1].multiselect(
        "Obras dos lançamentos", work_options, placeholder="Todas as obras", key="fleet_dashboard_works"
    )
    second_filters = st.columns(2)
    selected_types = second_filters[0].multiselect(
        "Tipos de ativo", type_options, placeholder="Todos os tipos", key="fleet_dashboard_types"
    )
    selected_status_labels = second_filters[1].multiselect(
        "Situações atuais",
        [_status_label(value) for value in status_options],
        placeholder="Todas as situações",
        key="fleet_dashboard_statuses",
    )
    reverse_status = {_status_label(value): value for value in status_options}
    selected_statuses = [reverse_status[label] for label in selected_status_labels]

    fleet, maintenance, fuel, usage = filter_fleet_data(
        fleet,
        maintenance,
        fuel,
        usage,
        start,
        end,
        selected_assets,
        selected_types,
        selected_statuses,
        selected_works,
    )
    if fleet.empty:
        st.info("Nenhum veículo ou equipamento corresponde aos filtros selecionados.")
        return
    summary = build_fleet_summary(fleet, maintenance, fuel, usage, today)

    _render_top_metrics(summary, maintenance, fuel, usage, goals, end)
    future_total = sum(future_events.values())
    if future_total:
        st.warning(
            f"Existem {future_total} lançamento(s) após {today.strftime('%d/%m/%Y')}: "
            f"{future_events['manutenções']} manutenção(ões), {future_events['abastecimentos']} abastecimento(s) e "
            f"{future_events['utilizações']} utilização(ões). Eles não são tratados como realizados nos indicadores atuais."
        )

    tabs = st.tabs(["Visão geral", "Utilização e produtividade", "Custos e abastecimentos", "Manutenções e alertas"])
    with tabs[0]:
        _render_overview(summary)
    with tabs[1]:
        _render_usage(summary, usage)
    with tabs[2]:
        _render_costs(summary, maintenance, fuel, usage)
    with tabs[3]:
        _render_maintenance(summary, maintenance)
