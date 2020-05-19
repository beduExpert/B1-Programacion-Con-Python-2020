class Vehiculo:
    def __init__(self,ruedas = 0, medio = 'medio', velocidad = 'no se mueve'):
        self.__ruedas = ruedas
        self.__velocidad = velocidad
        self.__medio = medio
    def avanzar(self):
        print("El vehiculo se mueve a velocidad {}".format(self.__velocidad))
    def __str__(self):
        return "ruedas {}, medio: {}, velocidad:{}".format(self.__ruedas, self.__medio, self.__velocidad)
    def describir(self):
        print("Es un vehiculo de {} ruedas".format(self.__ruedas))
        print("se mueve a velocidad {}".format(self.__velocidad))
        print("Su medio es {}".format(self.__medio))


barco = Vehiculo(ruedas=0, medio='agua',velocidad='lenta')

avion = Vehiculo(ruedas=4, medio='aire',velocidad='rapida')

auto = Vehiculo(ruedas=4, medio='asfalto',velocidad='media')
barco.describir()

avion.describir()

auto.describir()

auto.avanzar()

print(avion)
#auto.__ruedas