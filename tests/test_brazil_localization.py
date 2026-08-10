from datetime import UTC, date, datetime
from decimal import Decimal

from src.shared.utils.brazil_localization import (
    format_cep,
    format_competence_br,
    format_cpf_cnpj,
    format_currency_br,
    format_date_br,
    format_datetime_br,
    format_month_name_br,
    format_month_year_br,
    format_phone_br,
    parse_number_br,
)
from src.ui.financial_dashboard import _chart_locale_pt_br


def test_formats_values_using_brazilian_conventions():
    assert format_date_br(date(2026, 8, 10)) == "10/08/2026"
    assert format_currency_br(Decimal("1234567.8")) == "R$ 1.234.567,80"
    assert format_competence_br("2026-08") == "08/2026"
    assert parse_number_br("1.234,56") == Decimal("1234.56")


def test_formats_every_month_in_portuguese():
    expected = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
    assert [format_month_name_br(month, abbreviated=True) for month in range(1, 13)] == expected
    assert format_month_year_br(date(2026, 2, 1)) == "fev/2026"
    assert format_month_year_br(date(2026, 8, 1), abbreviated=False) == "agosto de 2026"


def test_dashboard_chart_uses_brazilian_calendar_and_number_symbols():
    locale = _chart_locale_pt_br().to_dict()
    assert locale["time"]["shortMonths"] == [
        "jan", "fev", "mar", "abr", "mai", "jun",
        "jul", "ago", "set", "out", "nov", "dez",
    ]
    assert locale["number"]["decimal"] == ","
    assert locale["number"]["thousands"] == "."
    assert locale["number"]["currency"] == ["R$ ", ""]


def test_converts_aware_datetime_to_pernambuco_time():
    utc_value = datetime(2026, 8, 10, 18, 30, tzinfo=UTC)
    assert format_datetime_br(utc_value, "America/Recife") == "10/08/2026 15:30"


def test_formats_common_brazilian_identifiers():
    assert format_cpf_cnpj("90000013000101") == "90.000.013/0001-01"
    assert format_cpf_cnpj("12345678901") == "123.456.789-01"
    assert format_cep("55292310") == "55292-310"
    assert format_phone_br("87999130404") == "(87) 99913-0404"
