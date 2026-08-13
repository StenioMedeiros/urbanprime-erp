from datetime import date, time

import pandas as pd

from src.ui.hr_dashboard import (
    build_employee_summary,
    build_headcount_series,
    build_payroll_series,
    calculate_worked_hours,
    count_future_hr_events,
    filter_hr_data,
    headcount_at,
    hr_period_bounds,
)


def _employees() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "funcionario_id": 1,
                "nome": "Ana Souza",
                "data_nascimento": pd.Timestamp("1990-05-10"),
                "email_corporativo": "ana@empresa.com",
                "telefone": "(87) 99999-1111",
                "cargo": "Engenheira civil",
                "setor": "engenharia",
                "data_admissao": pd.Timestamp("2026-01-10"),
                "data_demissao": pd.NaT,
                "salario_base": 8_000.0,
                "status": "ativo",
            },
            {
                "funcionario_id": 2,
                "nome": "Bruno Lima",
                "data_nascimento": pd.Timestamp("1988-03-20"),
                "email_corporativo": "bruno@empresa.com",
                "telefone": "(87) 99999-2222",
                "cargo": "Mestre de obras",
                "setor": "obras",
                "data_admissao": pd.Timestamp("2026-02-01"),
                "data_demissao": pd.Timestamp("2026-07-31"),
                "salario_base": 5_000.0,
                "status": "inativo",
            },
        ]
    )


def _time_records() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "ponto_id": 1,
                "funcionario_id": 1,
                "nome": "Ana Souza",
                "setor": "engenharia",
                "data": pd.Timestamp("2026-08-05"),
                "entrada": time(8, 0),
                "saida_intervalo": time(12, 0),
                "retorno_intervalo": time(13, 0),
                "saida": time(18, 0),
                "observacao": None,
                "horas_trabalhadas": 9.0,
                "horas_extras_estimadas": 1.0,
                "jornada_incompleta": False,
            }
        ]
    )


def _payroll() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "folha_id": 1,
                "funcionario_id": 1,
                "nome": "Ana Souza",
                "setor": "engenharia",
                "competencia": "2026-08",
                "competencia_data": pd.Timestamp("2026-08-01"),
                "salario_bruto": 8_000.0,
                "descontos": 800.0,
                "salario_liquido": 7_200.0,
                "status": "pago",
            }
        ]
    )


def _allocations() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "alocacao_id": 1,
                "funcionario_id": 1,
                "nome": "Ana Souza",
                "setor": "engenharia",
                "obra_id": 10,
                "obra": "Residencial Garanhuns",
                "centro_custo_id": 10,
                "centro_custo": "Residencial Garanhuns",
                "funcao": "Responsável técnica",
                "data_inicio": pd.Timestamp("2026-01-10"),
                "data_fim": pd.NaT,
                "custo_hora": 40.0,
                "ativo": True,
            }
        ]
    )


def test_worked_hours_subtracts_break_and_supports_overnight_shift():
    assert calculate_worked_hours(time(8), time(12), time(13), time(18)) == 9.0
    assert calculate_worked_hours(time(22), None, None, time(6)) == 8.0
    assert calculate_worked_hours(time(8), None, None, None) is None


def test_hr_period_bounds_ignores_future_records_in_history():
    employees = _employees()
    time_records = _time_records()
    payroll = _payroll()
    allocations = _allocations()
    time_records.loc[len(time_records)] = {
        **time_records.iloc[0].to_dict(),
        "ponto_id": 2,
        "data": pd.Timestamp("2027-01-10"),
    }

    assert hr_period_bounds(
        "Ano atual", date(2026, 8, 13), employees, time_records, payroll, allocations
    ) == (date(2026, 1, 1), date(2026, 8, 13))
    assert hr_period_bounds(
        "Todo o histórico", date(2026, 8, 13), employees, time_records, payroll, allocations
    ) == (date(2026, 1, 10), date(2026, 8, 13))


def test_filter_hr_data_applies_human_filters_and_work_relationship():
    employees, time_records, payroll, allocations = filter_hr_data(
        _employees(),
        _time_records(),
        _payroll(),
        _allocations(),
        date(2026, 1, 1),
        date(2026, 8, 13),
        selected_employees=[],
        selected_sectors=["engenharia"],
        selected_roles=[],
        selected_statuses=["ativo"],
        selected_works=["Residencial Garanhuns"],
    )

    assert employees["nome"].tolist() == ["Ana Souza"]
    assert len(time_records) == len(payroll) == len(allocations) == 1


def test_headcount_uses_admission_and_dismissal_dates():
    employees = _employees()

    assert headcount_at(employees, date(2026, 1, 31)) == 1
    assert headcount_at(employees, date(2026, 6, 30)) == 2
    assert headcount_at(employees, date(2026, 8, 31)) == 1
    series = build_headcount_series(employees, date(2026, 1, 1), date(2026, 8, 31))
    assert series.iloc[-1]["Quadro de funcionários"] == 1
    assert series["Admissões"].sum() == 2
    assert series["Desligamentos"].sum() == 1


def test_payroll_series_fills_month_without_payroll():
    payroll = _payroll()
    september = {**payroll.iloc[0].to_dict(), "folha_id": 2, "competencia": "2026-10", "competencia_data": pd.Timestamp("2026-10-01")}
    payroll.loc[len(payroll)] = september

    series = build_payroll_series(payroll).set_index("data")

    assert list(series.index) == list(pd.date_range("2026-08-01", "2026-10-01", freq="MS"))
    assert series.loc[pd.Timestamp("2026-09-01")].sum() == 0
    assert series.loc[pd.Timestamp("2026-10-01"), "Salário líquido"] == 7_200.0


def test_employee_summary_keeps_payroll_and_allocation_costs_separate():
    summary = build_employee_summary(
        _employees(), _time_records(), _payroll(), _allocations()
    ).set_index("funcionario_id")

    assert summary.loc[1, "horas_trabalhadas"] == 9.0
    assert summary.loc[1, "salario_liquido_periodo"] == 7_200.0
    assert summary.loc[1, "custo_hora_alocado"] == 40.0
    assert summary.loc[1, "atencao"] == "Regular"
    assert summary.loc[2, "atencao"] == "Sem folha no período"


def test_future_event_counter_reports_each_hr_source():
    employees = _employees()
    time_records = _time_records()
    payroll = _payroll()
    allocations = _allocations()
    employees.loc[0, "data_admissao"] = pd.Timestamp("2026-08-14")
    time_records.loc[0, "data"] = pd.Timestamp("2026-08-15")
    payroll.loc[0, "competencia_data"] = pd.Timestamp("2026-09-01")
    allocations.loc[0, "data_inicio"] = pd.Timestamp("2026-08-16")

    assert count_future_hr_events(
        employees, time_records, payroll, allocations, date(2026, 8, 13)
    ) == {
        "admissões": 1,
        "registros de ponto": 1,
        "folhas": 1,
        "alocações": 1,
    }
