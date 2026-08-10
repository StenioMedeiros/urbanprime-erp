from __future__ import annotations

from datetime import date
from typing import Any, Callable

import altair as alt
import pandas as pd
import streamlit as st
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.core.config.settings import get_settings
from src.shared.utils.brazil_localization import (
    MONTH_NAMES_PT_BR,
    SHORT_MONTH_NAMES_PT_BR,
    SHORT_WEEKDAY_NAMES_PT_BR,
    WEEKDAY_NAMES_PT_BR,
    format_currency_br,
    format_number_br,
    today_in_timezone,
)


APP_SETTINGS = get_settings()


EXPENSES_SQL = """
SELECT
    ac.data_apropriacao AS data,
    ac.competencia,
    'Custos apropriados'::text AS origem,
    COALESCE(cf.nome, 'Outras despesas')::text AS categoria,
    'Despesa operacional'::text AS natureza,
    ac.descricao,
    ac.valor_total::numeric AS valor,
    o.id AS obra_id,
    o.nome::text AS obra,
    p.id AS projeto_id,
    p.nome::text AS projeto,
    cl.id AS cliente_id,
    cl.nome::text AS cliente
FROM apropriacoes_custo ac
JOIN obras o ON o.id = ac.obra_id
LEFT JOIN categorias_financeiras cf ON cf.id = ac.categoria_financeira_id
LEFT JOIN projetos p ON p.id = o.projeto_id
LEFT JOIN contratos ct ON ct.id = COALESCE(o.contrato_id, p.contrato_id)
LEFT JOIN clientes cl ON cl.id = ct.cliente_id

UNION ALL

SELECT
    make_date(SUBSTRING(fp.competencia, 1, 4)::integer, SUBSTRING(fp.competencia, 6, 2)::integer, 1) AS data,
    fp.competencia,
    'Folha de pagamento'::text AS origem,
    'Pessoal e folha de pagamento'::text AS categoria,
    'Despesa operacional'::text AS natureza,
    ('Salário bruto de ' || f.nome)::text AS descricao,
    fp.salario_bruto::numeric AS valor,
    o.id AS obra_id,
    o.nome::text AS obra,
    p.id AS projeto_id,
    p.nome::text AS projeto,
    cl.id AS cliente_id,
    cl.nome::text AS cliente
FROM folha_pagamento fp
JOIN funcionarios f ON f.id = fp.funcionario_id
LEFT JOIN LATERAL (
    SELECT a.obra_id
    FROM alocacoes_funcionario_obra a
    WHERE a.funcionario_id = fp.funcionario_id
      AND a.data_inicio <= (make_date(SUBSTRING(fp.competencia, 1, 4)::integer, SUBSTRING(fp.competencia, 6, 2)::integer, 1) + INTERVAL '1 month - 1 day')::date
      AND (a.data_fim IS NULL OR a.data_fim >= make_date(SUBSTRING(fp.competencia, 1, 4)::integer, SUBSTRING(fp.competencia, 6, 2)::integer, 1))
    ORDER BY a.ativo DESC, a.data_inicio DESC
    LIMIT 1
) allocation ON TRUE
LEFT JOIN obras o ON o.id = allocation.obra_id
LEFT JOIN projetos p ON p.id = o.projeto_id
LEFT JOIN contratos ct ON ct.id = COALESCE(o.contrato_id, p.contrato_id)
LEFT JOIN clientes cl ON cl.id = ct.cliente_id

UNION ALL

SELECT
    mf.data_entrada AS data,
    TO_CHAR(mf.data_entrada, 'YYYY-MM') AS competencia,
    'Manutenção da frota'::text AS origem,
    'Manutenção de máquinas e veículos'::text AS categoria,
    'Despesa operacional'::text AS natureza,
    mf.descricao::text,
    mf.custo::numeric AS valor,
    o.id AS obra_id,
    o.nome::text AS obra,
    p.id AS projeto_id,
    p.nome::text AS projeto,
    cl.id AS cliente_id,
    cl.nome::text AS cliente
FROM manutencoes_frota mf
LEFT JOIN obras o ON o.id = mf.obra_id
LEFT JOIN projetos p ON p.id = o.projeto_id
LEFT JOIN contratos ct ON ct.id = COALESCE(o.contrato_id, p.contrato_id)
LEFT JOIN clientes cl ON cl.id = ct.cliente_id

UNION ALL

SELECT
    af.data_abastecimento AS data,
    TO_CHAR(af.data_abastecimento, 'YYYY-MM') AS competencia,
    'Abastecimento da frota'::text AS origem,
    'Combustíveis'::text AS categoria,
    'Despesa operacional'::text AS natureza,
    COALESCE(af.observacao, 'Abastecimento de máquina ou veículo')::text AS descricao,
    af.valor_total::numeric AS valor,
    o.id AS obra_id,
    o.nome::text AS obra,
    p.id AS projeto_id,
    p.nome::text AS projeto,
    cl.id AS cliente_id,
    cl.nome::text AS cliente
FROM abastecimentos_frota af
LEFT JOIN obras o ON o.id = af.obra_id
LEFT JOIN projetos p ON p.id = o.projeto_id
LEFT JOIN contratos ct ON ct.id = COALESCE(o.contrato_id, p.contrato_id)
LEFT JOIN clientes cl ON cl.id = ct.cliente_id

UNION ALL

SELECT
    uf.data_utilizacao AS data,
    TO_CHAR(uf.data_utilizacao, 'YYYY-MM') AS competencia,
    'Uso de máquinas e veículos'::text AS origem,
    'Custo operacional de máquinas'::text AS categoria,
    'Despesa operacional'::text AS natureza,
    COALESCE(uf.observacao, 'Uso de máquina ou veículo')::text AS descricao,
    (uf.horas_utilizadas * uf.custo_hora)::numeric AS valor,
    o.id AS obra_id,
    o.nome::text AS obra,
    p.id AS projeto_id,
    p.nome::text AS projeto,
    cl.id AS cliente_id,
    cl.nome::text AS cliente
FROM utilizacoes_frota uf
LEFT JOIN obras o ON o.id = uf.obra_id
LEFT JOIN projetos p ON p.id = o.projeto_id
LEFT JOIN contratos ct ON ct.id = COALESCE(o.contrato_id, p.contrato_id)
LEFT JOIN clientes cl ON cl.id = ct.cliente_id

UNION ALL

SELECT
    fr.data_aquisicao AS data,
    TO_CHAR(fr.data_aquisicao, 'YYYY-MM') AS competencia,
    'Aquisição de máquinas e veículos'::text AS origem,
    'Investimentos em máquinas'::text AS categoria,
    'Investimento'::text AS natureza,
    ('Aquisição: ' || fr.identificacao || COALESCE(' - ' || fr.marca || ' ' || fr.modelo, ''))::text AS descricao,
    fr.valor_aquisicao::numeric AS valor,
    o.id AS obra_id,
    o.nome::text AS obra,
    p.id AS projeto_id,
    p.nome::text AS projeto,
    cl.id AS cliente_id,
    cl.nome::text AS cliente
FROM frotas fr
LEFT JOIN obras o ON o.id = fr.obra_id
LEFT JOIN projetos p ON p.id = o.projeto_id
LEFT JOIN contratos ct ON ct.id = COALESCE(o.contrato_id, p.contrato_id)
LEFT JOIN clientes cl ON cl.id = ct.cliente_id
WHERE fr.data_aquisicao IS NOT NULL AND fr.valor_aquisicao IS NOT NULL

UNION ALL

SELECT
    COALESCE(cp.data_competencia, cp.data_pagamento, cp.data_vencimento) AS data,
    TO_CHAR(COALESCE(cp.data_competencia, cp.data_pagamento, cp.data_vencimento), 'YYYY-MM') AS competencia,
    'Contas a pagar'::text AS origem,
    COALESCE(cf.nome, 'Outras despesas')::text AS categoria,
    'Despesa operacional'::text AS natureza,
    cp.descricao::text,
    cp.valor::numeric AS valor,
    o.id AS obra_id,
    o.nome::text AS obra,
    p.id AS projeto_id,
    p.nome::text AS projeto,
    cl.id AS cliente_id,
    cl.nome::text AS cliente
FROM contas_pagar cp
LEFT JOIN categorias_financeiras cf ON cf.id = cp.categoria_financeira_id
LEFT JOIN obras o ON o.id = cp.obra_id
LEFT JOIN projetos p ON p.id = o.projeto_id
LEFT JOIN contratos ct ON ct.id = COALESCE(o.contrato_id, p.contrato_id)
LEFT JOIN clientes cl ON cl.id = ct.cliente_id
WHERE NOT EXISTS (
    SELECT 1 FROM apropriacoes_custo ac WHERE ac.conta_pagar_id = cp.id
)
"""


