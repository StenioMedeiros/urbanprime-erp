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


ORDERS_SQL = """
WITH item_totals AS (
    SELECT ordem_compra_id,
           COUNT(*)::numeric AS quantidade_itens,
           SUM(valor_total)::numeric AS total_itens
    FROM itens_ordem_compra
    GROUP BY ordem_compra_id
), payables AS (
    SELECT ordem_compra_id,
           COUNT(*)::numeric AS contas_geradas,
           SUM(valor)::numeric AS valor_contas,
           SUM(valor) FILTER (WHERE status = 'pago')::numeric AS valor_pago,
           COUNT(*) FILTER (WHERE status NOT IN ('pago', 'cancelado'))::numeric AS contas_pendentes
    FROM contas_pagar
    WHERE ordem_compra_id IS NOT NULL
    GROUP BY ordem_compra_id
)
SELECT
    oc.id AS ordem_id,
    oc.numero,
    oc.status,
    oc.data_emissao,
    oc.data_aprovacao,
    oc.data_recebimento,
    oc.valor_total::numeric AS valor_ordem,
    oc.fornecedor_id,
    COALESCE(NULLIF(f.nome_fantasia, ''), f.razao_social) AS fornecedor,
    f.status AS status_fornecedor,
    oc.obra_id,
    o.nome AS obra,
    oc.cotacao_id,
    c.status AS status_cotacao,
    c.valor_total::numeric AS valor_cotado,
    c.data_cotacao,
    COALESCE(i.quantidade_itens, 0)::numeric AS quantidade_itens,
    COALESCE(i.total_itens, 0)::numeric AS total_itens,
    COALESCE(p.contas_geradas, 0)::numeric AS contas_geradas,
    COALESCE(p.valor_contas, 0)::numeric AS valor_contas,
    COALESCE(p.valor_pago, 0)::numeric AS valor_pago,
    COALESCE(p.contas_pendentes, 0)::numeric AS contas_pendentes
FROM ordens_compra oc
JOIN fornecedores f ON f.id = oc.fornecedor_id
LEFT JOIN obras o ON o.id = oc.obra_id
LEFT JOIN cotacoes c ON c.id = oc.cotacao_id
LEFT JOIN item_totals i ON i.ordem_compra_id = oc.id
LEFT JOIN payables p ON p.ordem_compra_id = oc.id
ORDER BY oc.data_emissao DESC NULLS LAST, oc.id DESC
"""


QUOTES_SQL = """
WITH linked_orders AS (
    SELECT cotacao_id,
           COUNT(*)::numeric AS ordens_vinculadas,
           SUM(valor_total)::numeric AS valor_comprado,
           MIN(id) AS ordem_id
    FROM ordens_compra
    WHERE cotacao_id IS NOT NULL
    GROUP BY cotacao_id
)
SELECT
    c.id AS cotacao_id,
    c.fornecedor_id,
    COALESCE(NULLIF(f.nome_fantasia, ''), f.razao_social) AS fornecedor,
    c.obra_id,
    o.nome AS obra,
    c.descricao,
    c.valor_total::numeric AS valor_cotado,
    c.data_cotacao,
    c.status,
    COALESCE(lo.ordens_vinculadas, 0)::numeric AS ordens_vinculadas,
    COALESCE(lo.valor_comprado, 0)::numeric AS valor_comprado,
    lo.ordem_id
FROM cotacoes c
JOIN fornecedores f ON f.id = c.fornecedor_id
LEFT JOIN obras o ON o.id = c.obra_id
LEFT JOIN linked_orders lo ON lo.cotacao_id = c.id
ORDER BY c.data_cotacao DESC NULLS LAST, c.id DESC
"""


SUPPLIERS_SQL = """
SELECT id AS fornecedor_id,
       COALESCE(NULLIF(nome_fantasia, ''), razao_social) AS fornecedor,
       razao_social,
       cnpj,
       email,
       telefone,
       status,
       created_at
FROM fornecedores
ORDER BY fornecedor
"""


