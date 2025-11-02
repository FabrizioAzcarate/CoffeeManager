# Aplican tanto el Principio de Responsabilidad Unica (SRP, al solamente representar pedidos) como el encapsulamiento.

class Pedido:
    def __init__(self, cliente=None, bebida=None, tamano='M', extras=None, metodo_pago=None):
        self._cliente = cliente
        self._bebida = bebida
        self._tamano = tamano
        self._extras = extras or []
        self._metodo_pago = metodo_pago

    def cliente(self):
        return self._cliente

    def bebida(self):
        return self._bebida

    def tamano(self):
        return self._tamano

    def extras(self):
        return list(self._extras)

    def metodo_pago(self):
        return self._metodo_pago

    def descripcion(self):
        parts = [f"{self._bebida.nombre()} ({self._tamano})"]
        if self._extras:
            parts.append("Extras: " + ", ".join(self._extras))
        return " | ".join(parts)
