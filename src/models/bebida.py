from abc import ABC, abstractmethod

class Bebida(ABC):
    def __init__(self, nombre):
        self._nombre = nombre

    @abstractmethod
    def preparar(self):
        pass

    def nombre(self):
        return self._nombre
