from models.pedido import Pedido

class PedidoBuilder:
    def __init__(self):
        self._pedido = Pedido()

    def con_cliente(self, cliente):
        self._pedido._cliente = cliente
        return self

    def con_bebida(self, bebida):
        self._pedido._bebida = bebida
        return self

    def con_tamano(self, tamano):
        self._pedido._tamano = tamano
        return self

    def agregar_extra(self, extra):
        if not hasattr(self._pedido, '_extras') or self._pedido._extras is None:
            self._pedido._extras = []
        self._pedido._extras.append(extra)
        return self

    def con_metodo_pago(self, metodo):
        self._pedido._metodo_pago = metodo
        return self

    def build(self):
        return self._pedido
