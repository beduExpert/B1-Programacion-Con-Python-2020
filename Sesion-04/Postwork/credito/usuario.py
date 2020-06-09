from credito.tarjeta import Tarjeta_de_credito


class usuario:
    def __init__(self, nombre='Usuario', tarjetas = []):
        self.__nombre = nombre
        self.__tarjetas = tarjetas
    
    def agrega_tarjeta(self, tarjeta):
        self.__tarjetas.append(tarjeta)
    
    def cancela_tarjeta(self, nombre):
        for tarjeta in self.__tarjetas:
            if tarjeta.get_nombre() == nombre:
                self.__tarjetas.remove(tarjeta)

    
    def multiples_reportes(self):
        """
        Función que imprime el reporte de todas las tarjetas de un usuario
        """
        print("Reporte del usuario:      {}".format(self.__nombre))
        for tarjeta in self.__tarjetas:
            tarjeta.imprime_reporte()