import os

os.system('cls')

class Cliente:
    _total_clientes = 0

    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome.title()
        self._idade = idade
        self.adicionar_ao_valor()

    @classmethod
    def adicionar_ao_valor(cls) -> None:
        cls._total_clientes += 1

    @classmethod
    @property
    def total(cls) -> int:
        return cls._total_clientes

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome.title()

    @property
    def idade(self) -> int:
        return self._idade


alberto = Cliente('alberto frigATto', 20)
gustavo = Cliente('gustavo lopes', 21)

print(Cliente.total)
