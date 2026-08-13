from datetime import date

import pandas as pd

from src.ui.purchases_dashboard import (
    build_purchase_series,
    filter_purchases,
    purchase_attention,
    purchase_period_bounds,
    supplier_summary,
)


def test_purchase_attention_prioritizes_registration_inconsistencies():
    today = date(2026, 8, 13)
    assert purchase_attention("recebida", "2026-07-01", "2026-07-02", None, 100, 100, today) == "Dados incompletos"
    assert purchase_attention("aberta", "2026-07-01", "2026-07-02", None, 100, 100, today) == "Situação inconsistente"
    assert purchase_attention("aprovada", "2026-08-01", "2026-08-02", None, 100, 80, today) == "Total divergente"


def test_purchase_attention_distinguishes_waiting_and_received_orders():
    today = date(2026, 8, 13)
    assert purchase_attention("aprovada", "2026-06-01", "2026-06-02", None, 100, 100, today) == "Aguardando há mais de 30 dias"
    assert purchase_attention("aprovada", "2026-08-01", "2026-08-02", None, 100, 100, today) == "Aguardando recebimento"
    assert purchase_attention("recebida", "2026-08-01", "2026-08-02", "2026-08-10", 100, 100, today) == "Recebida"


def test_filter_purchases_applies_period_and_human_filters():
    orders = pd.DataFrame(
        [
            {"ordem_id": 1, "cotacao_id": 10, "fornecedor": "Fornecedor A", "obra": "Galpão", "status": "aprovada", "data_emissao": pd.Timestamp("2026-07-01")},
            {"ordem_id": 2, "cotacao_id": 20, "fornecedor": "Fornecedor B", "obra": "Residência", "status": "recebida", "data_emissao": pd.Timestamp("2025-07-01")},
        ]
    )
    quotes = pd.DataFrame(
        [
            {"cotacao_id": 10, "fornecedor": "Fornecedor A", "obra": "Galpão", "data_cotacao": pd.Timestamp("2026-06-28")},
            {"cotacao_id": 20, "fornecedor": "Fornecedor B", "obra": "Residência", "data_cotacao": pd.Timestamp("2025-06-28")},
        ]
    )
    filtered_orders, filtered_quotes = filter_purchases(
        orders,
        quotes,
        date(2026, 1, 1),
        date(2026, 8, 13),
        ["Fornecedor A"],
        ["Galpão"],
        ["aprovada"],
    )
    assert filtered_orders["ordem_id"].tolist() == [1]
    assert filtered_quotes["cotacao_id"].tolist() == [10]


def test_purchase_series_groups_value_economy_and_order_count_by_month():
    orders = pd.DataFrame(
        {
            "ordem_id": [1, 2, 3],
            "data_emissao": pd.to_datetime(["2026-01-02", "2026-01-20", "2026-03-05"]),
            "valor_ordem": [80.0, 150.0, 200.0],
            "valor_cotado": [100.0, 140.0, 250.0],
        }
    )
    series = build_purchase_series(orders)
    assert series["Valor comprado"].tolist() == [230.0, 0.0, 200.0]
    assert series["Economia estimada"].tolist() == [20.0, 0.0, 50.0]
    assert series["Ordens emitidas"].tolist() == [2.0, 0.0, 1.0]


def test_supplier_summary_calculates_share_and_keeps_suppliers_without_orders():
    suppliers = pd.DataFrame(
        [
            {"fornecedor_id": 1, "fornecedor": "Fornecedor A", "status": "ativo"},
            {"fornecedor_id": 2, "fornecedor": "Fornecedor B", "status": "ativo"},
        ]
    )
    orders = pd.DataFrame(
        [
            {"ordem_id": 1, "fornecedor_id": 1, "fornecedor": "Fornecedor A", "status": "recebida", "valor_ordem": 300.0, "prazo_recebimento": 8.0},
        ]
    )
    quotes = pd.DataFrame([{"cotacao_id": 10, "fornecedor_id": 1}])
    summary = supplier_summary(suppliers, orders, quotes)
    assert summary["fornecedor"].tolist() == ["Fornecedor A", "Fornecedor B"]
    assert summary["participacao"].tolist() == [100.0, 0.0]
    assert summary["ordens"].tolist() == [1.0, 0.0]


def test_purchase_period_uses_brazilian_current_year():
    orders = pd.DataFrame(columns=["data_emissao"])
    quotes = pd.DataFrame(columns=["data_cotacao"])
    assert purchase_period_bounds("Ano atual", date(2026, 8, 13), orders, quotes) == (
        date(2026, 1, 1),
        date(2026, 8, 13),
    )
