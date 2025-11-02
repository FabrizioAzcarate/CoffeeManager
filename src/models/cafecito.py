from models.bebida import Bebida

# Tiene las subclases heredadas de "bebida.py"
# Se hace uso de la herencia y del polimorfismo, ya que se implementan distintas tipos de cafés con el mismo metodo ("preparar")
# Se cumple con el Principio de Responsabilidad de Liskov, porque todas las subclases pueden usarse como una bebida.

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
