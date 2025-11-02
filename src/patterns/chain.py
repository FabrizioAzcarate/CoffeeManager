class Handler:
    def __init__(self, siguiente=None):
        self._siguiente = siguiente

    def set_siguiente(self, siguiente):
        self._siguiente = siguiente

    def handle(self, pedido):
        handled = self._procesar(pedido)
        if not handled and self._siguiente:
            return self._siguiente.handle(pedido)
        return handled

    def _procesar(self, pedido):
        raise NotImplementedError