ITEMS_SQL = """
SELECT
    i.id AS item_id,
    i.ordem_compra_id AS ordem_id,
    oc.numero AS ordem,
    oc.fornecedor_id,
    COALESCE(NULLIF(f.nome_fantasia, ''), f.razao_social) AS fornecedor,
    oc.obra_id,
    o.nome AS obra,
    i.insumo_id,
    COALESCE(ins.nome, i.descricao) AS insumo,
    i.descricao,
    i.quantidade::numeric AS quantidade,
    i.valor_unitario::numeric AS valor_unitario,
    i.valor_total::numeric AS valor_total,
    oc.data_emissao
FROM itens_ordem_compra i
JOIN ordens_compra oc ON oc.id = i.ordem_compra_id
JOIN fornecedores f ON f.id = oc.fornecedor_id
LEFT JOIN obras o ON o.id = oc.obra_id
LEFT JOIN insumos ins ON ins.id = i.insumo_id
ORDER BY oc.data_emissao DESC NULLS LAST, i.id DESC
"""


ORDER_STATUS_LABELS = {
    "aberta": "Aberta",
    "aprovada": "Aprovada",
    "recebida": "Recebida",
    "cancelada": "Cancelada",
}


QUOTE_STATUS_LABELS = {
    "aberta": "Aberta",
    "aprovada": "Aprovada",
    "recusada": "Recusada",
    "cancelada": "Cancelada",
}


NUMERIC_ORDER_COLUMNS = (
    "valor_ordem",
    "valor_cotado",
    "quantidade_itens",
    "total_itens",
    "contas_geradas",
    "valor_contas",
    "valor_pago",
    "contas_pendentes",
)


def _query_frame(db: Session, sql: str) -> pd.DataFrame:
    return pd.read_sql_query(text(sql), db.connection())