REVENUE_SQL = """
SELECT
    f.data_emissao AS data,
    f.competencia,
    f.numero_documento,
    f.valor_bruto::numeric AS valor_bruto,
    f.impostos::numeric AS impostos,
    f.retencoes::numeric AS retencoes,
    f.valor_liquido::numeric AS valor_liquido,
    f.status,
    o.id AS obra_id,
    o.nome::text AS obra,
    p.id AS projeto_id,
    p.nome::text AS projeto,
    cl.id AS cliente_id,
    cl.nome::text AS cliente
FROM faturas f
LEFT JOIN obras o ON o.id = f.obra_id
LEFT JOIN projetos p ON p.id = o.projeto_id
LEFT JOIN contratos ct ON ct.id = COALESCE(f.contrato_id, o.contrato_id, p.contrato_id)
JOIN clientes cl ON cl.id = f.cliente_id
"""


CASH_SQL = """
SELECT
    mc.data_movimentacao AS data,
    TO_CHAR(mc.data_movimentacao, 'YYYY-MM') AS competencia,
    mc.tipo,
    mc.valor::numeric AS valor,
    mc.descricao,
    mc.forma_pagamento,
    mc.conciliado,
    cb.banco::text AS banco,
    COALESCE(cf.nome, 'Sem categoria')::text AS categoria,
    o.id AS obra_id,
    o.nome::text AS obra,
    p.id AS projeto_id,
    p.nome::text AS projeto,
    cl.id AS cliente_id,
    cl.nome::text AS cliente
FROM movimentacoes_caixa mc
JOIN contas_bancarias cb ON cb.id = mc.conta_bancaria_id
LEFT JOIN categorias_financeiras cf ON cf.id = mc.categoria_financeira_id
LEFT JOIN centros_custo cc ON cc.id = mc.centro_custo_id
LEFT JOIN contas_pagar cp ON cp.id = mc.conta_pagar_id
LEFT JOIN faturas f ON f.id = mc.fatura_id
LEFT JOIN obras o ON o.id = COALESCE(cc.obra_id, cp.obra_id, f.obra_id)
LEFT JOIN projetos p ON p.id = o.projeto_id
LEFT JOIN contratos ct ON ct.id = COALESCE(f.contrato_id, o.contrato_id, p.contrato_id)
LEFT JOIN clientes cl ON cl.id = COALESCE(f.cliente_id, ct.cliente_id)
"""


