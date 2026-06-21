def only_digits(value: str) -> str:
    return ''.join(ch for ch in value if ch.isdigit())
