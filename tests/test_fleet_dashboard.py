from datetime import date

import pandas as pd

from src.ui.fleet_dashboard import (
    build_fleet_cost_series,
    build_fleet_summary,
    count_future_events,
    filter_fleet_data,
    fleet_attention,
    fleet_period_bounds,
)


def _fleet() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "frota_id": 1,
                "identificacao": "Escavadeira 01",
                "tipo": "escavadeira",
                "placa": None,
                "marca": "CAT",
                "modelo": "320",
                "ano_fabricacao": 2023,
                "data_aquisicao": pd.Timestamp("2024-01-10"),
                "valor_aquisicao": 500_000.0,
                "horimetro_atual": 320.0,
                "status": "em_uso",
                "obra_atual_id": 10,
                "obra_atual": "Residencial Garanhuns",
            },
            {
                "frota_id": 2,
                "identificacao": "Caminhão 02",
                "tipo": "caminhao",
                "placa": "ABC1D23",
                "marca": "VW",
                "modelo": "Constellation",
                "ano_fabricacao": 2022,
                "data_aquisicao": pd.Timestamp("2023-02-15"),
                "valor_aquisicao": 350_000.0,
                "horimetro_atual": 900.0,
                "status": "disponivel",
                "obra_atual_id": 20,
                "obra_atual": "Galpão Industrial",
            },
        ]
    )


def _maintenance() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "manutencao_id": 1,
                "frota_id": 1,
                "identificacao": "Escavadeira 01",
                "tipo_frota": "escavadeira",
                "fornecedor_id": 1,
                "fornecedor": "Oficina Garanhuns",
                "obra_id": 10,
                "obra": "Residencial Garanhuns",
                "tipo": "preventiva",
                "descricao": "Revisão",
                "data_entrada": pd.Timestamp("2026-08-03"),
                "data_saida": pd.Timestamp("2026-08-04"),
                "custo": 1_000.0,
                "horimetro": 300.0,
                "status": "concluida",
            }
        ]
    )


def _fuel() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "abastecimento_id": 1,
                "frota_id": 1,
                "identificacao": "Escavadeira 01",
                "tipo_frota": "escavadeira",
                "obra_id": 10,
                "obra": "Residencial Garanhuns",
                "responsavel_id": 1,
                "responsavel": "Ana Souza",
                "data_abastecimento": pd.Timestamp("2026-08-05"),
                "litros": 100.0,
                "valor_total": 600.0,
                "quilometragem_horimetro": 310.0,
                "observacao": None,
            }
        ]
    )


def _usage() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "utilizacao_id": 1,
                "frota_id": 1,
                "identificacao": "Escavadeira 01",
                "tipo_frota": "escavadeira",
                "obra_id": 10,
                "obra": "Residencial Garanhuns",
                "funcionario_id": 1,
                "operador": "Carlos Lima",
                "data_utilizacao": pd.Timestamp("2026-08-06"),
                "horas_utilizadas": 10.0,
                "horimetro_inicial": 310.0,
                "horimetro_final": 320.0,
                "custo_hora": 150.0,
                "custo_utilizacao": 1_500.0,
                "observacao": None,
            }
        ]
    )


def test_fleet_attention_prioritizes_data_and_operational_alerts():
    today = date(2026, 8, 13)
    assert fleet_attention("em_uso", 0, today, 100, 110, today) == "Horímetro divergente"
    assert fleet_attention("em_manutencao", 1, today, 110, 110, today) == "Em manutenção"
    assert fleet_attention("disponivel", 0, None, 110, 0, today) == "Sem utilização no período"
    assert fleet_attention("disponivel", 0, date(2026, 4, 1), 110, 100, today) == "Sem utilização há 90 dias"
    assert fleet_attention("em_uso", 0, today, 110, 100, today) == "Em uso"
    assert fleet_attention("disponivel", 0, today, 110, 100, today) == "Disponível"


def test_fleet_period_never_advances_beyond_today():
    maintenance = _maintenance()
    fuel = _fuel()
    usage = _usage()
    maintenance.loc[len(maintenance)] = {**maintenance.iloc[0].to_dict(), "data_entrada": pd.Timestamp("2026-12-01")}

    assert fleet_period_bounds("Ano atual", date(2026, 8, 13), maintenance, fuel, usage) == (
        date(2026, 1, 1),
        date(2026, 8, 13),
    )
    assert fleet_period_bounds("Todo o histórico", date(2026, 8, 13), maintenance, fuel, usage) == (
        date(2026, 8, 3),
        date(2026, 8, 13),
    )


def test_filter_fleet_data_applies_dates_asset_and_work_without_ids_from_user():
    fleet, maintenance, fuel, usage = filter_fleet_data(
        _fleet(),
        _maintenance(),
        _fuel(),
        _usage(),
        date(2026, 8, 1),
        date(2026, 8, 31),
        selected_assets=[],
        selected_types=["escavadeira"],
        selected_statuses=["em_uso"],
        selected_works=["Residencial Garanhuns"],
    )

    assert fleet["identificacao"].tolist() == ["Escavadeira 01"]
    assert len(maintenance) == len(fuel) == len(usage) == 1


def test_build_fleet_summary_separates_direct_and_appropriated_costs():
    summary = build_fleet_summary(
        _fleet(),
        _maintenance(),
        _fuel(),
        _usage(),
        date(2026, 8, 13),
    ).set_index("frota_id")

    assert summary.loc[1, "custo_direto"] == 1_600.0
    assert summary.loc[1, "custo_utilizacao"] == 1_500.0
    assert summary.loc[1, "custo_direto_hora"] == 160.0
    assert summary.loc[1, "consumo_hora"] == 10.0
    assert summary.loc[1, "atencao"] == "Em uso"
    assert summary.loc[2, "atencao"] == "Sem utilização no período"


def test_monthly_cost_series_fills_months_without_events():
    maintenance = _maintenance()
    fuel = _fuel()
    usage = _usage()
    fuel.loc[0, "data_abastecimento"] = pd.Timestamp("2026-10-05")

    series = build_fleet_cost_series(maintenance, fuel, usage).set_index("data")

    assert list(series.index) == list(pd.date_range("2026-08-01", "2026-10-01", freq="MS"))
    assert series.loc[pd.Timestamp("2026-09-01"), ["Manutenção", "Combustível", "Custo de utilização"]].sum() == 0
    assert series.loc[pd.Timestamp("2026-10-01"), "Combustível"] == 600.0


def test_future_event_counter_reports_each_operational_source():
    maintenance = _maintenance()
    fuel = _fuel()
    usage = _usage()
    maintenance.loc[0, "data_entrada"] = pd.Timestamp("2026-08-14")
    fuel.loc[0, "data_abastecimento"] = pd.Timestamp("2026-08-15")
    usage.loc[0, "data_utilizacao"] = pd.Timestamp("2026-08-16")

    assert count_future_events(maintenance, fuel, usage, date(2026, 8, 13)) == {
        "manutenções": 1,
        "abastecimentos": 1,
        "utilizações": 1,
    }
