from controllers.pedido_controller import PedidoController
from models.cafecito import CafeLatte, CafeMocha, Espresso
from models.pago import PagoEfectivo, PagoTarjeta

class MenuView:
    def __init__(self):
        self.controller = PedidoController()

    def mostrar(self):
        while True:
            print('\n--- Pedido Café ---')
            print('1. Crear un pedido')
            print('2. Listar los pedidos')
            print('0. Salir')
            op = input('Opción: ').strip()
            if op == '1':
                cliente = input('Nombre del cliente: ').strip()
                print('Tipos de cafés: 1) Latte 2) Mocha 3) Espresso')
                tipo = input('Seleccione tipo (1/2/3): ').strip()
                bebida = Espresso()
                if tipo == '1':
                    bebida = CafeLatte()
                elif tipo == '2':
                    bebida = CafeMocha()
                tamano = input('Tamaño (S/M/L): ').strip().upper() or 'M'
                extras = []
                while True:
                    ex = input('Agregar extra (o Enter para terminar): ').strip()
                    if not ex:
                        break
                    extras.append(ex)
                print('Métodos de pago: efectivo / tarjeta')
                mp = input('Seleccione un método: ').strip().lower()
                metodo = None
                if mp == 'efectivo':
                    metodo = PagoEfectivo()
                elif mp == 'tarjeta':
                    metodo = PagoTarjeta()
                pedido = self.controller.crear_pedido(cliente, bebida, tamano, extras, metodo)
                print('\nPedido creado:')
                print('Cliente:', pedido.cliente())
                print('Descripcion:', pedido.descripcion())
            elif op == '2':
                pedidos = self.controller.listar_pedidos()
                if not pedidos:
                    print('No hay pedidos.')
                for i,p in enumerate(pedidos,1):
                    print(f'[{i}] {p.cliente()} - {p.descripcion()}')
            elif op == '0':
                print('Saliendo. Tenga un buen día.')
                break
            else:
                print('Opción no válida.')
