from patterns.builder import PedidoBuilder
from patterns.singleton import SingletonMeta
from patterns.handlers import ValidarHandler, PrepararHandler, EntregarHandler

class Cafeteria(metaclass=SingletonMeta):
    def __init__(self):
        self.pedidos = []

    def procesar_pedido(self, pedido):
        validar = ValidarHandler()
        preparar = PrepararHandler()
        entregar = EntregarHandler()
        validar.set_siguiente(preparar)
        preparar.set_siguiente(entregar)
        validar.handle(pedido)
        self.pedidos.append(pedido)

class PedidoController:
    def __init__(self):
        self._cafeteria = Cafeteria()

    def crear_pedido(self, cliente, bebida, tamano, extras, metodo_pago):
        builder = PedidoBuilder()
        builder.con_cliente(cliente).con_bebida(bebida).con_tamano(tamano)
        for e in extras:
            builder.agregar_extra(e)
        builder.con_metodo_pago(metodo_pago)
        pedido = builder.build()
        self._cafeteria.procesar_pedido(pedido)
        return pedido

    def listar_pedidos(self):
        return list(self._cafeteria.pedidos)
