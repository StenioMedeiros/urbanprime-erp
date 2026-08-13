from datetime import date

import pandas as pd

from src.ui.works_dashboard import (
    analysis_period_bounds,
    build_work_start_series,
    filter_works,
    work_attention,
)


def test_work_attention_prioritizes_inconsistent_and_late_records():
    today = date(2026, 8, 13)
    assert work_attention("concluida", 0, date(2026, 9, 1), 0, None, 0, today) == "Dados inconsistentes"
    assert work_attention("em_andamento", 70, date(2026, 8, 1), 0, None, 0, today) == "Atrasada"
    assert work_attention("em_andamento", 70, date(2026, 12, 1), 1, None, 0, today) == "Etapas atrasadas"
    assert work_attention("em_andamento", 70, date(2026, 12, 1), 0, None, 1, today) == "Atenção técnica"


def test_work_attention_recognizes_healthy_and_completed_works():
    today = date(2026, 8, 13)
    assert work_attention("concluida", 100, date(2026, 8, 1), 0, date(2026, 8, 1), 0, today) == "Concluída"
    assert work_attention("em_andamento", 70, date(2027, 3, 1), 0, None, 0, today) == "Em dia"


def test_filter_works_uses_period_intersection_and_human_filters():
    works = pd.DataFrame(
        [
            {"obra": "Galpão", "responsavel": "Ana", "status": "em_andamento", "data_inicio": pd.Timestamp("2026-01-01"), "data_previsao_fim": pd.Timestamp("2026-12-01"), "data_fim": pd.NaT},
            {"obra": "Residência", "responsavel": "Bruno", "status": "concluida", "data_inicio": pd.Timestamp("2025-01-01"), "data_previsao_fim": pd.Timestamp("2025-06-01"), "data_fim": pd.Timestamp("2025-06-01")},
        ]
    )
    filtered = filter_works(
        works,
        date(2026, 1, 1),
        date(2026, 8, 13),
        ["Galpão"],
        ["Ana"],
        ["em_andamento"],
    )
    assert filtered["obra"].tolist() == ["Galpão"]


def test_monthly_work_series_counts_new_and_accumulated_works():
    works = pd.DataFrame(
        {"data_inicio": pd.to_datetime(["2026-01-02", "2026-01-20", "2026-03-05"])}
    )
    series = build_work_start_series(works)
    assert series["Novas obras"].tolist() == [2, 0, 1]
    assert series["Total acumulado"].tolist() == [2, 2, 3]


def test_analysis_period_uses_brazilian_current_year():
    works = pd.DataFrame(columns=["data_inicio", "data_previsao_fim", "data_fim"])
    assert analysis_period_bounds("Ano atual", date(2026, 8, 13), works) == (
        date(2026, 1, 1),
        date(2026, 8, 13),
    )