WORKS_SQL = """
SELECT data_inicio AS data, COUNT(*)::numeric AS quantidade
FROM obras
WHERE data_inicio IS NOT NULL
GROUP BY data_inicio
ORDER BY data_inicio
"""


def _query_frame(db: Session, sql: str) -> pd.DataFrame:
    return pd.read_sql_query(text(sql), db.connection())


def _prepare_frame(frame: pd.DataFrame, monetary_columns: list[str]) -> pd.DataFrame:
    prepared = frame.copy()
    if "data" in prepared.columns:
        prepared["data"] = pd.to_datetime(prepared["data"], errors="coerce")
    for column in monetary_columns:
        if column in prepared.columns:
            prepared[column] = pd.to_numeric(prepared[column], errors="coerce").fillna(0.0)
    return prepared


def load_financial_data(db: Session) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    expenses = _prepare_frame(_query_frame(db, EXPENSES_SQL), ["valor"])
    revenue = _prepare_frame(
        _query_frame(db, REVENUE_SQL),
        ["valor_bruto", "impostos", "retencoes", "valor_liquido"],
    )
    cash = _prepare_frame(_query_frame(db, CASH_SQL), ["valor"])
    return expenses, revenue, cash


def _money(value: float) -> str:
    return format_currency_br(value)


def _chart_locale_pt_br() -> alt.Locale:
    return alt.Locale(
        number=alt.NumberLocale(
            decimal=",",
            thousands=".",
            grouping=[3],
            currency=["R$ ", ""],
            percent="%",
            minus="−",
            nan="Não disponível",
        ),
        time=alt.TimeLocale(
            dateTime="%A, %e de %B de %Y, %X",
            date="%d/%m/%Y",
            time="%H:%M:%S",
            periods=["AM", "PM"],
            days=list(WEEKDAY_NAMES_PT_BR),
            shortDays=list(SHORT_WEEKDAY_NAMES_PT_BR),
            months=list(MONTH_NAMES_PT_BR),
            shortMonths=list(SHORT_MONTH_NAMES_PT_BR),
        ),
    )


def _render_monthly_line_chart(
    frame: pd.DataFrame,
    *,
    height: int,
    monetary: bool = True,
) -> None:
    """Renderiza série temporal sem depender do idioma do navegador."""
    prepared = frame.copy()
    index_name = prepared.index.name or "data"
    prepared.index.name = index_name
    prepared = prepared.reset_index().rename(columns={index_name: "data"})
    prepared["data"] = pd.to_datetime(prepared["data"], errors="coerce")
    values = prepared.melt(id_vars="data", var_name="Indicador", value_name="Valor")
    values = values.dropna(subset=["data", "Valor"])
    if values.empty:
        st.info("Ainda não há dados suficientes para montar este gráfico.")
        return

    value_format = "$,.2f" if monetary else ",.0f"
    value_title = "Valor (R$)" if monetary else "Quantidade"
    chart = (
        alt.Chart(values)
        .mark_line(point=True)
        .encode(
            x=alt.X(
                "data:T",
                title="Período",
                axis=alt.Axis(format="%b/%Y", labelAngle=-35),
            ),
            y=alt.Y(
                "Valor:Q",
                title=value_title,
                axis=alt.Axis(format=value_format),
            ),
            color=alt.Color("Indicador:N", title="Indicador"),
            tooltip=[
                alt.Tooltip("data:T", title="Período", format="%B de %Y"),
                alt.Tooltip("Indicador:N", title="Indicador"),
                alt.Tooltip("Valor:Q", title=value_title, format=value_format),
            ],
        )
        .properties(height=height)
        .configure(locale=_chart_locale_pt_br())
    )
    st.altair_chart(chart, width="stretch")


