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


INVENTORY_SQL = """
WITH movement_totals AS (
    SELECT
        insumo_id,
        COUNT(*)::numeric AS total_movimentacoes,
        COUNT(*) FILTER (WHERE tipo = 'entrada')::numeric AS total_entradas,
        COUNT(*) FILTER (WHERE tipo = 'saida')::numeric AS total_saidas,
        SUM(quantidade) FILTER (WHERE tipo = 'entrada')::numeric AS quantidade_entrada,
        SUM(quantidade) FILTER (WHERE tipo = 'saida')::numeric AS quantidade_saida,
        MAX(data_movimentacao) AS ultima_movimentacao
    FROM movimentacoes_estoque
    GROUP BY insumo_id
), pending_purchases AS (
    SELECT
        item.insumo_id,
        COUNT(DISTINCT ordem.id)::numeric AS ordens_pendentes,
        SUM(item.quantidade)::numeric AS quantidade_pendente,
        SUM(item.valor_total)::numeric AS valor_pendente
    FROM itens_ordem_compra item
    JOIN ordens_compra ordem ON ordem.id = item.ordem_compra_id
    WHERE ordem.status IN ('aberta', 'aprovada')
      AND item.insumo_id IS NOT NULL
    GROUP BY item.insumo_id
)
SELECT
    insumo.id AS insumo_id,
    insumo.nome AS insumo,
    insumo.descricao,
    insumo.unidade_medida,
    insumo.quantidade_atual::numeric AS quantidade_atual,
    insumo.estoque_minimo::numeric AS estoque_minimo,
    insumo.valor_unitario::numeric AS valor_unitario,
    (insumo.quantidade_atual * COALESCE(insumo.valor_unitario, 0))::numeric AS valor_estoque,
    insumo.status,
    (insumo.valor_unitario IS NULL) AS sem_valor_unitario,
    COALESCE(movimento.total_movimentacoes, 0)::numeric AS total_movimentacoes,
    COALESCE(movimento.total_entradas, 0)::numeric AS total_entradas,
    COALESCE(movimento.total_saidas, 0)::numeric AS total_saidas,
    COALESCE(movimento.quantidade_entrada, 0)::numeric AS quantidade_entrada,
    COALESCE(movimento.quantidade_saida, 0)::numeric AS quantidade_saida,
    movimento.ultima_movimentacao,
    COALESCE(compra.ordens_pendentes, 0)::numeric AS ordens_pendentes,
    COALESCE(compra.quantidade_pendente, 0)::numeric AS quantidade_pendente,
    COALESCE(compra.valor_pendente, 0)::numeric AS valor_pendente
FROM insumos insumo
LEFT JOIN movement_totals movimento ON movimento.insumo_id = insumo.id
LEFT JOIN pending_purchases compra ON compra.insumo_id = insumo.id
ORDER BY insumo.nome
"""


MOVEMENTS_SQL = """
SELECT
    movimento.id AS movimentacao_id,
    movimento.insumo_id,
    insumo.nome AS insumo,
    insumo.unidade_medida,
    insumo.valor_unitario::numeric AS valor_unitario,
    movimento.obra_id,
    obra.nome AS obra,
    movimento.tipo,
    movimento.quantidade::numeric AS quantidade,
    (movimento.quantidade * COALESCE(insumo.valor_unitario, 0))::numeric AS valor_estimado,
    movimento.data_movimentacao,
    movimento.observacao
FROM movimentacoes_estoque movimento
JOIN insumos insumo ON insumo.id = movimento.insumo_id
LEFT JOIN obras obra ON obra.id = movimento.obra_id
ORDER BY movimento.data_movimentacao DESC NULLS LAST, movimento.id DESC
"""


PENDING_PURCHASES_SQL = """
SELECT
    ordem.id AS ordem_id,
    ordem.numero AS ordem,
    ordem.status,
    ordem.data_emissao,
    item.insumo_id,
    COALESCE(insumo.nome, item.descricao) AS insumo,
    item.quantidade::numeric AS quantidade,
    item.valor_unitario::numeric AS valor_unitario,
    item.valor_total::numeric AS valor_total,
    COALESCE(NULLIF(fornecedor.nome_fantasia, ''), fornecedor.razao_social) AS fornecedor,
    ordem.obra_id,
    obra.nome AS obra
FROM itens_ordem_compra item
JOIN ordens_compra ordem ON ordem.id = item.ordem_compra_id
JOIN fornecedores fornecedor ON fornecedor.id = ordem.fornecedor_id
LEFT JOIN insumos insumo ON insumo.id = item.insumo_id
LEFT JOIN obras obra ON obra.id = ordem.obra_id
WHERE ordem.status IN ('aberta', 'aprovada')
ORDER BY ordem.data_emissao, ordem.numero, insumo
"""


