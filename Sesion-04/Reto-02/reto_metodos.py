class Vehiculo:
    def __init__(self,ruedas = 0, medio = 'medio', velocidad = 'no se mueve'):
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.medio = medio
    def avanzar(self):
        print("El vehiculo se mueve a velocidad {}".format(self.velocidad))
    def __str__(self):
        return "ruedas {}, medio: {}, velocidad:{}".format(self.ruedas, self.medio, self.velocidad)
    def describir(self):
        print("Es un vehiculo de {} ruedas".format(self.ruedas))
        print("se mueve a velocidad {}".format(self.velocidad))
        print("Su medio es {}".format(self.medio))


barco = Vehiculo(ruedas=0, medio='agua',velocidad='lenta')

avion = Vehiculo(ruedas=4, medio='aire',velocidad='rapida')

auto = Vehiculo(ruedas=4, medio='asfalto',velocidad='media')
barco.describir()

avion.describir()

auto.describir()

auto.avanzar()

print(avion)