from __future__ import annotations

from datetime import date, datetime, time, timedelta
from typing import Any

import pandas as pd
import streamlit as st
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.core.config.settings import get_settings
from src.shared.utils.brazil_localization import format_currency_br, format_number_br, today_in_timezone
from src.ui.financial_dashboard import _render_monthly_line_chart


APP_SETTINGS = get_settings()


EMPLOYEES_SQL = """
SELECT
    funcionario.id AS funcionario_id,
    funcionario.nome,
    funcionario.data_nascimento,
    funcionario.email_corporativo,
    funcionario.telefone,
    funcionario.cargo,
    funcionario.setor,
    funcionario.data_admissao,
    funcionario.data_demissao,
    funcionario.salario_base::numeric AS salario_base,
    funcionario.status
FROM funcionarios funcionario
ORDER BY funcionario.nome
"""


TIME_RECORDS_SQL = """
SELECT
    ponto.id AS ponto_id,
    ponto.funcionario_id,
    funcionario.nome,
    funcionario.setor,
    ponto.data,
    ponto.entrada,
    ponto.saida_intervalo,
    ponto.retorno_intervalo,
    ponto.saida,
    ponto.observacao
FROM registro_ponto ponto
JOIN funcionarios funcionario ON funcionario.id = ponto.funcionario_id
ORDER BY ponto.data DESC, ponto.id DESC
"""


PAYROLL_SQL = """
SELECT
    folha.id AS folha_id,
    folha.funcionario_id,
    funcionario.nome,
    funcionario.setor,
    folha.competencia,
    folha.salario_bruto::numeric AS salario_bruto,
    folha.descontos::numeric AS descontos,
    folha.salario_liquido::numeric AS salario_liquido,
    folha.status
FROM folha_pagamento folha
JOIN funcionarios funcionario ON funcionario.id = folha.funcionario_id
ORDER BY folha.competencia DESC, folha.id DESC
"""


ALLOCATIONS_SQL = """
SELECT
    alocacao.id AS alocacao_id,
    alocacao.funcionario_id,
    funcionario.nome,
    funcionario.setor,
    alocacao.obra_id,
    obra.nome AS obra,
    alocacao.centro_custo_id,
    centro_custo.nome AS centro_custo,
    alocacao.funcao,
    alocacao.data_inicio,
    alocacao.data_fim,
    alocacao.custo_hora::numeric AS custo_hora,
    alocacao.ativo
FROM alocacoes_funcionario_obra alocacao
JOIN funcionarios funcionario ON funcionario.id = alocacao.funcionario_id
JOIN obras obra ON obra.id = alocacao.obra_id
LEFT JOIN centros_custo centro_custo ON centro_custo.id = alocacao.centro_custo_id
ORDER BY alocacao.data_inicio DESC, alocacao.id DESC
"""


EMPLOYEE_NUMERIC_COLUMNS = ("salario_base",)
PAYROLL_NUMERIC_COLUMNS = ("salario_bruto", "descontos", "salario_liquido")
ALLOCATION_NUMERIC_COLUMNS = ("custo_hora",)


STATUS_LABELS = {
    "ativo": "Ativo",
    "inativo": "Inativo",
    "afastado": "Afastado",
    "ferias": "Férias",
    "aberta": "Aberta",
    "pago": "Paga",
    "cancelada": "Cancelada",
}


def _query_frame(db: Session, sql: str) -> pd.DataFrame:
    return pd.read_sql_query(text(sql), db.connection())


def _time_value(value: Any) -> time | None:
    if value is None or pd.isna(value):
        return None
    if isinstance(value, time):
        return value
    parsed = pd.to_datetime(value, errors="coerce")
    return None if pd.isna(parsed) else parsed.time()


def calculate_worked_hours(
    entry: Any,
    break_start: Any,
    break_end: Any,
    exit_time: Any,
) -> float | None:
    entry_value = _time_value(entry)
    exit_value = _time_value(exit_time)
    if entry_value is None or exit_value is None:
        return None
    reference = date(2000, 1, 1)
    entry_dt = datetime.combine(reference, entry_value)
    exit_dt = datetime.combine(reference, exit_value)
    if exit_dt < entry_dt:
        exit_dt += timedelta(days=1)
    break_hours = 0.0
    break_start_value = _time_value(break_start)
    break_end_value = _time_value(break_end)
    if break_start_value is not None and break_end_value is not None:
        break_start_dt = datetime.combine(reference, break_start_value)
        break_end_dt = datetime.combine(reference, break_end_value)
        if break_end_dt < break_start_dt:
            break_end_dt += timedelta(days=1)
        break_hours = max((break_end_dt - break_start_dt).total_seconds() / 3600, 0.0)
    return max((exit_dt - entry_dt).total_seconds() / 3600 - break_hours, 0.0)


