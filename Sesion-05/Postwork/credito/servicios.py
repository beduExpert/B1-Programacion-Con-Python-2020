from credito.tarjeta import Tarjeta_de_credito

def decorador_servicios(funcion):
    def nueva_funcion(*args, **kwargs):
        print("Se ignoraron los parámetros debido a que la tarjeta solo permite pagos totales, se muestra proyección con pago total")
        funcion(*args, **kwargs)
    return nueva_funcion

class Tarjeta_de_servicios(Tarjeta_de_credito):
    
    def __init__(self,nombre='tarjeta de servicio', deuda = 0, cargos=0):
        super().__init__(nombre=nombre, tasa = 0, deuda = deuda, pagos = deuda, cargos = cargos)

    def crea_tarjeta(self):
        """
        Función que crea una tarjeta a partir de un formulario 
        """
        capturado = False
        while capturado == False:
            print("Inserta el nombre de tu tarjeta de crédito:")
            self.__nombre = input()

            print("Inserta la deuda de la tarjeta en el último corte:")
            self.__deuda = int(input())

            print("Inserta el monto total de los pagos realizados durante el último mes:")
            self.__pagos = int(input())

            print("Inserta el monto total de las compras realizadas después del corte:")
            self.__cargos = int(input())

            if self.__pagos != self.__deuda:
                print("ERROR: CON LA TARJETA DE SERVICIOS DEBES PAGAR EL SALDO TOTAL!!!")
                print("Vuelve a insertar los datos")
            else:
                capturado = True


    
    def pago_recurrente(self, monto):
        """
        Función que calcula un pago recurrente sobre la tarjeta con un mionto preestablecido, hasta que la tarjeta quede en cero 
        """
        self.__pagos = super().__deuda
        self.__cargos = 0
        while self.__deuda > 0:
            if self.__deuda < self.__pagos:
                self.__pagos = self.__deuda
            self.imprime_reporte()
            self.__deuda = self.__nueva_deuda

    @decorador_servicios
    def pagos_distintos(self, *args):
        """
        Función que calcula un pago recurrente sobre la tarjeta con distintos montos mes a mes 
        """
        self.__cargos = 0
        self.__pagos = self.__deuda
        self.imprime_reporte()
        self.__deuda = self.__nueva_deuda

        
            

        
