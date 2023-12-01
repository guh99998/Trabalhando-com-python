#classe animal com nome e som, propertys e o setters
import os

os.system('cls')

class Animal:
    _total_animais = 0
    _total_barulhos = 0

    def __init__(self, nome: str, som: str):
        self._nome = nome.title()
        self._som = som.lower()
        self.adicionar_ao_valor()

    @classmethod
    def adicionar_ao_valor(cls) -> None:
        cls._total_animais += 1

    @classmethod
    def adicionar_ao_som(cls) -> None:
        cls._total_barulhos += 1

    @classmethod
    @property
    def total_animais(cls) -> int:
        return cls._total_animais

    @classmethod
    @property
    def total_barulhos(cls) -> int:
        return cls._total_barulhos

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome.title()

    def fazer_barulho(self) -> None:
        self.adicionar_ao_som()
        print(self.som)

    @property
    def som(self) -> str:
        return self._som

    @som.setter
    def som(self, som: int) -> None:
        self._som = som.lower()


cachorro = Animal('Luna', 'Auau')

gato = Animal('Gato', 'Miau')

cavalo = Animal('Horse', 'Cavaaalo')

cachorro.fazer_barulho()
gato.fazer_barulho()
cavalo.fazer_barulho()
cavalo.fazer_barulho()
cavalo.fazer_barulho()

print(Animal.total_animais)
print(Animal.total_barulhos)