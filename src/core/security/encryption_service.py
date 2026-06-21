from cryptography.fernet import Fernet

from src.core.config.settings import get_settings


class EncryptionService:
    def __init__(self):
        self._fernet = Fernet(get_settings().fernet_key.encode())

    def encrypt(self, value: str) -> str:
        return self._fernet.encrypt(value.encode()).decode()

    def decrypt(self, value: str) -> str:
        return self._fernet.decrypt(value.encode()).decode()