def load_hr_dashboard_data(
    db: Session,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    employees = _query_frame(db, EMPLOYEES_SQL)
    for column in ("data_nascimento", "data_admissao", "data_demissao"):
        employees[column] = pd.to_datetime(employees[column], errors="coerce")
    for column in EMPLOYEE_NUMERIC_COLUMNS:
        employees[column] = pd.to_numeric(employees[column], errors="coerce")

    time_records = _query_frame(db, TIME_RECORDS_SQL)
    time_records["data"] = pd.to_datetime(time_records["data"], errors="coerce")
    time_records["horas_trabalhadas"] = time_records.apply(
        lambda row: calculate_worked_hours(
            row["entrada"], row["saida_intervalo"], row["retorno_intervalo"], row["saida"]
        ),
        axis=1,
    )
    time_records["horas_extras_estimadas"] = time_records["horas_trabalhadas"].map(
        lambda value: max(float(value) - 8.0, 0.0) if pd.notna(value) else 0.0
    )
    time_records["jornada_incompleta"] = time_records["horas_trabalhadas"].isna()

    payroll = _query_frame(db, PAYROLL_SQL)
    payroll["competencia_data"] = pd.to_datetime(payroll["competencia"] + "-01", errors="coerce")
    for column in PAYROLL_NUMERIC_COLUMNS:
        payroll[column] = pd.to_numeric(payroll[column], errors="coerce").fillna(0.0)

    allocations = _query_frame(db, ALLOCATIONS_SQL)
    for column in ("data_inicio", "data_fim"):
        allocations[column] = pd.to_datetime(allocations[column], errors="coerce")
    for column in ALLOCATION_NUMERIC_COLUMNS:
        allocations[column] = pd.to_numeric(allocations[column], errors="coerce").fillna(0.0)
    return employees, time_records, payroll, allocations


def hr_period_bounds(
    period: str,
    today: date,
    employees: pd.DataFrame,
    time_records: pd.DataFrame,
    payroll: pd.DataFrame,
    allocations: pd.DataFrame,
) -> tuple[date, date]:
    if period == "Ano atual":
        return date(today.year, 1, 1), today
    if period == "Últimos 90 dias":
        return today - timedelta(days=89), today
    if period == "Últimos 12 meses":
        start = (pd.Timestamp(today).to_period("M").start_time - pd.DateOffset(months=11)).date()
        return start, today
    dates: list[pd.Timestamp] = []
    for frame, column in (
        (employees, "data_admissao"),
        (employees, "data_demissao"),
        (time_records, "data"),
        (payroll, "competencia_data"),
        (allocations, "data_inicio"),
    ):
        if not frame.empty:
            dates.extend(frame[column].dropna().tolist())
    historical_dates = [value for value in dates if value.date() <= today]
    if not historical_dates:
        return date(today.year, 1, 1), today
    return min(historical_dates).date(), today


def filter_hr_data(
    employees: pd.DataFrame,
    time_records: pd.DataFrame,
    payroll: pd.DataFrame,
    allocations: pd.DataFrame,
    start: date,
    end: date,
    selected_employees: list[str],
    selected_sectors: list[str],
    selected_roles: list[str],
    selected_statuses: list[str],
    selected_works: list[str],
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    filtered_employees = employees.copy()
    if selected_employees:
        filtered_employees = filtered_employees[filtered_employees["nome"].isin(selected_employees)]
    if selected_sectors:
        filtered_employees = filtered_employees[filtered_employees["setor"].isin(selected_sectors)]
    if selected_roles:
        filtered_employees = filtered_employees[filtered_employees["cargo"].isin(selected_roles)]
    if selected_statuses:
        filtered_employees = filtered_employees[filtered_employees["status"].isin(selected_statuses)]

    start_ts = pd.Timestamp(start)
    end_ts = pd.Timestamp(end)
    employment_overlap = (
        (filtered_employees["data_admissao"].isna() | filtered_employees["data_admissao"].le(end_ts))
        & (filtered_employees["data_demissao"].isna() | filtered_employees["data_demissao"].ge(start_ts))
    )
    filtered_employees = filtered_employees[employment_overlap]
    employee_ids = filtered_employees["funcionario_id"].dropna().astype(int).tolist()

    filtered_time = time_records[
        time_records["funcionario_id"].isin(employee_ids)
        & time_records["data"].between(start_ts, end_ts, inclusive="both")
    ].copy()
    start_month = start_ts.to_period("M").start_time
    end_month = end_ts.to_period("M").start_time
    filtered_payroll = payroll[
        payroll["funcionario_id"].isin(employee_ids)
        & payroll["competencia_data"].between(start_month, end_month, inclusive="both")
    ].copy()
    filtered_allocations = allocations[
        allocations["funcionario_id"].isin(employee_ids)
        & allocations["data_inicio"].le(end_ts)
        & (allocations["data_fim"].isna() | allocations["data_fim"].ge(start_ts))
    ].copy()

    if selected_works:
        filtered_allocations = filtered_allocations[filtered_allocations["obra"].isin(selected_works)]
        work_employee_ids = filtered_allocations["funcionario_id"].dropna().astype(int).unique().tolist()
        filtered_employees = filtered_employees[filtered_employees["funcionario_id"].isin(work_employee_ids)]
        filtered_time = filtered_time[filtered_time["funcionario_id"].isin(work_employee_ids)]
        filtered_payroll = filtered_payroll[filtered_payroll["funcionario_id"].isin(work_employee_ids)]
    return filtered_employees, filtered_time, filtered_payroll, filtered_allocations


def headcount_at(employees: pd.DataFrame, reference_date: date) -> int:
    if employees.empty:
        return 0
    reference = pd.Timestamp(reference_date)
    valid_admission = employees["data_admissao"].notna() & employees["data_admissao"].le(reference)
    not_dismissed = employees["data_demissao"].isna() | employees["data_demissao"].gt(reference)
    return int((valid_admission & not_dismissed).sum())


def build_headcount_series(employees: pd.DataFrame, start: date, end: date) -> pd.DataFrame:
    months = pd.date_range(pd.Timestamp(start).to_period("M").start_time, pd.Timestamp(end), freq="MS")
    rows: list[dict[str, Any]] = []
    for month in months:
        month_end = min((month + pd.offsets.MonthEnd(0)).date(), end)
        rows.append(
            {
                "data": month,
                "Quadro de funcionários": headcount_at(employees, month_end),
                "Admissões": int(employees["data_admissao"].dt.to_period("M").eq(month.to_period("M")).sum()),
                "Desligamentos": int(employees["data_demissao"].dt.to_period("M").eq(month.to_period("M")).sum()),
            }
        )
    return pd.DataFrame(rows)


def build_payroll_series(payroll: pd.DataFrame) -> pd.DataFrame:
    columns = ["data", "Salário bruto", "Descontos", "Salário líquido"]
    if payroll.empty or payroll["competencia_data"].dropna().empty:
        return pd.DataFrame(columns=columns)
    monthly = (
        payroll.dropna(subset=["competencia_data"])
        .groupby("competencia_data", as_index=False)[["salario_bruto", "descontos", "salario_liquido"]]
        .sum()
        .rename(
            columns={
                "competencia_data": "data",
                "salario_bruto": "Salário bruto",
                "descontos": "Descontos",
                "salario_liquido": "Salário líquido",
            }
        )
    )
    calendar = pd.DataFrame({"data": pd.date_range(monthly["data"].min(), monthly["data"].max(), freq="MS")})
    return calendar.merge(monthly, on="data", how="left").fillna(0.0)[columns]


def employee_attention(row: pd.Series) -> str:
    if pd.isna(row.get("data_admissao")) or not str(row.get("cargo") or "").strip() or not str(row.get("setor") or "").strip():
        return "Cadastro incompleto"
    if float(row.get("jornadas_incompletas", 0)) > 0:
        return "Jornada incompleta"
    if float(row.get("folhas", 0)) == 0:
        return "Sem folha no período"
    if float(row.get("registros_ponto", 0)) == 0:
        return "Sem ponto no período"
    if str(row.get("status")) == "ativo" and float(row.get("alocacoes", 0)) == 0:
        return "Sem alocação no período"
    return "Regular"


def build_employee_summary(
    employees: pd.DataFrame,
    time_records: pd.DataFrame,
    payroll: pd.DataFrame,
    allocations: pd.DataFrame,
) -> pd.DataFrame:
    result = employees.copy()
    time_group = time_records.groupby("funcionario_id", as_index=False).agg(
        registros_ponto=("ponto_id", "count"),
        horas_trabalhadas=("horas_trabalhadas", "sum"),
        horas_extras_estimadas=("horas_extras_estimadas", "sum"),
        jornadas_incompletas=("jornada_incompleta", "sum"),
        ultimo_ponto=("data", "max"),
    )
    payroll_group = payroll.groupby("funcionario_id", as_index=False).agg(
        folhas=("folha_id", "count"),
        salario_bruto_periodo=("salario_bruto", "sum"),
        descontos_periodo=("descontos", "sum"),
        salario_liquido_periodo=("salario_liquido", "sum"),
        folhas_abertas=("status", lambda values: int((~values.isin(["pago", "cancelada"])).sum())),
        ultima_competencia=("competencia_data", "max"),
    )
    allocation_group = allocations.groupby("funcionario_id", as_index=False).agg(
        alocacoes=("alocacao_id", "count"),
        obras_alocadas=("obra", lambda values: ", ".join(sorted(set(values.dropna().astype(str))))),
        custo_hora_alocado=("custo_hora", "sum"),
    )
    for grouped in (time_group, payroll_group, allocation_group):
        result = result.merge(grouped, on="funcionario_id", how="left")
    numeric_columns = (
        "registros_ponto",
        "horas_trabalhadas",
        "horas_extras_estimadas",
        "jornadas_incompletas",
        "folhas",
        "salario_bruto_periodo",
        "descontos_periodo",
        "salario_liquido_periodo",
        "folhas_abertas",
        "alocacoes",
        "custo_hora_alocado",
    )
    for column in numeric_columns:
        result[column] = pd.to_numeric(result[column], errors="coerce").fillna(0.0)
    result["obras_alocadas"] = result["obras_alocadas"].fillna("")
    result["atencao"] = result.apply(employee_attention, axis=1)
    return result


def count_future_hr_events(
    employees: pd.DataFrame,
    time_records: pd.DataFrame,
    payroll: pd.DataFrame,
    allocations: pd.DataFrame,
    today: date,
) -> dict[str, int]:
    reference = pd.Timestamp(today)
    current_month = reference.to_period("M").start_time
    return {
        "admissões": int(employees["data_admissao"].gt(reference).sum()),
        "registros de ponto": int(time_records["data"].gt(reference).sum()),
        "folhas": int(payroll["competencia_data"].gt(current_month).sum()),
        "alocações": int(allocations["data_inicio"].gt(reference).sum()),
    }


def _status_label(value: Any) -> str:
    return STATUS_LABELS.get(str(value), str(value).replace("_", " ").title())


def _format_time(value: Any) -> str:
    parsed = _time_value(value)
    return parsed.strftime("%H:%M") if parsed else "—"


def _render_top_metrics(
    employees: pd.DataFrame,
    time_records: pd.DataFrame,
    payroll: pd.DataFrame,
    allocations: pd.DataFrame,
    start: date,
    end: date,
) -> None:
    active = int((employees["status"] == "ativo").sum())
    admissions = int(employees["data_admissao"].between(pd.Timestamp(start), pd.Timestamp(end), inclusive="both").sum())
    dismissals = int(employees["data_demissao"].between(pd.Timestamp(start), pd.Timestamp(end), inclusive="both").sum())
    headcount = headcount_at(employees, end)
    open_payroll = payroll[~payroll["status"].isin(["pago", "cancelada"])]
    hours = float(time_records["horas_trabalhadas"].sum())
    complete_shifts = int(time_records["horas_trabalhadas"].notna().sum())
    average_hours = hours / complete_shifts if complete_shifts else 0.0

    first_row = st.columns(4)
    first_row[0].metric("Funcionários no recorte", len(employees))
    first_row[1].metric("Ativos no cadastro", active)
    first_row[2].metric("Admissões no período", admissions)
    first_row[3].metric("Desligamentos no período", dismissals, delta_color="inverse")

    second_row = st.columns(4)
    second_row[0].metric(
        "Quadro no encerramento",
        headcount,
        help="Considera admissões e desligamentos com datas preenchidas até o fim do período.",
    )
    second_row[1].metric("Setores representados", int(employees["setor"].dropna().nunique()))
    second_row[2].metric("Obras com equipe", int(allocations["obra_id"].dropna().nunique()))
    second_row[3].metric("Alocações no período", len(allocations))

    third_row = st.columns(4)
    third_row[0].metric("Folha bruta", format_currency_br(float(payroll["salario_bruto"].sum())))
    third_row[1].metric("Descontos", format_currency_br(float(payroll["descontos"].sum())))
    third_row[2].metric("Folha líquida", format_currency_br(float(payroll["salario_liquido"].sum())))
    third_row[3].metric(
        "Folha em aberto",
        format_currency_br(float(open_payroll["salario_liquido"].sum())),
        help=f"{len(open_payroll)} lançamento(s) ainda não marcados como pagos ou cancelados.",
    )

    fourth_row = st.columns(4)
    fourth_row[0].metric("Horas registradas", f"{format_number_br(hours, 1)} h")
    fourth_row[1].metric("Média por jornada", f"{format_number_br(average_hours, 1)} h")
    fourth_row[2].metric(
        "Horas acima de 8h",
        f"{format_number_br(float(time_records['horas_extras_estimadas'].sum()), 1)} h",
        help="Estimativa gerencial. A jornada contratual e as regras de horas extras não estão cadastradas no banco.",
    )
    fourth_row[3].metric(
        "Jornadas incompletas",
        int(time_records["jornada_incompleta"].sum()),
        delta_color="inverse",
    )


def _employee_table(summary: pd.DataFrame) -> pd.DataFrame:
    display = summary.copy()
    attention_order = {
        "Cadastro incompleto": 0,
        "Jornada incompleta": 1,
        "Sem folha no período": 2,
        "Sem ponto no período": 3,
        "Sem alocação no período": 4,
        "Regular": 5,
    }
    display["ordem"] = display["atencao"].map(attention_order).fillna(99)
    display = display.sort_values(["ordem", "nome"])
    display["status"] = display["status"].map(_status_label)
    display["salario_base"] = display["salario_base"].map(lambda value: format_currency_br(value) if pd.notna(value) else "—")
    display["horas_trabalhadas"] = display["horas_trabalhadas"].map(lambda value: f"{format_number_br(value, 1)} h")
    display["salario_liquido_periodo"] = display["salario_liquido_periodo"].map(format_currency_br)
    display["ultimo_ponto"] = display["ultimo_ponto"].map(
        lambda value: value.strftime("%d/%m/%Y") if pd.notna(value) else "—"
    )
    return display[
        [
            "atencao",
            "nome",
            "cargo",
            "setor",
            "status",
            "salario_base",
            "horas_trabalhadas",
            "salario_liquido_periodo",
            "obras_alocadas",
            "ultimo_ponto",
        ]
    ].rename(
        columns={
            "atencao": "Situação gerencial",
            "nome": "Funcionário",
            "cargo": "Cargo",
            "setor": "Setor",
            "status": "Status",
            "salario_base": "Salário-base",
            "horas_trabalhadas": "Horas no período",
            "salario_liquido_periodo": "Folha líquida no período",
            "obras_alocadas": "Obras vinculadas",
            "ultimo_ponto": "Último ponto",
        }
    )


def _render_overview(summary: pd.DataFrame, start: date, end: date) -> None:
    st.subheader("Evolução do quadro de funcionários")
    series = build_headcount_series(summary, start, end)
    if series.empty:
        st.info("Não há datas de admissão suficientes para calcular a evolução do quadro.")
    else:
        st.line_chart(series.set_index("data")[["Quadro de funcionários"]], height=340)
        movements = series.set_index("data")[["Admissões", "Desligamentos"]]
        if movements.to_numpy().sum() > 0:
            st.caption("Admissões e desligamentos por mês")
            st.bar_chart(movements, height=280)

    left, right = st.columns(2)
    with left:
        st.subheader("Funcionários por setor")
        by_sector = summary["setor"].fillna("Não informado").value_counts()
        st.bar_chart(by_sector, horizontal=True, height=300)
    with right:
        st.subheader("Funcionários por cargo")
        by_role = summary["cargo"].fillna("Não informado").value_counts().head(12)
        st.bar_chart(by_role, horizontal=True, height=300)

    st.subheader("Resumo dos funcionários")
    st.dataframe(_employee_table(summary), width="stretch", hide_index=True)


def _render_time_records(summary: pd.DataFrame, time_records: pd.DataFrame) -> None:
    st.info(
        "A ausência de um registro de ponto não é classificada como falta. Para calcular faltas com segurança, "
        "o sistema precisaria também de escala prevista, feriados, férias e afastamentos."
    )
    left, right = st.columns(2)
    with left:
        st.subheader("Horas registradas por funcionário")
        hours = summary.set_index("nome")["horas_trabalhadas"].sort_values(ascending=False)
        if float(hours.sum()) == 0:
            st.info("Não existem horas registradas no período.")
        else:
            st.bar_chart(hours, horizontal=True, height=350)
    with right:
        st.subheader("Média de horas por jornada")
        averages = summary.copy()
        averages["media"] = averages.apply(
            lambda row: row["horas_trabalhadas"] / row["registros_ponto"] if row["registros_ponto"] else 0.0,
            axis=1,
        )
        averages = averages.set_index("nome")["media"].sort_values(ascending=False)
        if float(averages.sum()) == 0:
            st.info("Não há jornadas completas para calcular a média.")
        else:
            st.bar_chart(averages, horizontal=True, height=350)

    st.subheader("Histórico de registros de ponto")
    if time_records.empty:
        st.info("Nenhum registro de ponto corresponde aos filtros selecionados.")
        return
    display = time_records.sort_values(["data", "ponto_id"], ascending=[False, False]).copy()
    for column in ("entrada", "saida_intervalo", "retorno_intervalo", "saida"):
        display[column] = display[column].map(_format_time)
    display["horas_trabalhadas"] = display["horas_trabalhadas"].map(
        lambda value: f"{format_number_br(value, 1)} h" if pd.notna(value) else "Incompleta"
    )
    st.dataframe(
        display[
            [
                "data",
                "nome",
                "setor",
                "entrada",
                "saida_intervalo",
                "retorno_intervalo",
                "saida",
                "horas_trabalhadas",
                "observacao",
            ]
        ].rename(
            columns={
                "data": "Data",
                "nome": "Funcionário",
                "setor": "Setor",
                "entrada": "Entrada",
                "saida_intervalo": "Saída intervalo",
                "retorno_intervalo": "Retorno intervalo",
                "saida": "Saída",
                "horas_trabalhadas": "Horas trabalhadas",
                "observacao": "Observação",
            }
        ),
        width="stretch",
        hide_index=True,
        column_config={"Data": st.column_config.DateColumn(format="DD/MM/YYYY")},
    )


def _render_payroll(employees: pd.DataFrame, payroll: pd.DataFrame) -> None:
    st.subheader("Evolução mensal da folha")
    series = build_payroll_series(payroll)
    if series.empty:
        st.info("Não existem folhas de pagamento no período selecionado.")
    else:
        _render_monthly_line_chart(
            series.set_index("data")[["Salário bruto", "Descontos", "Salário líquido"]],
            height=370,
        )
        latest = payroll["competencia_data"].max()
        if pd.notna(latest):
            st.caption(f"Última competência encontrada nos filtros: {latest.strftime('%m/%Y')}.")

    st.caption(
        "O salário-base mensal é uma referência cadastral e não é somado à folha realizada, evitando dupla contagem."
    )
    left, right = st.columns(2)
    with left:
        st.subheader("Salário-base mensal por setor")
        base_by_sector = employees.groupby(employees["setor"].fillna("Não informado"))["salario_base"].sum()
        if float(base_by_sector.sum()) == 0:
            st.info("Não existem salários-base preenchidos para o recorte.")
        else:
            st.bar_chart(base_by_sector.sort_values(ascending=False), horizontal=True, height=330)
    with right:
        st.subheader("Folhas por situação")
        if payroll.empty:
            st.info("Não existem folhas no período selecionado.")
        else:
            by_status = payroll.groupby(payroll["status"].map(_status_label))["salario_liquido"].sum()
            st.bar_chart(by_status.sort_values(ascending=False), horizontal=True, height=330)

    st.subheader("Histórico da folha de pagamento")
    if payroll.empty:
        st.info("Nenhuma folha corresponde aos filtros selecionados.")
        return
    display = payroll.sort_values(["competencia_data", "folha_id"], ascending=[False, False]).copy()
    display["competencia"] = display["competencia_data"].map(lambda value: value.strftime("%m/%Y"))
    display["status"] = display["status"].map(_status_label)
    for column in PAYROLL_NUMERIC_COLUMNS:
        display[column] = display[column].map(format_currency_br)
    st.dataframe(
        display[
            ["competencia", "nome", "setor", "status", "salario_bruto", "descontos", "salario_liquido"]
        ].rename(
            columns={
                "competencia": "Competência",
                "nome": "Funcionário",
                "setor": "Setor",
                "status": "Situação",
                "salario_bruto": "Salário bruto",
                "descontos": "Descontos",
                "salario_liquido": "Salário líquido",
            }
        ),
        width="stretch",
        hide_index=True,
    )


def _render_teams_and_alerts(summary: pd.DataFrame, allocations: pd.DataFrame) -> None:
    st.subheader("Distribuição das equipes por obra")
    if allocations.empty:
        st.info("Nenhuma alocação corresponde aos filtros selecionados.")
    else:
        by_work = allocations.groupby("obra", as_index=False).agg(
            funcionarios=("funcionario_id", "nunique"),
            alocacoes=("alocacao_id", "count"),
            custo_hora_potencial=("custo_hora", "sum"),
        )
        by_work = by_work.sort_values(["funcionarios", "obra"], ascending=[False, True])
        chart = by_work.set_index("obra")["funcionarios"]
        st.bar_chart(chart, horizontal=True, height=360)
        display = by_work.copy()
        display["custo_hora_potencial"] = display["custo_hora_potencial"].map(format_currency_br)
        st.dataframe(
            display.rename(
                columns={
                    "obra": "Obra",
                    "funcionarios": "Funcionários",
                    "alocacoes": "Alocações",
                    "custo_hora_potencial": "Custo-hora potencial",
                }
            ),
            width="stretch",
            hide_index=True,
        )
        st.caption(
            "O custo-hora potencial representa a capacidade cadastrada das equipes. Ele não é custo realizado, "
            "pois o registro de ponto ainda não identifica em qual obra cada hora foi trabalhada."
        )

    st.subheader("Pontos de atenção")
    alerts = summary[summary["atencao"] != "Regular"]
    if alerts.empty:
        st.success("Nenhuma inconsistência foi identificada para o período e os filtros selecionados.")
    else:
        display = alerts[
            ["atencao", "nome", "cargo", "setor", "status", "registros_ponto", "folhas", "alocacoes"]
        ].copy()
        display["status"] = display["status"].map(_status_label)
        st.dataframe(
            display.rename(
                columns={
                    "atencao": "Situação",
                    "nome": "Funcionário",
                    "cargo": "Cargo",
                    "setor": "Setor",
                    "status": "Status",
                    "registros_ponto": "Registros de ponto",
                    "folhas": "Folhas",
                    "alocacoes": "Alocações",
                }
            ),
            width="stretch",
            hide_index=True,
        )

    st.subheader("Alocações das equipes")
    if allocations.empty:
        return
    display = allocations.sort_values(["data_inicio", "alocacao_id"], ascending=[False, False]).copy()
    display["custo_hora"] = display["custo_hora"].map(format_currency_br)
    display["ativo"] = display["ativo"].map(lambda value: "Ativa" if value else "Encerrada")
    st.dataframe(
        display[
            ["nome", "setor", "obra", "funcao", "centro_custo", "data_inicio", "data_fim", "custo_hora", "ativo"]
        ].rename(
            columns={
                "nome": "Funcionário",
                "setor": "Setor",
                "obra": "Obra",
                "funcao": "Função na equipe",
                "centro_custo": "Centro de custo",
                "data_inicio": "Início",
                "data_fim": "Fim",
                "custo_hora": "Custo por hora",
                "ativo": "Situação",
            }
        ),
        width="stretch",
        hide_index=True,
        column_config={
            "Início": st.column_config.DateColumn(format="DD/MM/YYYY"),
            "Fim": st.column_config.DateColumn(format="DD/MM/YYYY"),
        },
    )


def render_hr_dashboard(db: Session) -> None:
    st.header("Dashboard de Recursos Humanos", anchor="dashboard-recursos-humanos")
    st.caption("Acompanhe quadro de pessoal, admissões, jornada, folha de pagamento e alocação das equipes.")
    employees, time_records, payroll, allocations = load_hr_dashboard_data(db)
    today = today_in_timezone(APP_SETTINGS.app_timezone)
    future_events = count_future_hr_events(employees, time_records, payroll, allocations, today)

    st.subheader("Filtros da análise")
    period = st.selectbox(
        "Período",
        ["Ano atual", "Últimos 90 dias", "Últimos 12 meses", "Todo o histórico", "Personalizado"],
        index=3,
        key="hr_dashboard_period",
    )
    default_start, default_end = hr_period_bounds(period, today, employees, time_records, payroll, allocations)
    if period == "Personalizado":
        date_columns = st.columns(2)
        start = date_columns[0].date_input(
            "Data inicial", value=default_start, max_value=today, key="hr_dashboard_start"
        )
        end = date_columns[1].date_input(
            "Data final", value=default_end, max_value=today, key="hr_dashboard_end"
        )
    else:
        start, end = default_start, default_end
        st.caption(f"Período considerado: {start.strftime('%d/%m/%Y')} a {end.strftime('%d/%m/%Y')}")
    if start > end:
        st.error("A data inicial precisa ser anterior à data final.")
        return

    employee_options = sorted(employees["nome"].dropna().astype(str).unique().tolist())
    sector_options = sorted(employees["setor"].dropna().astype(str).unique().tolist())
    role_options = sorted(employees["cargo"].dropna().astype(str).unique().tolist())
    status_options = sorted(employees["status"].dropna().astype(str).unique().tolist())
    work_options = sorted(allocations["obra"].dropna().astype(str).unique().tolist())

    first_filters = st.columns(2)
    selected_employees = first_filters[0].multiselect(
        "Funcionários", employee_options, placeholder="Todos os funcionários", key="hr_dashboard_employees"
    )
    selected_works = first_filters[1].multiselect(
        "Obras das equipes", work_options, placeholder="Todas as obras", key="hr_dashboard_works"
    )
    second_filters = st.columns(3)
    selected_sectors = second_filters[0].multiselect(
        "Setores", sector_options, placeholder="Todos os setores", key="hr_dashboard_sectors"
    )
    selected_roles = second_filters[1].multiselect(
        "Cargos", role_options, placeholder="Todos os cargos", key="hr_dashboard_roles"
    )
    selected_status_labels = second_filters[2].multiselect(
        "Situações atuais",
        [_status_label(value) for value in status_options],
        placeholder="Todas as situações",
        key="hr_dashboard_statuses",
    )
    reverse_status = {_status_label(value): value for value in status_options}
    selected_statuses = [reverse_status[label] for label in selected_status_labels]

    employees, time_records, payroll, allocations = filter_hr_data(
        employees,
        time_records,
        payroll,
        allocations,
        start,
        end,
        selected_employees,
        selected_sectors,
        selected_roles,
        selected_statuses,
        selected_works,
    )
    if employees.empty:
        st.info("Nenhum funcionário corresponde aos filtros selecionados.")
        return
    summary = build_employee_summary(employees, time_records, payroll, allocations)

    _render_top_metrics(employees, time_records, payroll, allocations, start, end)
    future_total = sum(future_events.values())
    if future_total:
        st.warning(
            f"Existem {future_total} lançamento(s) futuros: {future_events['admissões']} admissão(ões), "
            f"{future_events['registros de ponto']} registro(s) de ponto, {future_events['folhas']} folha(s) e "
            f"{future_events['alocações']} alocação(ões). Eles não são tratados como realizados nos indicadores atuais."
        )
    missing_admission = int(employees["data_admissao"].isna().sum())
    if missing_admission:
        st.warning(
            f"{missing_admission} funcionário(s) não possuem data de admissão e, por isso, não entram no cálculo "
            "histórico do quadro de pessoal. O cadastro continua visível nos demais indicadores."
        )

    tabs = st.tabs(["Visão geral", "Jornada e ponto", "Folha e custos", "Equipes e alertas"])
    with tabs[0]:
        _render_overview(summary, start, end)
    with tabs[1]:
        _render_time_records(summary, time_records)
    with tabs[2]:
        _render_payroll(employees, payroll)
    with tabs[3]:
        _render_teams_and_alerts(summary, allocations)
