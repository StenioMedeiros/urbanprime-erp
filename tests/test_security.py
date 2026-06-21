from src.core.security.jwt_manager import create_access_token, decode_token
from src.core.security.password_manager import hash_password, verify_password


def test_hash_password():
    hashed = hash_password("Admin@123")
    assert hashed != "Admin@123"
    assert verify_password("Admin@123", hashed)


def test_jwt_access_token():
    token = create_access_token("1", {"username": "admin"})
    payload = decode_token(token)
    assert payload["sub"] == "1"
    assert payload["type"] == "access"
