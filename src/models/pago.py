# Se hacen uso del Patron de Diseño Strategy, Polimorfismo (Con los metodos de pago) y del Principio de Responsabilidad Unica.

from abc import ABC, abstractmethod

class PagoStrategy(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass

class PagoEfectivo(PagoStrategy):
    def pagar(self, monto):
        return f"Pago en efectivo recibido: ${monto:.2f}"

class PagoTarjeta(PagoStrategy):
    def pagar(self, monto):
        return f"Pago con tarjeta procesado: ${monto:.2f}"