def _monthly(frame: pd.DataFrame, value_column: str, output_name: str) -> pd.DataFrame:
    if frame.empty or frame["data"].dropna().empty:
        return pd.DataFrame(columns=["data", output_name])
    work = frame.dropna(subset=["data"]).copy()
    work["data"] = work["data"].dt.to_period("M").dt.to_timestamp()
    return work.groupby("data", as_index=False)[value_column].sum().rename(columns={value_column: output_name})


def _complete_months(series: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    if series.empty:
        return series
    start = series["data"].min()
    end = series["data"].max()
    calendar = pd.DataFrame({"data": pd.date_range(start=start, end=end, freq="MS")})
    return calendar.merge(series, on="data", how="left").fillna({column: 0.0 for column in columns})


def build_economic_series(expenses: pd.DataFrame, revenue: pd.DataFrame) -> pd.DataFrame:
    operating_expenses = expenses[expenses["natureza"] != "Investimento"] if "natureza" in expenses else expenses
    costs = _monthly(operating_expenses, "valor", "Custos")
    billing = _monthly(revenue, "valor_liquido", "Faturamento líquido")
    if costs.empty and billing.empty:
        return pd.DataFrame(columns=["data", "Faturamento líquido", "Custos", "Resultado"])
    series = pd.merge(billing, costs, on="data", how="outer").fillna(0.0).sort_values("data")
    series = _complete_months(series, ["Faturamento líquido", "Custos"])
    series["Resultado"] = series["Faturamento líquido"] - series["Custos"]
    return series


def build_cash_series(cash: pd.DataFrame) -> pd.DataFrame:
    if cash.empty:
        return pd.DataFrame(columns=["data", "Entradas", "Saídas", "Saldo do mês"])
    work = cash.copy()
    work["entrada"] = work["valor"].where(work["tipo"] == "entrada", 0.0)
    work["saida"] = work["valor"].where(work["tipo"] == "saida", 0.0)
    entries = _monthly(work, "entrada", "Entradas")
    exits = _monthly(work, "saida", "Saídas")
    series = pd.merge(entries, exits, on="data", how="outer").fillna(0.0).sort_values("data")
    series = _complete_months(series, ["Entradas", "Saídas"])
    series["Saldo do mês"] = series["Entradas"] - series["Saídas"]
    return series


def _actual_and_projection(
    series: pd.DataFrame,
    value_column: str,
    months: int = 6,
    nonnegative: bool = False,
) -> tuple[pd.DataFrame, float]:
    if series.empty:
        return pd.DataFrame(columns=["Realizado", "Projeção"]), 0.0
    history = series[["data", value_column]].dropna().sort_values("data").copy()
    if history.empty:
        return pd.DataFrame(columns=["Realizado", "Projeção"]), 0.0
    history = history.tail(12).reset_index(drop=True)
    values = history[value_column].astype(float).tolist()
    if len(values) < 2:
        slope = 0.0
        intercept = values[-1]
    else:
        xs = list(range(len(values)))
        x_mean = sum(xs) / len(xs)
        y_mean = sum(values) / len(values)
        denominator = sum((x - x_mean) ** 2 for x in xs)
        slope = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, values)) / denominator if denominator else 0.0
        intercept = y_mean - slope * x_mean
    future_dates = pd.date_range(history["data"].iloc[-1] + pd.offsets.MonthBegin(1), periods=months, freq="MS")
    projected_values = [intercept + slope * (len(values) + index) for index in range(months)]
    if nonnegative:
        projected_values = [max(0.0, value) for value in projected_values]
    actual = pd.DataFrame({"data": history["data"], "Realizado": values, "Projeção": float("nan")})
    connector = pd.DataFrame(
        {"data": [history["data"].iloc[-1]], "Realizado": [float("nan")], "Projeção": [values[-1]]}
    )
    forecast = pd.DataFrame({"data": future_dates, "Realizado": float("nan"), "Projeção": projected_values})
    chart = pd.concat([actual, connector, forecast], ignore_index=True).set_index("data")
    return chart, float(projected_values[-1]) if projected_values else values[-1]


def _filter_period(frame: pd.DataFrame, start: date, end: date) -> pd.DataFrame:
    if frame.empty:
        return frame
    start_ts = pd.Timestamp(start)
    end_ts = pd.Timestamp(end)
    return frame[frame["data"].between(start_ts, end_ts, inclusive="both")].copy()


