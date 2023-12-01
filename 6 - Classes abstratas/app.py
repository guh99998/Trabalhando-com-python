import os
from abc import ABC, abstractmethod

os.system('cls')


class Poligono(ABC):
    def metodo(self):
        print('método')

    @abstractmethod
    def lados(self):
        pass


class Triangulo(Poligono):
    def lados(self):
        print('eu tenho 3 lados')

class Quadrado(Poligono):
    def lados(self):
        print('eu tenho 4 lados')

Triangulo().lados()
Quadrado().lados()
