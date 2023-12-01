import os
from abc import ABC

os.system('cls')

class Animal(ABC):

    def __init__(self, nome: str, som: str):
        self._nome = nome.title()
        self._som = som.lower()

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome.title()

    @property
    def som(self) -> str:
        return self._som

    @som.setter
    def som(self, som: int) -> None:
        self._som = som.lower()

class Cachorro(Animal):
    def __init__(self, nome: str, som: str, cor: str):
        super().__init__(nome, som)
        self._cor = cor

    @property
    def cor(self) -> str:
        return self._cor

    @cor.setter
    def cor(self, cor) -> str:
        self._cor = cor

class Gato(Animal):
    def __init__(self, nome: str, som: str, raca: str):
        super().__init__(nome, som)
        self._raca = raca

    @property
    def raca(self) -> str:
        return self._raca

    @raca.setter
    def raca(self, raca) -> str:
        self._raca = raca


gato = Gato('gatao', 'miau', 'vira lata')
cachorro = Cachorro('frida', 'auau', 'amarelo')

print(gato.nome)
print(gato.som)
print(gato._raca)
print(cachorro.nome)
print(cachorro.som)
print(cachorro._cor)