def _filter_dimensions(
    frame: pd.DataFrame,
    works: list[str],
    clients: list[str],
) -> pd.DataFrame:
    filtered = frame.copy()
    if works and "obra" in filtered.columns:
        filtered = filtered[filtered["obra"].isin(works)]
    if clients and "cliente" in filtered.columns:
        filtered = filtered[filtered["cliente"].isin(clients)]
    return filtered


def _period_bounds(
    period: str,
    frames: list[pd.DataFrame],
) -> tuple[date, date]:
    today = today_in_timezone(APP_SETTINGS.app_timezone)
    if period == "Ano atual":
        return date(today.year, 1, 1), date(today.year, 12, 31)
    if period == "Últimos 12 meses":
        start = (pd.Timestamp(today).to_period("M").start_time - pd.DateOffset(months=11)).date()
        return start, today
    dates = [value for frame in frames if not frame.empty for value in frame["data"].dropna().tolist()]
    if not dates:
        return date(today.year, 1, 1), today
    return min(dates).date(), max(dates).date()


def _go_to(page: str) -> Callable[[], None]:
    def callback() -> None:
        st.session_state["main_page"] = page

    return callback


def _render_quick_actions() -> None:
    st.subheader("Ações rápidas")
    st.caption("Use estes atalhos para registrar uma operação sem procurar o módulo no menu.")
    first_row = st.columns(2)
    first_row[0].button("Emitir fatura", use_container_width=True, on_click=_go_to("Faturas"))
    first_row[1].button("Registrar conta a pagar", use_container_width=True, on_click=_go_to("Contas Pagar"))
    second_row = st.columns(2)
    second_row[0].button("Registrar entrada ou saída", use_container_width=True, on_click=_go_to("Movimentacoes Caixa"))
    second_row[1].button("Apropriar custo à obra", use_container_width=True, on_click=_go_to("Apropriacoes Custo"))


def _render_overview(expenses: pd.DataFrame, revenue: pd.DataFrame, cash: pd.DataFrame) -> None:
    gross = float(revenue["valor_bruto"].sum()) if not revenue.empty else 0.0
    net = float(revenue["valor_liquido"].sum()) if not revenue.empty else 0.0
    operating = expenses[expenses["natureza"] != "Investimento"] if not expenses.empty else expenses
    investments = expenses[expenses["natureza"] == "Investimento"] if not expenses.empty else expenses
    costs = float(operating["valor"].sum()) if not operating.empty else 0.0
    investment_total = float(investments["valor"].sum()) if not investments.empty else 0.0
    result = net - costs
    cash_balance = 0.0
    if not cash.empty:
        cash_balance = float(cash.loc[cash["tipo"] == "entrada", "valor"].sum() - cash.loc[cash["tipo"] == "saida", "valor"].sum())
    margin = (result / net * 100) if net else 0.0

    first_row = st.columns(3)
    first_row[0].metric("Faturamento bruto", _money(gross), help="Total das notas/faturas antes de impostos e retenções.")
    first_row[1].metric("Faturamento líquido", _money(net), help="Valor faturado depois de impostos e retenções.")
    first_row[2].metric("Custos operacionais", _money(costs), help="Custos de obras, pessoal, manutenção, combustível e contas a pagar ainda não apropriadas.")
    second_row = st.columns(3)
    second_row[0].metric("Resultado", _money(result), delta=f"Margem {format_number_br(margin, 1)}%", help="Faturamento líquido menos custos operacionais.")
    second_row[1].metric("Investimentos", _money(investment_total), help="Compra de máquinas e veículos. É apresentada separadamente para não distorcer o lucro operacional.")
    second_row[2].metric("Saldo de caixa", _money(cash_balance), help="Entradas recebidas menos saídas pagas. Não é o mesmo que lucro.")

    st.subheader("Evolução mensal")
    series = build_economic_series(expenses, revenue)
    if series.empty:
        st.info("Ainda não há dados suficientes para montar a evolução mensal.")
    else:
        _render_monthly_line_chart(
            series.set_index("data")[["Faturamento líquido", "Custos", "Resultado"]],
            height=360,
        )

    left, right = st.columns(2)
    with left:
        st.subheader("Despesas por categoria")
        if expenses.empty:
            st.info("Nenhuma despesa encontrada no período.")
        else:
            categories = expenses.groupby("categoria", as_index=False)["valor"].sum().sort_values("valor", ascending=False).head(12)
            st.bar_chart(categories.set_index("categoria")["valor"], horizontal=True, height=360)
    with right:
        st.subheader("Despesas por origem")
        if expenses.empty:
            st.info("Nenhuma despesa encontrada no período.")
        else:
            sources = expenses.groupby("origem", as_index=False)["valor"].sum().sort_values("valor", ascending=False)
            st.bar_chart(sources.set_index("origem")["valor"], horizontal=True, height=360)