def load_purchases_dashboard_data(
    db: Session,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    orders = _query_frame(db, ORDERS_SQL)
    for column in ("data_emissao", "data_aprovacao", "data_recebimento", "data_cotacao"):
        orders[column] = pd.to_datetime(orders[column], errors="coerce")
    for column in NUMERIC_ORDER_COLUMNS:
        orders[column] = pd.to_numeric(orders[column], errors="coerce").fillna(0.0)

    quotes = _query_frame(db, QUOTES_SQL)
    quotes["data_cotacao"] = pd.to_datetime(quotes["data_cotacao"], errors="coerce")
    for column in ("valor_cotado", "valor_comprado", "ordens_vinculadas"):
        quotes[column] = pd.to_numeric(quotes[column], errors="coerce").fillna(0.0)

    suppliers = _query_frame(db, SUPPLIERS_SQL)
    suppliers["created_at"] = pd.to_datetime(suppliers["created_at"], errors="coerce")

    items = _query_frame(db, ITEMS_SQL)
    items["data_emissao"] = pd.to_datetime(items["data_emissao"], errors="coerce")
    for column in ("quantidade", "valor_unitario", "valor_total"):
        items[column] = pd.to_numeric(items[column], errors="coerce").fillna(0.0)
    return orders, quotes, suppliers, items


def _date_value(value: Any) -> date | None:
    if value is None or pd.isna(value):
        return None
    if isinstance(value, pd.Timestamp):
        return value.date()
    if isinstance(value, date):
        return value
    parsed = pd.to_datetime(value, errors="coerce")
    return None if pd.isna(parsed) else parsed.date()


def purchase_attention(
    status: str,
    emission_date: Any,
    approval_date: Any,
    receipt_date: Any,
    order_total: float,
    item_total: float,
    today: date,
) -> str:
    emission = _date_value(emission_date)
    approval = _date_value(approval_date)
    receipt = _date_value(receipt_date)
    if status == "cancelada":
        return "Cancelada"
    if status == "recebida" and receipt is None:
        return "Dados incompletos"
    if status == "aberta" and approval is not None:
        return "Situação inconsistente"
    if abs(float(order_total) - float(item_total)) > 0.01:
        return "Total divergente"
    if status in {"aberta", "aprovada"} and emission is not None and emission < today - timedelta(days=30):
        return "Aguardando há mais de 30 dias"
    if status == "recebida":
        return "Recebida"
    if status == "aprovada":
        return "Aguardando recebimento"
    if status == "aberta":
        return "Aguardando aprovação"
    return "Acompanhar"


def purchase_period_bounds(
    period: str,
    today: date,
    orders: pd.DataFrame,
    quotes: pd.DataFrame,
) -> tuple[date, date]:
    if period == "Ano atual":
        return date(today.year, 1, 1), today
    if period == "Últimos 12 meses":
        start = (pd.Timestamp(today).to_period("M").start_time - pd.DateOffset(months=11)).date()
        return start, today
    dates: list[pd.Timestamp] = []
    if not orders.empty:
        dates.extend(orders["data_emissao"].dropna().tolist())
    if not quotes.empty:
        dates.extend(quotes["data_cotacao"].dropna().tolist())
    if not dates:
        return date(today.year, 1, 1), today
    return min(dates).date(), max(max(dates).date(), today)


def filter_purchases(
    orders: pd.DataFrame,
    quotes: pd.DataFrame,
    start: date,
    end: date,
    selected_suppliers: list[str],
    selected_works: list[str],
    selected_statuses: list[str],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    start_ts = pd.Timestamp(start)
    end_ts = pd.Timestamp(end)
    filtered_orders = orders[
        orders["data_emissao"].between(start_ts, end_ts, inclusive="both")
    ].copy()
    filtered_quotes = quotes[
        quotes["data_cotacao"].between(start_ts, end_ts, inclusive="both")
    ].copy()
    if selected_suppliers:
        filtered_orders = filtered_orders[filtered_orders["fornecedor"].isin(selected_suppliers)]
        filtered_quotes = filtered_quotes[filtered_quotes["fornecedor"].isin(selected_suppliers)]
    if selected_works:
        filtered_orders = filtered_orders[filtered_orders["obra"].isin(selected_works)]
        filtered_quotes = filtered_quotes[filtered_quotes["obra"].isin(selected_works)]
    if selected_statuses:
        filtered_orders = filtered_orders[filtered_orders["status"].isin(selected_statuses)]
        quote_ids = filtered_orders["cotacao_id"].dropna().astype(int).tolist()
        filtered_quotes = filtered_quotes[filtered_quotes["cotacao_id"].isin(quote_ids)]
    return filtered_orders, filtered_quotes


def build_purchase_series(orders: pd.DataFrame) -> pd.DataFrame:
    if orders.empty or orders["data_emissao"].dropna().empty:
        return pd.DataFrame(columns=["data", "Valor comprado", "Economia estimada", "Ordens emitidas"])
    work = orders.dropna(subset=["data_emissao"]).copy()
    work["data"] = work["data_emissao"].dt.to_period("M").dt.to_timestamp()
    work["Economia estimada"] = (work["valor_cotado"] - work["valor_ordem"]).clip(lower=0)
    grouped = work.groupby("data", as_index=False).agg(
        **{
            "Valor comprado": ("valor_ordem", "sum"),
            "Economia estimada": ("Economia estimada", "sum"),
            "Ordens emitidas": ("ordem_id", "count"),
        }
    )
    calendar = pd.DataFrame({"data": pd.date_range(grouped["data"].min(), grouped["data"].max(), freq="MS")})
    return calendar.merge(grouped, on="data", how="left").fillna(0.0)


def _status_label(value: Any, labels: dict[str, str]) -> str:
    return labels.get(str(value), str(value).replace("_", " ").title())


def _add_attention(orders: pd.DataFrame, today: date) -> pd.DataFrame:
    result = orders.copy()
    result["atencao"] = result.apply(
        lambda row: purchase_attention(
            str(row["status"]),
            row["data_emissao"],
            row["data_aprovacao"],
            row["data_recebimento"],
            float(row["valor_ordem"]),
            float(row["total_itens"]),
            today,
        ),
        axis=1,
    )
    result["economia"] = (result["valor_cotado"] - result["valor_ordem"]).clip(lower=0)
    result["prazo_recebimento"] = (result["data_recebimento"] - result["data_emissao"]).dt.days
    return result


def _quality_issue_count(orders: pd.DataFrame) -> int:
    if orders.empty:
        return 0
    return int(orders["atencao"].isin({"Dados incompletos", "Situação inconsistente", "Total divergente"}).sum())


def supplier_summary(
    suppliers: pd.DataFrame,
    orders: pd.DataFrame,
    quotes: pd.DataFrame,
    selected_suppliers: list[str] | None = None,
) -> pd.DataFrame:
    base = suppliers.copy()
    if selected_suppliers:
        base = base[base["fornecedor"].isin(selected_suppliers)]
    order_groups = orders.groupby(["fornecedor_id", "fornecedor"], as_index=False).agg(
        ordens=("ordem_id", "count"),
        valor_comprado=("valor_ordem", "sum"),
        ordens_recebidas=("status", lambda values: int((values == "recebida").sum())),
        valor_em_aberto=("valor_ordem", lambda values: float(values[orders.loc[values.index, "status"].isin(["aberta", "aprovada"])] .sum())),
        prazo_medio=("prazo_recebimento", "mean"),
    )
    quote_groups = quotes.groupby("fornecedor_id", as_index=False).agg(cotacoes=("cotacao_id", "count"))
    result = base.merge(order_groups.drop(columns=["fornecedor"], errors="ignore"), on="fornecedor_id", how="left")
    result = result.merge(quote_groups, on="fornecedor_id", how="left")
    for column in ("ordens", "valor_comprado", "ordens_recebidas", "valor_em_aberto", "prazo_medio", "cotacoes"):
        result[column] = pd.to_numeric(result[column], errors="coerce").fillna(0.0)
    total = float(result["valor_comprado"].sum())
    result["participacao"] = result["valor_comprado"] / total * 100 if total else 0.0
    return result.sort_values(["valor_comprado", "fornecedor"], ascending=[False, True])


def _render_top_metrics(orders: pd.DataFrame, quotes: pd.DataFrame, suppliers: pd.DataFrame) -> None:
    total = float(orders["valor_ordem"].sum())
    backlog = float(orders.loc[orders["status"].isin(["aberta", "aprovada"]), "valor_ordem"].sum())
    received = orders[orders["status"] == "recebida"]
    received_value = float(received["valor_ordem"].sum())
    economy = float(orders["economia"].sum())
    quoted_total = float(orders["valor_cotado"].sum())
    economy_rate = economy / quoted_total * 100 if quoted_total else 0.0
    delivery_days = received["prazo_recebimento"].dropna()
    average_delivery = float(delivery_days.mean()) if not delivery_days.empty else 0.0
    suppliers_with_orders = int(orders["fornecedor_id"].nunique())
    average_ticket = total / len(orders) if len(orders) else 0.0
    concentration = 0.0
    if total:
        concentration = float(orders.groupby("fornecedor_id")["valor_ordem"].sum().nlargest(3).sum()) / total * 100
    issues = _quality_issue_count(orders)

    first_row = st.columns(4)
    first_row[0].metric("Ordens analisadas", len(orders))
    first_row[1].metric("Abertas", int((orders["status"] == "aberta").sum()))
    first_row[2].metric("Aprovadas", int((orders["status"] == "aprovada").sum()))
    first_row[3].metric("Recebidas", len(received))

    second_row = st.columns(3)
    second_row[0].metric("Total comprado", format_currency_br(total))
    second_row[1].metric("Aguardando recebimento", format_currency_br(backlog))
    second_row[2].metric("Compras recebidas", format_currency_br(received_value))

    third_row = st.columns(3)
    third_row[0].metric("Economia estimada", format_currency_br(economy), help="Diferença positiva entre o valor cotado e o valor final da ordem vinculada.")
    third_row[1].metric("Economia sobre cotações", f"{format_number_br(economy_rate, 1)}%")
    third_row[2].metric("Prazo médio de recebimento", f"{format_number_br(average_delivery, 1)} dias")

    fourth_row = st.columns(3)
    fourth_row[0].metric("Fornecedores com compras", suppliers_with_orders)
    fourth_row[1].metric("Ticket médio", format_currency_br(average_ticket))
    fourth_row[2].metric("Concentração nos 3 maiores", f"{format_number_br(concentration, 1)}%")

    fifth_row = st.columns(2)
    fifth_row[0].metric("Cotações no recorte", len(quotes))
    fifth_row[1].metric("Pendências cadastrais", issues, delta_color="inverse")

    if issues:
        st.warning(
            f"{issues} ordem(ns) apresentam dados que precisam de conferência, como situação incompatível com as datas "
            "ou diferença entre o total da ordem e a soma dos itens. O painel apenas sinaliza; nenhum registro foi alterado."
        )


def _render_overview(orders: pd.DataFrame) -> None:
    left, right = st.columns(2)
    with left:
        st.subheader("Ordens por situação")
        status = orders["status"].map(lambda value: _status_label(value, ORDER_STATUS_LABELS)).value_counts()
        st.bar_chart(status, horizontal=True, height=290)
    with right:
        st.subheader("Compras por obra")
        by_work = orders.groupby(orders["obra"].fillna("Sem obra"))["valor_ordem"].sum().sort_values(ascending=False).head(12)
        st.bar_chart(by_work, horizontal=True, height=290)

    st.subheader("Evolução das compras e da economia negociada")
    series = build_purchase_series(orders)
    if series.empty:
        st.info("Ainda não existem datas suficientes para montar a evolução das compras.")
        return
    _render_monthly_line_chart(series.set_index("data")[["Valor comprado", "Economia estimada"]], height=350)
    st.subheader("Quantidade mensal de ordens emitidas")
    st.bar_chart(series.set_index("data")["Ordens emitidas"], height=260)


def _orders_ranking(orders: pd.DataFrame) -> pd.DataFrame:
    attention_order = {
        "Dados incompletos": 0,
        "Situação inconsistente": 1,
        "Total divergente": 2,
        "Aguardando há mais de 30 dias": 3,
        "Aguardando aprovação": 4,
        "Aguardando recebimento": 5,
        "Recebida": 6,
        "Cancelada": 7,
    }
    display = orders.copy()
    display["ordem_atencao"] = display["atencao"].map(attention_order).fillna(99)
    display = display.sort_values(["ordem_atencao", "data_emissao", "numero"], ascending=[True, True, True])
    display["status"] = display["status"].map(lambda value: _status_label(value, ORDER_STATUS_LABELS))
    for column in ("valor_cotado", "valor_ordem", "total_itens", "economia"):
        display[column] = display[column].map(format_currency_br)
    return display[
        [
            "atencao", "numero", "fornecedor", "obra", "status", "data_emissao",
            "data_aprovacao", "data_recebimento", "valor_cotado", "valor_ordem",
            "total_itens", "economia",
        ]
    ].rename(
        columns={
            "atencao": "Situação gerencial",
            "numero": "Ordem",
            "fornecedor": "Fornecedor",
            "obra": "Obra",
            "status": "Status",
            "data_emissao": "Emissão",
            "data_aprovacao": "Aprovação",
            "data_recebimento": "Recebimento",
            "valor_cotado": "Valor cotado",
            "valor_ordem": "Valor da ordem",
            "total_itens": "Soma dos itens",
            "economia": "Economia estimada",
        }
    )


def _render_orders(orders: pd.DataFrame, today: date) -> None:
    st.subheader("Ranking gerencial das ordens")
    st.caption("Prioriza inconsistências, ordens há mais de 30 dias sem recebimento e etapas ainda pendentes.")
    st.dataframe(
        _orders_ranking(orders),
        width="stretch",
        hide_index=True,
        column_config={
            "Emissão": st.column_config.DateColumn(format="DD/MM/YYYY"),
            "Aprovação": st.column_config.DateColumn(format="DD/MM/YYYY"),
            "Recebimento": st.column_config.DateColumn(format="DD/MM/YYYY"),
        },
    )

    waiting = orders[orders["status"].isin(["aberta", "aprovada"])]
    older_than_30 = waiting["data_emissao"].lt(pd.Timestamp(today - timedelta(days=30))).sum()
    received_with_date = orders[(orders["status"] == "recebida") & orders["data_recebimento"].notna()]
    paid = float(orders["valor_pago"].sum())
    columns = st.columns(4)
    columns[0].metric("Ordens em processamento", len(waiting))
    columns[1].metric("Há mais de 30 dias", int(older_than_30), delta_color="inverse")
    columns[2].metric("Recebimentos com data", len(received_with_date))
    columns[3].metric("Valor já pago", format_currency_br(paid))
    st.info(
        "As ordens ainda não possuem uma data prevista de entrega. Por isso, o painel trata 30 dias sem recebimento "
        "como ponto de atenção operacional, e não como atraso contratual confirmado."
    )


def _render_suppliers(suppliers: pd.DataFrame, orders: pd.DataFrame, quotes: pd.DataFrame, selected_suppliers: list[str]) -> None:
    summary = supplier_summary(suppliers, orders, quotes, selected_suppliers)
    with_orders = summary[summary["ordens"] > 0]
    without_orders = int((summary["ordens"] == 0).sum())
    active = int((summary["status"] == "ativo").sum())
    top_supplier = with_orders.iloc[0]["fornecedor"] if not with_orders.empty else "Não disponível"
    columns = st.columns(4)
    columns[0].metric("Fornecedores cadastrados", len(summary))
    columns[1].metric("Fornecedores ativos", active)
    columns[2].metric("Sem compras no período", without_orders)
    columns[3].metric("Maior fornecedor", top_supplier)

    st.subheader("Valor comprado por fornecedor")
    if with_orders.empty:
        st.info("Nenhum fornecedor possui compras no período selecionado.")
    else:
        chart = with_orders.head(12).set_index("fornecedor")["valor_comprado"]
        st.bar_chart(chart, horizontal=True, height=max(300, min(520, 36 * len(chart))))

    display = summary.copy()
    display["status"] = display["status"].map(lambda value: str(value).title())
    display["valor_comprado"] = display["valor_comprado"].map(format_currency_br)
    display["valor_em_aberto"] = display["valor_em_aberto"].map(format_currency_br)
    display["participacao"] = display["participacao"].map(lambda value: f"{format_number_br(value, 1)}%")
    display["prazo_medio"] = display["prazo_medio"].map(lambda value: f"{format_number_br(value, 1)} dias" if value else "—")
    st.subheader("Ranking e concentração dos fornecedores")
    st.dataframe(
        display[
            ["fornecedor", "status", "ordens", "ordens_recebidas", "cotacoes", "valor_comprado", "valor_em_aberto", "participacao", "prazo_medio"]
        ].rename(
            columns={
                "fornecedor": "Fornecedor",
                "status": "Status",
                "ordens": "Ordens",
                "ordens_recebidas": "Recebidas",
                "cotacoes": "Cotações",
                "valor_comprado": "Valor comprado",
                "valor_em_aberto": "Aguardando recebimento",
                "participacao": "Participação",
                "prazo_medio": "Prazo médio",
            }
        ),
        width="stretch",
        hide_index=True,
    )


def _render_quotes_and_items(quotes: pd.DataFrame, items: pd.DataFrame, orders: pd.DataFrame) -> None:
    linked = int((quotes["ordens_vinculadas"] > 0).sum()) if not quotes.empty else 0
    approved = int((quotes["status"] == "aprovada").sum()) if not quotes.empty else 0
    open_quotes = int((quotes["status"] == "aberta").sum()) if not quotes.empty else 0
    refused = int((quotes["status"] == "recusada").sum()) if not quotes.empty else 0
    columns = st.columns(4)
    columns[0].metric("Cotações vinculadas", f"{linked} de {len(quotes)}")
    columns[1].metric("Abertas", open_quotes)
    columns[2].metric("Aprovadas", approved)
    columns[3].metric("Recusadas", refused)

    left, right = st.columns(2)
    with left:
        st.subheader("Cotações por situação")
        quote_status = quotes["status"].map(lambda value: _status_label(value, QUOTE_STATUS_LABELS)).value_counts()
        st.bar_chart(quote_status, horizontal=True, height=270)
    with right:
        st.subheader("Itens com maior valor")
        if items.empty:
            st.info("Nenhum item encontrado para o recorte selecionado.")
        else:
            top_items = items.groupby("insumo")["valor_total"].sum().sort_values(ascending=False).head(10)
            st.bar_chart(top_items, horizontal=True, height=270)

    st.subheader("Economia estimada por negociação")
    if orders.empty:
        st.info("Nenhuma ordem vinculada a cotação foi encontrada.")
    else:
        display = orders[orders["cotacao_id"].notna()].copy()
        display["percentual_economia"] = display.apply(
            lambda row: row["economia"] / row["valor_cotado"] * 100 if row["valor_cotado"] else 0.0,
            axis=1,
        )
        for column in ("valor_cotado", "valor_ordem", "economia"):
            display[column] = display[column].map(format_currency_br)
        display["percentual_economia"] = display["percentual_economia"].map(lambda value: f"{format_number_br(value, 1)}%")
        st.dataframe(
            display[["numero", "fornecedor", "obra", "valor_cotado", "valor_ordem", "economia", "percentual_economia"]].rename(
                columns={
                    "numero": "Ordem",
                    "fornecedor": "Fornecedor",
                    "obra": "Obra",
                    "valor_cotado": "Cotação",
                    "valor_ordem": "Compra",
                    "economia": "Economia estimada",
                    "percentual_economia": "Economia (%)",
                }
            ),
            width="stretch",
            hide_index=True,
        )

    st.subheader("Itens comprados")
    if items.empty:
        st.info("Nenhum item de ordem encontrado para os filtros selecionados.")
        return
    grouped = items.groupby("insumo", as_index=False).agg(
        quantidade=("quantidade", "sum"),
        valor_total=("valor_total", "sum"),
        ordens=("ordem_id", "nunique"),
    ).sort_values("valor_total", ascending=False)
    grouped["quantidade"] = grouped["quantidade"].map(lambda value: format_number_br(value, 3))
    grouped["valor_total"] = grouped["valor_total"].map(format_currency_br)
    st.dataframe(
        grouped.rename(columns={"insumo": "Insumo", "quantidade": "Quantidade", "valor_total": "Valor dos itens", "ordens": "Ordens"}),
        width="stretch",
        hide_index=True,
    )
    st.caption("Os valores dos itens são apresentados separadamente porque o painel encontrou ordens cuja soma dos itens difere do total informado na ordem.")


def render_purchases_dashboard(db: Session) -> None:
    st.header("Dashboard de Compras e Fornecedores", anchor="dashboard-compras-fornecedores")
    st.caption("Acompanhe valores comprados, andamento das ordens, desempenho dos fornecedores, cotações e itens sem procurar códigos internos.")
    orders, quotes, suppliers, items = load_purchases_dashboard_data(db)
    today = today_in_timezone(APP_SETTINGS.app_timezone)

    st.subheader("Filtros da análise")
    period = st.selectbox(
        "Período",
        ["Ano atual", "Últimos 12 meses", "Todo o histórico", "Personalizado"],
        key="purchases_dashboard_period",
    )
    default_start, default_end = purchase_period_bounds(period, today, orders, quotes)
    if period == "Personalizado":
        date_columns = st.columns(2)
        start = date_columns[0].date_input("Data inicial", value=default_start, key="purchases_dashboard_start")
        end = date_columns[1].date_input("Data final", value=default_end, key="purchases_dashboard_end")
    else:
        start, end = default_start, default_end
        st.caption(f"Período considerado: {start.strftime('%d/%m/%Y')} a {end.strftime('%d/%m/%Y')}")
    if start > end:
        st.error("A data inicial precisa ser anterior à data final.")
        return

    supplier_options = sorted(orders["fornecedor"].dropna().astype(str).unique().tolist())
    work_options = sorted(orders["obra"].dropna().astype(str).unique().tolist())
    status_options = sorted(orders["status"].dropna().astype(str).unique().tolist())
    filter_columns = st.columns(3)
    selected_suppliers = filter_columns[0].multiselect(
        "Fornecedores", supplier_options, placeholder="Todos os fornecedores", key="purchases_dashboard_suppliers"
    )
    selected_works = filter_columns[1].multiselect(
        "Obras", work_options, placeholder="Todas as obras", key="purchases_dashboard_works"
    )
    selected_status_labels = filter_columns[2].multiselect(
        "Situações das ordens",
        [_status_label(value, ORDER_STATUS_LABELS) for value in status_options],
        placeholder="Todas as situações",
        key="purchases_dashboard_statuses",
    )
    reverse_status = {_status_label(value, ORDER_STATUS_LABELS): value for value in status_options}
    selected_statuses = [reverse_status[label] for label in selected_status_labels]

    orders, quotes = filter_purchases(
        orders, quotes, start, end, selected_suppliers, selected_works, selected_statuses
    )
    if orders.empty:
        st.info("Nenhuma ordem de compra corresponde aos filtros selecionados.")
        return
    orders = _add_attention(orders, today)
    order_ids = orders["ordem_id"].astype(int).tolist()
    items = items[items["ordem_id"].isin(order_ids)].copy()

    _render_top_metrics(orders, quotes, suppliers)
    tabs = st.tabs(["Visão geral", "Pedidos e prazos", "Fornecedores", "Cotações e itens"])
    with tabs[0]:
        _render_overview(orders)
    with tabs[1]:
        _render_orders(orders, today)
    with tabs[2]:
        _render_suppliers(suppliers, orders, quotes, selected_suppliers)
    with tabs[3]:
        _render_quotes_and_items(quotes, items, orders)