MOVEMENT_LABELS = {
    "entrada": "Entrada",
    "saida": "Saída",
}


ORDER_STATUS_LABELS = {
    "aberta": "Aberta",
    "aprovada": "Aprovada",
}


INVENTORY_NUMERIC_COLUMNS = (
    "quantidade_atual",
    "estoque_minimo",
    "valor_unitario",
    "valor_estoque",
    "total_movimentacoes",
    "total_entradas",
    "total_saidas",
    "quantidade_entrada",
    "quantidade_saida",
    "ordens_pendentes",
    "quantidade_pendente",
    "valor_pendente",
)


def _query_frame(db: Session, sql: str) -> pd.DataFrame:
    return pd.read_sql_query(text(sql), db.connection())


def load_stock_dashboard_data(db: Session) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    inventory = _query_frame(db, INVENTORY_SQL)
    inventory["ultima_movimentacao"] = pd.to_datetime(inventory["ultima_movimentacao"], errors="coerce")
    for column in INVENTORY_NUMERIC_COLUMNS:
        inventory[column] = pd.to_numeric(inventory[column], errors="coerce").fillna(0.0)

    movements = _query_frame(db, MOVEMENTS_SQL)
    movements["data_movimentacao"] = pd.to_datetime(movements["data_movimentacao"], errors="coerce")
    for column in ("quantidade", "valor_unitario", "valor_estimado"):
        movements[column] = pd.to_numeric(movements[column], errors="coerce").fillna(0.0)

    pending = _query_frame(db, PENDING_PURCHASES_SQL)
    pending["data_emissao"] = pd.to_datetime(pending["data_emissao"], errors="coerce")
    for column in ("quantidade", "valor_unitario", "valor_total"):
        pending[column] = pd.to_numeric(pending[column], errors="coerce").fillna(0.0)
    return inventory, movements, pending


def _date_value(value: Any) -> date | None:
    if value is None or pd.isna(value):
        return None
    if isinstance(value, pd.Timestamp):
        return value.date()
    if isinstance(value, date):
        return value
    parsed = pd.to_datetime(value, errors="coerce")
    return None if pd.isna(parsed) else parsed.date()


def stock_attention(
    status: str,
    current_quantity: float,
    minimum_quantity: float,
    average_daily_output: float,
    last_movement: Any,
    has_unit_value: bool,
    today: date,
) -> str:
    last_date = _date_value(last_movement)
    if status != "ativo":
        return "Inativo"
    if not has_unit_value:
        return "Sem valor unitário"
    if current_quantity <= 0:
        return "Sem saldo"
    if current_quantity <= minimum_quantity:
        return "Abaixo do mínimo"
    projected_quantity = current_quantity - average_daily_output * 30
    if average_daily_output > 0 and projected_quantity <= minimum_quantity:
        return "Risco em 30 dias"
    if last_date is None:
        return "Sem movimentação"
    if last_date < today - timedelta(days=90):
        return "Sem giro há 90 dias"
    return "Estoque adequado"


def build_inventory_health(
    inventory: pd.DataFrame,
    movements: pd.DataFrame,
    today: date,
) -> pd.DataFrame:
    result = inventory.copy()
    cutoff = pd.Timestamp(today - timedelta(days=29))
    recent_outputs = movements[
        (movements["tipo"] == "saida")
        & movements["data_movimentacao"].between(cutoff, pd.Timestamp(today), inclusive="both")
    ]
    output_by_item = recent_outputs.groupby("insumo_id")["quantidade"].sum()
    result["consumo_30_dias"] = result["insumo_id"].map(output_by_item).fillna(0.0)
    result["consumo_medio_diario"] = result["consumo_30_dias"] / 30.0
    result["saldo_projetado_30_dias"] = (
        result["quantidade_atual"] - result["consumo_30_dias"]
    ).clip(lower=0.0)
    result["dias_ate_minimo"] = result.apply(
        lambda row: max((row["quantidade_atual"] - row["estoque_minimo"]) / row["consumo_medio_diario"], 0.0)
        if row["consumo_medio_diario"] > 0
        else float("inf"),
        axis=1,
    )
    result["atencao"] = result.apply(
        lambda row: stock_attention(
            str(row["status"]),
            float(row["quantidade_atual"]),
            float(row["estoque_minimo"]),
            float(row["consumo_medio_diario"]),
            row["ultima_movimentacao"],
            not bool(row["sem_valor_unitario"]),
            today,
        ),
        axis=1,
    )
    return result


