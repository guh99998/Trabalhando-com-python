import re
from werkzeug.security import generate_password_hash
from src.db import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String
from flask import jsonify


class User(Base):
    __tablename__ = 'USUARIO'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(320), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(50), nullable=False)

    def __init__(self, *, name: str, email: str, password: str) -> None:
        self._validate_name(name)
        self._validate_email(email)
        self._validate_password(password)

        self.name = name.title()
        self.email = email
        self.password = generate_password_hash(password)

    def _validate_name(self, name: str) -> None:
        if not self._name_is_valid(name):
            raise Exception('Nome inválido')

    def _name_is_valid(self, name: str) ->  bool:
        return len(name) < 50 and bool(re.search(r'^[a-zA-ZáéíóúâêîôûãõüçñÁÉÍÓÚÂÊÎÔÛÃÕÜÇÑ ]+$', name))

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
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
