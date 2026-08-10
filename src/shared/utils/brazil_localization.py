from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from functools import lru_cache
import re
from zoneinfo import ZoneInfo


DEFAULT_BRAZIL_TIMEZONE = "America/Recife"

BRAZIL_STATES = (
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
    "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC",
    "SP", "SE", "TO",
)


@lru_cache
def timezone_for(name: str = DEFAULT_BRAZIL_TIMEZONE) -> ZoneInfo:
    return ZoneInfo(name)


def now_in_timezone(name: str = DEFAULT_BRAZIL_TIMEZONE) -> datetime:
    return datetime.now(timezone_for(name))


def now_local_naive(name: str = DEFAULT_BRAZIL_TIMEZONE) -> datetime:
    return now_in_timezone(name).replace(tzinfo=None)


def today_in_timezone(name: str = DEFAULT_BRAZIL_TIMEZONE) -> date:
    return now_in_timezone(name).date()


def as_local_datetime(value: datetime, name: str = DEFAULT_BRAZIL_TIMEZONE) -> datetime:
    if value.tzinfo is None:
        return value
    return value.astimezone(timezone_for(name))


def format_date_br(value: date) -> str:
    return value.strftime("%d/%m/%Y")


def format_datetime_br(value: datetime, name: str = DEFAULT_BRAZIL_TIMEZONE) -> str:
    return as_local_datetime(value, name).strftime("%d/%m/%Y %H:%M")


def format_number_br(value: Decimal | int | float | str, decimal_places: int = 2) -> str:
    number = Decimal(str(value))
    formatted = f"{number:,.{decimal_places}f}"
    return formatted.replace(",", "X").replace(".", ",").replace("X", ".")


def format_currency_br(value: Decimal | int | float | str) -> str:
    return f"R$ {format_number_br(value, 2)}"


def parse_number_br(value: str | Decimal | int | float) -> Decimal:
    if isinstance(value, Decimal):
        return value
    if isinstance(value, (int, float)):
        return Decimal(str(value))
    normalized = value.strip().replace("R$", "").replace(" ", "")
    if "," in normalized:
        normalized = normalized.replace(".", "").replace(",", ".")
    try:
        return Decimal(normalized)
    except InvalidOperation as exc:
        raise ValueError("Informe um número no formato brasileiro, como 1.234,56.") from exc


def format_competence_br(value: str) -> str:
    match = re.fullmatch(r"(\d{4})-(\d{2})", value.strip())
    return f"{match.group(2)}/{match.group(1)}" if match else value


def digits_only(value: str) -> str:
    return re.sub(r"\D", "", value)


def format_cpf(value: str) -> str:
    digits = digits_only(value)
    if len(digits) != 11:
        return value
    return f"{digits[:3]}.{digits[3:6]}.{digits[6:9]}-{digits[9:]}"


def format_cnpj(value: str) -> str:
    digits = digits_only(value)
    if len(digits) != 14:
        return value
    return f"{digits[:2]}.{digits[2:5]}.{digits[5:8]}/{digits[8:12]}-{digits[12:]}"


def format_cpf_cnpj(value: str) -> str:
    digits = digits_only(value)
    if len(digits) == 11:
        return format_cpf(digits)
    if len(digits) == 14:
        return format_cnpj(digits)
    return value


def format_cep(value: str) -> str:
    digits = digits_only(value)
    if len(digits) != 8:
        return value
    return f"{digits[:5]}-{digits[5:]}"


def format_phone_br(value: str) -> str:
    digits = digits_only(value)
    if len(digits) == 10:
        return f"({digits[:2]}) {digits[2:6]}-{digits[6:]}"
    if len(digits) == 11:
        return f"({digits[:2]}) {digits[2:7]}-{digits[7:]}"
    return value


def normalize_brazilian_field(field: str, value: str) -> str:
    normalized = value.strip()
    if field == "cpf":
        return format_cpf(normalized)
    if field == "cnpj":
        return format_cnpj(normalized)
    if field == "cpf_cnpj":
        return format_cpf_cnpj(normalized)
    if field == "cep":
        return format_cep(normalized)
    if field == "telefone":
        return format_phone_br(normalized)
    if field in {"estado", "placa"}:
        return normalized.upper()
    return normalized
