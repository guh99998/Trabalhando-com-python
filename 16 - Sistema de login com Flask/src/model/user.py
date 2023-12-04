import re
from werkzeug.security import generate_password_hash


class User:
    def __init__(self, *, name: str, email: str, password: str) -> None:
        self._validate_name(name)
        self._validate_email(email)
        self._validate_password(password)

        self._name = name.title()
        self._email = email
        self._password = generate_password_hash(password)

    def _validate_name(self, name: str) -> None:
        if not self._name_is_valid(name):
            raise Exception('Nome inválido')

    def _name_is_valid(self, name: str) ->  bool:
        return len(name) < 50 and bool(re.search(r'\D', name))

    def _validate_email(self, email: str) -> None:
        if not self._email_is_valid(email):
            raise Exception('Email inválido')

    def _email_is_valid(self, email: str) -> bool:
        return bool(re.search('^[A-Za-z0-9+_.-]+@([A-Za-z0-9]+\\.)+[A-Za-z]{2,}$', email))

    def _validate_password(self, password: str) -> None:
        if not self._password_is_valid(password):
            raise Exception('Senha inválida')

    def _password_is_valid(self, password: str) -> bool:
        regex = (
            r'^(?=.*[A-Z])'
            r'(?=.*[a-z])'
            r'(?=.*\d)'
            r'(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\-])'
            r'.{8,}$'
        )

        return bool(re.match(regex, password))

    def to_json(self) -> dict:
        return {
            'name': self._name,
            'email': self._email
        }

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def password(self) -> str:
        return self._password
