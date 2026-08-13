from datetime import date

from src.ui.dashboard_hub import (
    dashboard_is_available,
    dashboard_names,
    executive_period_bounds,
    executive_previous_period_bounds,
    percent_delta,
    previous_period_bounds,
)


def test_dashboard_center_exposes_all_sector_views():
    assert dashboard_names() == [
        "Executivo",
        "Financeiro e Fluxo de Caixa",
        "Obras e Engenharia",
        "Compras e Fornecedores",
        "Estoque",
        "Frota e Maquinário",
        "Recursos Humanos",
    ]


def test_only_completed_dashboards_are_marked_as_available():
    assert dashboard_is_available("Executivo")
    assert dashboard_is_available("Financeiro e Fluxo de Caixa")
    assert dashboard_is_available("Obras e Engenharia")
    assert dashboard_is_available("Compras e Fornecedores")
    assert dashboard_is_available("Estoque")
    assert not dashboard_is_available("Frota e Maquinário")


def test_executive_period_comparison_uses_equivalent_previous_months():
    start, end = executive_period_bounds("Últimos 6 meses", date(2026, 8, 13))
    previous_start, previous_end = executive_previous_period_bounds("Últimos 6 meses", start, end)

    assert (start, end) == (date(2026, 3, 1), date(2026, 8, 13))
    assert (previous_start, previous_end) == (date(2025, 9, 1), date(2026, 2, 13))


def test_custom_comparison_keeps_the_same_duration():
    previous_start, previous_end = previous_period_bounds(date(2026, 8, 1), date(2026, 8, 13))
    assert (previous_start, previous_end) == (date(2026, 7, 19), date(2026, 7, 31))


def test_percent_delta_handles_growth_drop_and_zero_base():
    assert percent_delta(120, 100) == 20
    assert percent_delta(80, 100) == -20
    assert percent_delta(0, 0) is None
    assert percent_delta(10, 0) == 100
