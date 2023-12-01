import os
from abc import ABC

os.system('cls')

class Cliente(ABC):
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome.title()
        self._idade = idade

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome.title()

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, idade: str) -> None:
        self._idade = idade.title()

class ClientePF(Cliente):
    def __init__(self, nome: str, idade: int, cpf: str) -> None:
        super().__init__(nome, idade)
        self._cpf = cpf

    @property
    def cpf(self) -> int:
        return self._cpf

    @cpf.setter
    def cpf(self, cpf: str) -> None:
        self._cpf = cpf

alberto = ClientePF('alberto frigatto', 20, '12345678912')
print(alberto.idade)