def stock_period_bounds(
    period: str,
    today: date,
    movements: pd.DataFrame,
) -> tuple[date, date]:
    if period == "Ano atual":
        return date(today.year, 1, 1), today
    if period == "Últimos 90 dias":
        return today - timedelta(days=89), today
    if period == "Últimos 12 meses":
        start = (pd.Timestamp(today).to_period("M").start_time - pd.DateOffset(months=11)).date()
        return start, today
    dates = movements["data_movimentacao"].dropna().tolist() if not movements.empty else []
    if not dates:
        return date(today.year, 1, 1), today
    return min(dates).date(), max(max(dates).date(), today)


def filter_stock_data(
    inventory: pd.DataFrame,
    movements: pd.DataFrame,
    start: date,
    end: date,
    selected_materials: list[str],
    selected_works: list[str],
    selected_types: list[str],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    start_ts = pd.Timestamp(start)
    end_ts = pd.Timestamp(end)
    filtered_inventory = inventory.copy()
    filtered_movements = movements[
        movements["data_movimentacao"].between(start_ts, end_ts, inclusive="both")
    ].copy()
    if selected_materials:
        filtered_inventory = filtered_inventory[filtered_inventory["insumo"].isin(selected_materials)]
        filtered_movements = filtered_movements[filtered_movements["insumo"].isin(selected_materials)]
    if selected_works:
        filtered_movements = filtered_movements[filtered_movements["obra"].isin(selected_works)]
    if selected_types:
        filtered_movements = filtered_movements[filtered_movements["tipo"].isin(selected_types)]
    if selected_works or selected_types:
        material_ids = filtered_movements["insumo_id"].dropna().astype(int).unique().tolist()
        filtered_inventory = filtered_inventory[filtered_inventory["insumo_id"].isin(material_ids)]
    return filtered_inventory, filtered_movements


def build_stock_movement_series(movements: pd.DataFrame) -> pd.DataFrame:
    if movements.empty or movements["data_movimentacao"].dropna().empty:
        return pd.DataFrame(columns=["data", "Entradas", "Saídas"])
    work = movements.dropna(subset=["data_movimentacao"]).copy()
    work["data"] = work["data_movimentacao"].dt.to_period("M").dt.to_timestamp()
    work["Entradas"] = work["valor_estimado"].where(work["tipo"] == "entrada", 0.0)
    work["Saídas"] = work["valor_estimado"].where(work["tipo"] == "saida", 0.0)
    grouped = work.groupby("data", as_index=False)[["Entradas", "Saídas"]].sum()
    calendar = pd.DataFrame({"data": pd.date_range(grouped["data"].min(), grouped["data"].max(), freq="MS")})
    return calendar.merge(grouped, on="data", how="left").fillna(0.0)


def _movement_label(value: Any) -> str:
    return MOVEMENT_LABELS.get(str(value), str(value).replace("_", " ").title())


def _filter_pending_purchases(
    pending: pd.DataFrame,
    inventory: pd.DataFrame,
    selected_works: list[str],
) -> pd.DataFrame:
    if inventory.empty:
        return pending.iloc[0:0].copy()
    material_ids = inventory["insumo_id"].dropna().astype(int).tolist()
    result = pending[pending["insumo_id"].isin(material_ids)].copy()
    if selected_works:
        result = result[result["obra"].isin(selected_works)]
    return result


def _render_top_metrics(inventory: pd.DataFrame, movements: pd.DataFrame, pending: pd.DataFrame) -> None:
    total_value = float(inventory["valor_estoque"].sum())
    minimum_value = float((inventory["estoque_minimo"] * inventory["valor_unitario"]).sum())
    pending_value = float(pending["valor_total"].sum()) if not pending.empty else 0.0
    critical = int(inventory["atencao"].isin(["Sem saldo", "Abaixo do mínimo"]).sum())
    risk = int((inventory["atencao"] == "Risco em 30 dias").sum())
    without_movement = int(inventory["atencao"].isin(["Sem movimentação", "Sem giro há 90 dias"]).sum())
    entries = movements[movements["tipo"] == "entrada"]
    outputs = movements[movements["tipo"] == "saida"]

    first_row = st.columns(4)
    first_row[0].metric("Materiais analisados", len(inventory))
    first_row[1].metric("Materiais ativos", int((inventory["status"] == "ativo").sum()))
    first_row[2].metric("Abaixo do mínimo", critical, delta_color="inverse")
    first_row[3].metric("Risco em 30 dias", risk, delta_color="inverse")

    second_row = st.columns(3)
    second_row[0].metric("Valor do estoque atual", format_currency_br(total_value))
    second_row[1].metric("Valor correspondente ao mínimo", format_currency_br(minimum_value))
    second_row[2].metric("Compras pendentes de recebimento", format_currency_br(pending_value))

    third_row = st.columns(3)
    third_row[0].metric("Movimentações no período", len(movements))
    third_row[1].metric("Valor estimado das entradas", format_currency_br(float(entries["valor_estimado"].sum())))
    third_row[2].metric("Valor estimado das saídas", format_currency_br(float(outputs["valor_estimado"].sum())))

    fourth_row = st.columns(2)
    fourth_row[0].metric("Materiais com compra pendente", int(pending["insumo_id"].nunique()) if not pending.empty else 0)
    fourth_row[1].metric("Sem movimentação ou sem giro", without_movement, delta_color="inverse")


def _render_overview(inventory: pd.DataFrame, movements: pd.DataFrame) -> None:
    left, right = st.columns(2)
    with left:
        st.subheader("Situação dos materiais")
        status = inventory["atencao"].value_counts()
        st.bar_chart(status, horizontal=True, height=290)
    with right:
        st.subheader("Valor armazenado por material")
        values = inventory.set_index("insumo")["valor_estoque"].sort_values(ascending=False).head(12)
        st.bar_chart(values, horizontal=True, height=290)

    st.subheader("Evolução financeira das movimentações")
    series = build_stock_movement_series(movements)
    if series.empty:
        st.info("Não existem movimentações com data no período selecionado.")
    else:
        _render_monthly_line_chart(series.set_index("data")[["Entradas", "Saídas"]], height=350)
    st.caption("Os valores das movimentações são estimados pela quantidade movimentada multiplicada pelo valor unitário atual do material.")


def _inventory_ranking(inventory: pd.DataFrame) -> pd.DataFrame:
    attention_order = {
        "Sem saldo": 0,
        "Abaixo do mínimo": 1,
        "Risco em 30 dias": 2,
        "Sem valor unitário": 3,
        "Sem movimentação": 4,
        "Sem giro há 90 dias": 5,
        "Estoque adequado": 6,
        "Inativo": 7,
    }
    display = inventory.copy()
    display["ordem_atencao"] = display["atencao"].map(attention_order).fillna(99)
    display = display.sort_values(["ordem_atencao", "dias_ate_minimo", "insumo"])
    display["quantidade_atual"] = display["quantidade_atual"].map(lambda value: format_number_br(value, 3))
    display["estoque_minimo"] = display["estoque_minimo"].map(lambda value: format_number_br(value, 3))
    display["consumo_30_dias"] = display["consumo_30_dias"].map(lambda value: format_number_br(value, 3))
    display["saldo_projetado_30_dias"] = display["saldo_projetado_30_dias"].map(lambda value: format_number_br(value, 3))
    display["quantidade_pendente"] = display["quantidade_pendente"].map(lambda value: format_number_br(value, 3))
    display["valor_estoque"] = display["valor_estoque"].map(format_currency_br)
    display["cobertura"] = display["dias_ate_minimo"].map(
        lambda value: f"{format_number_br(value, 0)} dias" if pd.notna(value) and value != float("inf") else "Sem consumo recente"
    )
    display["ultima_movimentacao"] = display["ultima_movimentacao"].map(
        lambda value: value.strftime("%d/%m/%Y") if pd.notna(value) else "—"
    )
    return display[
        [
            "atencao", "insumo", "unidade_medida", "quantidade_atual", "estoque_minimo",
            "consumo_30_dias", "saldo_projetado_30_dias", "cobertura", "quantidade_pendente",
            "valor_estoque", "ultima_movimentacao",
        ]
    ].rename(
        columns={
            "atencao": "Situação gerencial",
            "insumo": "Material",
            "unidade_medida": "Unidade",
            "quantidade_atual": "Saldo atual",
            "estoque_minimo": "Estoque mínimo",
            "consumo_30_dias": "Saídas em 30 dias",
            "saldo_projetado_30_dias": "Saldo projetado",
            "cobertura": "Cobertura até o mínimo",
            "quantidade_pendente": "Quantidade em compra",
            "valor_estoque": "Valor armazenado",
            "ultima_movimentacao": "Última movimentação",
        }
    )


def _render_balances(inventory: pd.DataFrame) -> None:
    st.subheader("Saldos, consumo e cobertura estimada")
    st.caption(
        "A cobertura usa as saídas registradas nos últimos 30 dias. Quando não há consumo recente, o sistema não inventa uma previsão."
    )
    st.dataframe(
        _inventory_ranking(inventory),
        width="stretch",
        hide_index=True,
    )

    st.subheader("Saldo atual comparado ao estoque mínimo")
    comparison = inventory[["insumo", "quantidade_atual", "estoque_minimo"]].rename(
        columns={"insumo": "Material", "quantidade_atual": "Saldo atual", "estoque_minimo": "Estoque mínimo"}
    )
    st.bar_chart(comparison.set_index("Material"), horizontal=True, height=max(320, min(650, 36 * len(comparison))))


def _render_movements(movements: pd.DataFrame) -> None:
    st.subheader("Consumo e movimentação por obra")
    if movements.empty:
        st.info("Nenhuma movimentação corresponde aos filtros selecionados.")
        return
    by_work = movements.copy()
    by_work["obra"] = by_work["obra"].fillna("Sem obra vinculada")
    by_work["Movimentação"] = by_work["tipo"].map(_movement_label)
    chart = by_work.groupby(["obra", "Movimentação"])["valor_estimado"].sum().unstack(fill_value=0.0)
    st.bar_chart(chart, horizontal=True, height=max(320, min(620, 38 * len(chart))))

    st.subheader("Histórico das movimentações")
    display = movements.copy()
    display["tipo"] = display["tipo"].map(_movement_label)
    display["quantidade"] = display.apply(
        lambda row: f"{format_number_br(row['quantidade'], 3)} {row['unidade_medida']}", axis=1
    )
    display["valor_estimado"] = display["valor_estimado"].map(format_currency_br)
    st.dataframe(
        display[
            ["data_movimentacao", "tipo", "insumo", "quantidade", "obra", "valor_estimado", "observacao"]
        ].rename(
            columns={
                "data_movimentacao": "Data",
                "tipo": "Movimentação",
                "insumo": "Material",
                "quantidade": "Quantidade",
                "obra": "Obra",
                "valor_estimado": "Valor estimado",
                "observacao": "Observação",
            }
        ),
        width="stretch",
        hide_index=True,
        column_config={"Data": st.column_config.DateColumn(format="DD/MM/YYYY")},
    )


def _render_replenishment(inventory: pd.DataFrame, pending: pd.DataFrame) -> None:
    attention = inventory[
        inventory["atencao"].isin(
            ["Sem saldo", "Abaixo do mínimo", "Risco em 30 dias", "Sem valor unitário", "Sem movimentação", "Sem giro há 90 dias"]
        )
    ]
    critical = int(attention["atencao"].isin(["Sem saldo", "Abaixo do mínimo", "Risco em 30 dias"]).sum())
    data_attention = int(attention["atencao"].isin(["Sem valor unitário", "Sem movimentação", "Sem giro há 90 dias"]).sum())
    columns = st.columns(3)
    columns[0].metric("Materiais para reposição", critical, delta_color="inverse")
    columns[1].metric("Materiais para conferência", data_attention, delta_color="inverse")
    columns[2].metric("Ordens de compra pendentes", int(pending["ordem_id"].nunique()) if not pending.empty else 0)

    st.subheader("Alertas e recomendações")
    if attention.empty:
        st.success("Nenhum material exige reposição ou conferência no recorte atual.")
    else:
        display = attention.copy()
        display["quantidade_atual"] = display["quantidade_atual"].map(lambda value: format_number_br(value, 3))
        display["estoque_minimo"] = display["estoque_minimo"].map(lambda value: format_number_br(value, 3))
        display["quantidade_pendente"] = display["quantidade_pendente"].map(lambda value: format_number_br(value, 3))
        display["ultima_movimentacao"] = display["ultima_movimentacao"].map(
            lambda value: value.strftime("%d/%m/%Y") if pd.notna(value) else "—"
        )
        st.dataframe(
            display[["atencao", "insumo", "unidade_medida", "quantidade_atual", "estoque_minimo", "quantidade_pendente", "ultima_movimentacao"]].rename(
                columns={
                    "atencao": "Situação",
                    "insumo": "Material",
                    "unidade_medida": "Unidade",
                    "quantidade_atual": "Saldo atual",
                    "estoque_minimo": "Estoque mínimo",
                    "quantidade_pendente": "Quantidade em compra",
                    "ultima_movimentacao": "Última movimentação",
                }
            ),
            width="stretch",
            hide_index=True,
        )

    st.subheader("Compras aguardando recebimento")
    if pending.empty:
        st.info("Não existem itens de compra abertos ou aprovados para os materiais selecionados.")
        return
    display = pending.copy()
    display["status"] = display["status"].map(lambda value: ORDER_STATUS_LABELS.get(str(value), str(value).title()))
    display["quantidade"] = display["quantidade"].map(lambda value: format_number_br(value, 3))
    display["valor_total"] = display["valor_total"].map(format_currency_br)
    st.dataframe(
        display[["ordem", "status", "data_emissao", "insumo", "quantidade", "fornecedor", "obra", "valor_total"]].rename(
            columns={
                "ordem": "Ordem",
                "status": "Status",
                "data_emissao": "Emissão",
                "insumo": "Material",
                "quantidade": "Quantidade",
                "fornecedor": "Fornecedor",
                "obra": "Obra",
                "valor_total": "Valor dos itens",
            }
        ),
        width="stretch",
        hide_index=True,
        column_config={"Emissão": st.column_config.DateColumn(format="DD/MM/YYYY")},
    )
    st.caption("As compras pendentes são mostradas por material e unidade; quantidades de unidades diferentes não são somadas entre si.")


def render_stock_dashboard(db: Session) -> None:
    st.header("Dashboard de Estoque", anchor="dashboard-estoque")
    st.caption("Acompanhe saldos, valor armazenado, movimentações, consumo por obra, cobertura e necessidades de reposição.")
    inventory, movements, pending = load_stock_dashboard_data(db)
    today = today_in_timezone(APP_SETTINGS.app_timezone)

    st.subheader("Filtros da análise")
    period = st.selectbox(
        "Período",
        ["Ano atual", "Últimos 90 dias", "Últimos 12 meses", "Todo o histórico", "Personalizado"],
        key="stock_dashboard_period",
    )
    default_start, default_end = stock_period_bounds(period, today, movements)
    if period == "Personalizado":
        date_columns = st.columns(2)
        start = date_columns[0].date_input("Data inicial", value=default_start, key="stock_dashboard_start")
        end = date_columns[1].date_input("Data final", value=default_end, key="stock_dashboard_end")
    else:
        start, end = default_start, default_end
        st.caption(f"Período considerado: {start.strftime('%d/%m/%Y')} a {end.strftime('%d/%m/%Y')}")
    if start > end:
        st.error("A data inicial precisa ser anterior à data final.")
        return

    material_options = sorted(inventory["insumo"].dropna().astype(str).unique().tolist())
    work_options = sorted(movements["obra"].dropna().astype(str).unique().tolist())
    type_options = sorted(movements["tipo"].dropna().astype(str).unique().tolist())
    filter_columns = st.columns(3)
    selected_materials = filter_columns[0].multiselect(
        "Materiais", material_options, placeholder="Todos os materiais", key="stock_dashboard_materials"
    )
    selected_works = filter_columns[1].multiselect(
        "Obras", work_options, placeholder="Todas as obras", key="stock_dashboard_works"
    )
    selected_type_labels = filter_columns[2].multiselect(
        "Movimentações",
        [_movement_label(value) for value in type_options],
        placeholder="Entradas e saídas",
        key="stock_dashboard_types",
    )
    reverse_types = {_movement_label(value): value for value in type_options}
    selected_types = [reverse_types[label] for label in selected_type_labels]

    inventory, movements = filter_stock_data(
        inventory, movements, start, end, selected_materials, selected_works, selected_types
    )
    if inventory.empty:
        st.info("Nenhum material corresponde aos filtros selecionados.")
        return
    inventory = build_inventory_health(inventory, movements, today)
    pending = _filter_pending_purchases(pending, inventory, selected_works)

    st.caption("Os saldos exibidos são os saldos atuais. O período selecionado limita as movimentações e as análises de consumo.")
    _render_top_metrics(inventory, movements, pending)
    tabs = st.tabs(["Visão geral", "Saldos e cobertura", "Movimentações e obras", "Reposição e alertas"])
    with tabs[0]:
        _render_overview(inventory, movements)
    with tabs[1]:
        _render_balances(inventory)
    with tabs[2]:
        _render_movements(movements)
    with tabs[3]:
        _render_replenishment(inventory, pending)
