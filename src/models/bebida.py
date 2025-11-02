from abc import ABC, abstractmethod

# En "bebida.py" se define una clase base para los tipos de bebidas del menú.
# Se cumple con el Principio de Responsabilidad Unica (SRP)

class Bebida(ABC):
    def __init__(self, nombre):
        # Acá se hace uso del encapsulamiento.
        self._nombre = nombre

    @abstractmethod
    def preparar(self):
        pass

    def nombre(self):
        return self._nombre
