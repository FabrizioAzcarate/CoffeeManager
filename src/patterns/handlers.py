from patterns.chain import Handler

class ValidarHandler(Handler):
    def _procesar(self, pedido):
        if not pedido.cliente():
            print('Validación: cliente faltante.')
            return False
        if not pedido.bebida():
            print('Validación: bebida faltante.')
            return False
        print('Validación: OK.')
        return False

class PrepararHandler(Handler):
    def _procesar(self, pedido):
        print('Preparación:', pedido.bebida().preparar())
        return False

class EntregarHandler(Handler):
    def _procesar(self, pedido):
        monto_aprox = 5.00
        if pedido.metodo_pago():
            print(pedido.metodo_pago().pagar(monto_aprox))
        print(f"Pedido para {pedido.cliente()} listo para entrega.")
        return True
