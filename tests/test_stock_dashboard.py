from datetime import date

import pandas as pd

from src.ui.stock_dashboard import (
    build_inventory_health,
    build_stock_movement_series,
    filter_stock_data,
    stock_attention,
    stock_period_bounds,
)


def test_stock_attention_prioritizes_balance_and_cost_problems():
    today = date(2026, 8, 13)
    assert stock_attention("ativo", 0, 10, 0, "2026-08-01", True, today) == "Sem saldo"
    assert stock_attention("ativo", 8, 10, 0, "2026-08-01", True, today) == "Abaixo do mínimo"
    assert stock_attention("ativo", 20, 10, 0, "2026-08-01", False, today) == "Sem valor unitário"


def test_stock_attention_distinguishes_risk_no_movement_and_healthy_stock():
    today = date(2026, 8, 13)
    assert stock_attention("ativo", 40, 15, 1, "2026-08-01", True, today) == "Risco em 30 dias"
    assert stock_attention("ativo", 100, 10, 0, None, True, today) == "Sem movimentação"
    assert stock_attention("ativo", 100, 10, 1, "2026-08-01", True, today) == "Estoque adequado"


def test_inventory_health_uses_only_outputs_from_the_last_30_days():
    inventory = pd.DataFrame(
        [
            {
                "insumo_id": 1,
                "insumo": "Cimento",
                "status": "ativo",
                "quantidade_atual": 40.0,
                "estoque_minimo": 15.0,
                "ultima_movimentacao": pd.Timestamp("2026-08-10"),
                "sem_valor_unitario": False,
            }
        ]
    )
    movements = pd.DataFrame(
        [
            {"insumo_id": 1, "tipo": "saida", "quantidade": 30.0, "data_movimentacao": pd.Timestamp("2026-08-01")},
            {"insumo_id": 1, "tipo": "saida", "quantidade": 100.0, "data_movimentacao": pd.Timestamp("2026-06-01")},
            {"insumo_id": 1, "tipo": "entrada", "quantidade": 50.0, "data_movimentacao": pd.Timestamp("2026-08-02")},
        ]
    )
    result = build_inventory_health(inventory, movements, date(2026, 8, 13)).iloc[0]
    assert result["consumo_30_dias"] == 30.0
    assert result["consumo_medio_diario"] == 1.0
    assert result["saldo_projetado_30_dias"] == 10.0
    assert result["atencao"] == "Risco em 30 dias"


def test_filter_stock_data_applies_period_material_work_and_type():
    inventory = pd.DataFrame(
        [
            {"insumo_id": 1, "insumo": "Cimento"},
            {"insumo_id": 2, "insumo": "Areia"},
        ]
    )
    movements = pd.DataFrame(
        [
            {"insumo_id": 1, "insumo": "Cimento", "obra": "Galpão", "tipo": "saida", "data_movimentacao": pd.Timestamp("2026-08-01")},
            {"insumo_id": 2, "insumo": "Areia", "obra": "Residência", "tipo": "entrada", "data_movimentacao": pd.Timestamp("2026-08-01")},
        ]
    )
    filtered_inventory, filtered_movements = filter_stock_data(
        inventory,
        movements,
        date(2026, 1, 1),
        date(2026, 8, 13),
        ["Cimento"],
        ["Galpão"],
        ["saida"],
    )
    assert filtered_inventory["insumo"].tolist() == ["Cimento"]
    assert filtered_movements["insumo"].tolist() == ["Cimento"]


def test_stock_movement_series_uses_estimated_values_without_mixing_units():
    movements = pd.DataFrame(
        {
            "data_movimentacao": pd.to_datetime(["2026-01-02", "2026-01-20", "2026-03-05"]),
            "tipo": ["entrada", "saida", "entrada"],
            "valor_estimado": [100.0, 40.0, 250.0],
        }
    )
    series = build_stock_movement_series(movements)
    assert series["Entradas"].tolist() == [100.0, 0.0, 250.0]
    assert series["Saídas"].tolist() == [40.0, 0.0, 0.0]


def test_stock_period_uses_brazilian_current_year():
    movements = pd.DataFrame(columns=["data_movimentacao"])
    assert stock_period_bounds("Ano atual", date(2026, 8, 13), movements) == (
        date(2026, 1, 1),
        date(2026, 8, 13),
    )
