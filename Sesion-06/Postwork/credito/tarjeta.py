import json

class Tarjeta_de_credito:

    def __init__(self, nombre='tarjeta', tasa= 0, deuda = 0, pagos = 0, cargos=0):
        self.__nombre=nombre
        self.__tasa = tasa
        self.__deuda = deuda
        self.__pagos = pagos
        self.__cargos = cargos

    def get_nombre(self):
        return self.__nombre
    

    def get_deuda(self):
        return self.__deuda

    def set_pagos(self, pagos):
        self.__pagos = pagos

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_pagos(self):
        return self.__pagos
    
    def set_deuda(self, deuda):
        self.__deuda = deuda

    def get_nueva_deuda(self):
        return self.__nueva_deuda

    def set_cargos(self, cargos):
        self.__cargos = cargos
        

    def crea_tarjeta(self):
        """
        Función que crea una tarjeta a partir de un formulario 
        """
        try:
            capturado = False
            while capturado == False:
                print("Inserta el nombre de tu tarjeta de crédito:")
                self.__nombre = input()

                print("Inserta la tasa de interes de la tarjeta:")
                self.__tasa = float(input())

                print("Inserta la deuda de la tarjeta en el último corte:")
                self.__deuda = int(input())

                print("Inserta el monto total de los pagos realizados durante el último mes:")
                self.__pagos = int(input())

                print("Inserta el monto total de las compras realizadas después del corte:")
                self.__cargos = int(input())

                if self.__pagos > self.__deuda:
                    print("ERROR: EL PRODUCTO NO PERMITE REALIZAR PAGOS MAYORES A LA DEUDA ACTUAL")
                    print("Vuelve a insertar los datos")
                else:
                    capturado = True
        except:
            print("Error: Dato no valido, vuelve a intentar")
            self.crea_tarjeta()


    def __calcula_nueva_deuda(self):
        """
        Función que calcula el nivel de deuda para el proximo mes
        """   
        tasa_decimal = self.__tasa/100
        interes_mensual = tasa_decimal/12
        self.__deuda_recalculada = (self.__deuda - self.__pagos)*(1+interes_mensual)
        self.__nueva_deuda = self.__deuda_recalculada + self.__cargos
        



    def imprime_reporte(self):
        """
        Función que imprime el reporte de una tarjeta 
        """
        self.__calcula_nueva_deuda()
        print("-------------------------------------------------------------------")
        print("Resumen de información sobre la tarjeta {}".format(self.__nombre))
        print("Tasa de interes del producto:                    {}".format(self.__tasa))
        print("Saldo de la tarjeta antes del corte              {}".format(self.__deuda))
        print("Total de pagos realizados:                       {}".format(self.__pagos))
        print("Deuda después del corte con intereses aplicados: {}".format(self.__deuda_recalculada))
        print("Cargos realizados después del corte:             {}".format(self.__cargos))
        print("Deuda actual:                                    {}".format(self.__nueva_deuda))
        print("-------------------------------------------------------------------")


    def pago_recurrente(self, monto):
        """
        Función que calcula un pago recurrente sobre la tarjeta con un mionto preestablecido, hasta que la tarjeta quede en cero 
        """
        self.__pagos = monto
        self.__cargos = 0
        while self.__deuda > 0:
            if self.__deuda < self.__pagos:
                self.__pagos = self.__deuda
            self.imprime_reporte()
            self.__deuda = self.__nueva_deuda

    def pagos_distintos(self, *args):
        """
        Función que calcula un pago recurrente sobre la tarjeta con distintos montos mes a mes 
        """
        self.__cargos = 0
        for arg in args:
            self.__pagos = arg
            if self.__deuda < self.__pagos:
                self.__pagos = self.__deuda
            self.imprime_reporte()
            self.__deuda = self.__nueva_deuda

    def get_reporte(self):
        """
        Función que devuelve el reporte de una tarjeta en formato str
        """
        self.__calcula_nueva_deuda()
        reporte = "-------------------------------------------------------------------\n"
        reporte = reporte + "Resumen de información sobre la tarjeta {}\n".format(self.__nombre)
        reporte = reporte + "Tasa de interes del producto:                    {}\n".format(self.__tasa)
        reporte = reporte + "Saldo de la tarjeta antes del corte              {}\n".format(self.__deuda)
        reporte = reporte + "Total de pagos realizados:                       {}\n".format(self.__pagos)
        reporte = reporte + "Deuda después del corte con intereses aplicados: {}\n".format(self.__deuda_recalculada)
        reporte = reporte + "Cargos realizados después del corte:             {}\n".format(self.__cargos)
        reporte = reporte + "Deuda actual:                                    {}\n".format(self.__nueva_deuda)
        reporte = reporte + "-------------------------------------------------------------------\n"
        return reporte

    def reporte_texto(self):
        """
        Función que crea un reporte en un archivo de texto
        """
        archivo = open("reporte_tarjeta_{}.txt".format(self.__nombre), 'w')
        texto = self.get_reporte()
        archivo.write(texto)
        archivo.close()

    def crea_json(self):
        datos = {'nombre': self.__nombre, 'tasa':self.__tasa, 'deuda': self.__deuda, 'pagos': self.__pagos, 'cargos':self.__cargos}
        with open("tarjeta_{}.json".format(self.__nombre), "w") as fjson: 
            json.dump(datos, fjson, indent=4)  

    def lee_json(self, archivo):
        with open(archivo, 'r') as fjson: 
            mi_json = json.load(fjson) 
            self.__nombre = mi_json['nombre']
            self.__tasa = mi_json['tasa']
            self.__deuda = mi_json['deuda']
            self.__pagos = mi_json['pagos']
            self.__cargos = mi_json['cargos']
            
    
