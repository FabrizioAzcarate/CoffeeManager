from models.bebida import Bebida

class CafeLatte(Bebida):
    def __init__(self):
        super().__init__("Café Latte")

    def preparar(self):
        return f"Preparando {self._nombre}: espresso + leche vaporizada"

class CafeMocha(Bebida):
    def __init__(self):
        super().__init__("Café Mocha")

    def preparar(self):
        return f"Preparando {self._nombre}: espresso + chocolate + leche"

class Espresso(Bebida):
    def __init__(self):
        super().__init__("Espresso")

    def preparar(self):
        return f"Preparando {self._nombre}: espresso simple"