def _profitability_table(expenses: pd.DataFrame, revenue: pd.DataFrame, grouping: str) -> pd.DataFrame:
    mapping = {"Obra": "obra", "Projeto": "projeto", "Cliente": "cliente"}
    column = mapping[grouping]
    missing = f"Sem {grouping.lower()} definido"
    cost_work = expenses.copy()
    revenue_work = revenue.copy()
    cost_work[column] = cost_work[column].fillna(missing)
    revenue_work[column] = revenue_work[column].fillna(missing)
    operating = cost_work[cost_work["natureza"] != "Investimento"]
    investments = cost_work[cost_work["natureza"] == "Investimento"]
    costs = operating.groupby(column, as_index=False)["valor"].sum().rename(columns={"valor": "Custos operacionais"})
    investment_totals = investments.groupby(column, as_index=False)["valor"].sum().rename(columns={"valor": "Investimentos"})
    billing = revenue_work.groupby(column, as_index=False)["valor_liquido"].sum().rename(columns={"valor_liquido": "Faturamento líquido"})
    result = pd.merge(billing, costs, on=column, how="outer").fillna(0.0)
    result = pd.merge(result, investment_totals, on=column, how="outer").fillna(0.0)
    result["Resultado"] = result["Faturamento líquido"] - result["Custos operacionais"]
    result["Margem (%)"] = result.apply(
        lambda row: row["Resultado"] / row["Faturamento líquido"] * 100 if row["Faturamento líquido"] else 0.0,
        axis=1,
    )
    return result.rename(columns={column: grouping}).sort_values("Resultado", ascending=False)


def _render_profitability(expenses: pd.DataFrame, revenue: pd.DataFrame) -> None:
    st.subheader("Rentabilidade sem precisar procurar por ID")
    st.caption("Compare o que foi faturado com os custos associados à mesma obra, projeto ou cliente.")
    grouping = st.segmented_control("Analisar por", ["Obra", "Projeto", "Cliente"], default="Obra", key="finance_grouping")
    table = _profitability_table(expenses, revenue, grouping or "Obra")
    if table.empty:
        st.info("Nenhuma informação encontrada para este recorte.")
        return
    chart = table.set_index(grouping or "Obra")[["Faturamento líquido", "Custos operacionais", "Resultado"]]
    st.bar_chart(chart, height=420)
    display = table.copy()
    for column in ("Faturamento líquido", "Custos operacionais", "Investimentos", "Resultado"):
        display[column] = display[column].map(format_currency_br)
    display["Margem (%)"] = display["Margem (%)"].map(lambda value: f"{format_number_br(value, 1)}%")
    st.dataframe(display, width="stretch", hide_index=True)


def _render_expenses(expenses: pd.DataFrame) -> None:
    st.subheader("Consulta consolidada de despesas")
    st.caption("Aqui aparecem custos de materiais e obras, folha, manutenção, combustível, uso e compra de máquinas, além de contas a pagar não apropriadas.")
    search = st.text_input("Pesquisar despesa", placeholder="Ex.: combustível, salário, galpão, manutenção...", key="financial_expense_search").strip().casefold()
    detailed = expenses.copy()
    if search and not detailed.empty:
        columns = ["natureza", "origem", "categoria", "descricao", "obra", "projeto", "cliente"]
        mask = detailed[columns].fillna("").astype(str).agg(" ".join, axis=1).str.casefold().str.contains(search, regex=False)
        detailed = detailed[mask]
    st.caption(f"{len(detailed)} lançamento(s) encontrado(s). Total: {_money(detailed['valor'].sum() if not detailed.empty else 0)}")
    if detailed.empty:
        st.info("Nenhuma despesa corresponde aos filtros e à pesquisa.")
        return
    display = detailed[["data", "natureza", "origem", "categoria", "descricao", "valor", "obra", "projeto", "cliente"]].sort_values("data", ascending=False)
    display = display.rename(
        columns={"data": "Data", "natureza": "Natureza", "origem": "Origem", "categoria": "Categoria", "descricao": "Descrição", "valor": "Valor", "obra": "Obra", "projeto": "Projeto", "cliente": "Cliente"}
    )
    display["Valor"] = display["Valor"].map(format_currency_br)
    st.dataframe(
        display,
        width="stretch",
        hide_index=True,
        column_config={"Data": st.column_config.DateColumn(format="DD/MM/YYYY")},
    )
    st.download_button(
        "Baixar despesas filtradas",
        data=display.to_csv(index=False, sep=";").encode("utf-8-sig"),
        file_name="despesas_financeiras.csv",
        mime="text/csv",
    )


