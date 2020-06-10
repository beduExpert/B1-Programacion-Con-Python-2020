from credito.tarjeta import Tarjeta_de_credito
from credito.servicios import Tarjeta_de_servicios

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
    
    def get_nombre(self):
        return self.__nombre

    def get_tarjetas(self):
        return self.__tarjetas
    
    def num_tarjetas(self):
        return(str(len(self.__tarjetas)))

    
    def multiples_reportes(self):
        """
        Función que imprime el reporte de todas las tarjetas de un usuario
        """
        print("Reporte del usuario:      {}".format(self.__nombre))
        for tarjeta in self.__tarjetas:
            tarjeta.imprime_reporte()

    def reportes_texto(self):
        archivo = open("reporte_{}.txt".format(self.__nombre), "w") # w para escritura
        archivo.write("Reporte del usuario:      {}\n".format(self.__nombre))
        for tarjeta in self.__tarjetas:
            texto = tarjeta.get_reporte()
            archivo.write(texto)
        archivo.close() # Debemos cerrar el archivo

    def get_reportes_html(self):
        texto = "Reporte del usuario:      {}<br>".format(self.__nombre)
        for tarjeta in self.__tarjetas:
            texto = texto + tarjeta.get_reporte_html()
        return texto