def _render_cash(cash: pd.DataFrame) -> None:
    st.subheader("Fluxo de caixa")
    st.caption("Mostra o dinheiro efetivamente movimentado. Uma venda faturada só entra no caixa quando o recebimento é registrado.")
    series = build_cash_series(cash)
    if series.empty:
        st.info("Nenhuma movimentação de caixa encontrada no período.")
        return
    entries = float(series["Entradas"].sum())
    exits = float(series["Saídas"].sum())
    columns = st.columns(3)
    columns[0].metric("Entradas", _money(entries))
    columns[1].metric("Saídas", _money(exits))
    columns[2].metric("Saldo do período", _money(entries - exits))
    _render_monthly_line_chart(
        series.set_index("data")[["Entradas", "Saídas", "Saldo do mês"]],
        height=360,
    )
    display = cash[["data", "tipo", "descricao", "categoria", "valor", "banco", "obra", "cliente", "conciliado"]].sort_values("data", ascending=False)
    display = display.rename(columns={"data": "Data", "tipo": "Tipo", "descricao": "Descrição", "categoria": "Categoria", "valor": "Valor", "banco": "Banco", "obra": "Obra", "cliente": "Cliente", "conciliado": "Conciliado"})
    display["Tipo"] = display["Tipo"].map({"entrada": "Entrada", "saida": "Saída"}).fillna(display["Tipo"])
    display["Conciliado"] = display["Conciliado"].map({True: "Sim", False: "Não"})
    display["Valor"] = display["Valor"].map(format_currency_br)
    st.dataframe(
        display,
        width="stretch",
        hide_index=True,
        column_config={"Data": st.column_config.DateColumn(format="DD/MM/YYYY")},
    )


def _render_projection(expenses: pd.DataFrame, revenue: pd.DataFrame, cash: pd.DataFrame) -> None:
    st.subheader("Projeção financeira")
    st.caption("Escolha o indicador. A linha projetada estima os próximos seis meses a partir da tendência dos últimos registros.")
    indicator = st.segmented_control(
        "Indicador",
        ["Faturamento líquido", "Custos operacionais", "Resultado (lucro/perda)", "Saldo de caixa"],
        default="Faturamento líquido",
        key="financial_projection_indicator",
    )
    economic = build_economic_series(expenses, revenue)
    cash_series = build_cash_series(cash)
    if indicator == "Saldo de caixa":
        source, column, nonnegative = cash_series, "Saldo do mês", False
    elif indicator == "Custos operacionais":
        source, column, nonnegative = economic, "Custos", True
    elif indicator == "Resultado (lucro/perda)":
        source, column, nonnegative = economic, "Resultado", False
    else:
        source, column, nonnegative = economic, "Faturamento líquido", True
    chart, last_projection = _actual_and_projection(source, column, nonnegative=nonnegative)
    if chart.empty:
        st.info("Ainda não há histórico suficiente para esta projeção.")
        return
    st.metric("Estimativa para o sexto mês", _money(last_projection), delta="lucro" if column == "Resultado" and last_projection >= 0 else ("perda" if column == "Resultado" else None))
    _render_monthly_line_chart(chart, height=420)
    st.warning("Esta é uma estimativa linear para apoio à análise, não uma garantia. Orçamento, contratos, cronograma, sazonalidade e decisões comerciais devem ser considerados antes de tomar decisões.")


def render_financial_area() -> None:
    st.title("Área financeira")
    st.write("Uma visão única de faturamento, custos, rentabilidade e caixa da UrbanPrime.")
    with st.expander("Como interpretar esta área", expanded=False):
        st.markdown(
            """
            - **Faturamento** é o valor emitido para o cliente.
            - **Resultado** compara faturamento líquido e custos, indicando lucro ou perda.
            - **Caixa** mostra somente dinheiro recebido ou pago; por isso pode ser diferente do resultado.
            - Use obra, projeto e cliente pelo nome. Os códigos internos continuam preservados no banco, mas não são necessários para consultar.
            """
        )

    db = None
    try:
        from src.core.database.connection import SessionLocal

        db = SessionLocal()
        expenses, revenue, cash = load_financial_data(db)
    except Exception as exc:
        st.error(f"Não foi possível carregar a área financeira: {exc}")
        return
    finally:
        if db is not None:
            db.close()

    _render_quick_actions()
    st.divider()
    st.subheader("Filtros da análise")
    period = st.selectbox("Período", ["Ano atual", "Últimos 12 meses", "Todo o histórico", "Personalizado"], key="financial_period")
    default_start, default_end = _period_bounds(period, [expenses, revenue, cash])
    if period == "Personalizado":
        date_columns = st.columns(2)
        start = date_columns[0].date_input("Data inicial", value=default_start, key="financial_start")
        end = date_columns[1].date_input("Data final", value=default_end, key="financial_end")
    else:
        start, end = default_start, default_end
        st.caption(f"Período considerado: {start.strftime('%d/%m/%Y')} a {end.strftime('%d/%m/%Y')}")

    work_options = sorted({str(value) for frame in (expenses, revenue, cash) if "obra" in frame for value in frame["obra"].dropna().unique()})
    client_options = sorted({str(value) for frame in (expenses, revenue, cash) if "cliente" in frame for value in frame["cliente"].dropna().unique()})
    category_options = sorted(str(value) for value in expenses["categoria"].dropna().unique()) if not expenses.empty else []
    filter_columns = st.columns(3)
    selected_works = filter_columns[0].multiselect("Obras", work_options, placeholder="Todas as obras")
    selected_clients = filter_columns[1].multiselect("Clientes", client_options, placeholder="Todos os clientes")
    selected_categories = filter_columns[2].multiselect("Categorias de despesa", category_options, placeholder="Todas as categorias")
    if start > end:
        st.error("A data inicial precisa ser anterior à data final.")
        return

    expenses = _filter_dimensions(_filter_period(expenses, start, end), selected_works, selected_clients)
    revenue = _filter_dimensions(_filter_period(revenue, start, end), selected_works, selected_clients)
    cash = _filter_dimensions(_filter_period(cash, start, end), selected_works, selected_clients)
    if selected_categories:
        expenses = expenses[expenses["categoria"].isin(selected_categories)]
        cash = cash[cash["categoria"].isin(selected_categories)]
        st.caption("Com categorias selecionadas, o resultado compara todo o faturamento do recorte somente com os custos operacionais dessas categorias; investimentos permanecem separados.")

    tabs = st.tabs(["Visão geral", "Rentabilidade", "Despesas", "Fluxo de caixa", "Projeções"])
    with tabs[0]:
        _render_overview(expenses, revenue, cash)
    with tabs[1]:
        _render_profitability(expenses, revenue)
    with tabs[2]:
        _render_expenses(expenses)
    with tabs[3]:
        _render_cash(cash)
    with tabs[4]:
        _render_projection(expenses, revenue, cash)


def render_dashboard_trends(db: Session) -> None:
    st.subheader("Tendências e projeções")
    st.caption("Troque o indicador para acompanhar crescimento, queda, lucro ou perda ao longo do tempo.")
    try:
        expenses, revenue, cash = load_financial_data(db)
        works = _prepare_frame(_query_frame(db, WORKS_SQL), ["quantidade"])
        economic = build_economic_series(expenses, revenue)
        cash_series = build_cash_series(cash)
        works_series = _monthly(works, "quantidade", "Novas obras")
        if not works_series.empty:
            works_series = _complete_months(works_series, ["Novas obras"])
            works_series["Total de obras"] = works_series["Novas obras"].cumsum()
        indicator = st.segmented_control(
            "O que você quer analisar?",
            ["Faturamento", "Lucro ou perda", "Caixa", "Quantidade de obras"],
            default="Faturamento",
            key="dashboard_trend_indicator",
        )
        include_projection = st.toggle("Mostrar projeção dos próximos 6 meses", value=True, key="dashboard_show_projection")
        if indicator == "Lucro ou perda":
            source, column, nonnegative = economic, "Resultado", False
        elif indicator == "Caixa":
            source, column, nonnegative = cash_series, "Saldo do mês", False
        elif indicator == "Quantidade de obras":
            source, column, nonnegative = works_series, "Total de obras", True
        else:
            source, column, nonnegative = economic, "Faturamento líquido", True
        if source.empty:
            st.info("Ainda não há histórico para este indicador.")
            return
        chart, final_value = _actual_and_projection(source, column, nonnegative=nonnegative)
        if not include_projection:
            chart = source.set_index("data")[[column]].rename(columns={column: "Realizado"})
        left, right = st.columns([4, 1])
        with left:
            _render_monthly_line_chart(
                chart,
                height=340,
                monetary=indicator != "Quantidade de obras",
            )
        with right:
            current_value = float(source[column].iloc[-1])
            if indicator == "Quantidade de obras":
                st.metric("Último valor", f"{current_value:.0f} obras")
                if include_projection:
                    st.metric("Em 6 meses", f"{final_value:.0f} obras")
            else:
                st.metric("Último mês", _money(current_value))
                if include_projection:
                    st.metric("Estimativa em 6 meses", _money(final_value))
                    if indicator == "Lucro ou perda":
                        st.caption("Tendência de lucro" if final_value >= 0 else "Tendência de perda")
        if include_projection:
            st.caption("A projeção é uma tendência linear baseada nos últimos 12 meses registrados. Use-a como referência e valide decisões com contratos, orçamento e cronograma.")
    except Exception as exc:
        st.warning(f"Os gráficos de tendência não puderam ser carregados: {exc}")
