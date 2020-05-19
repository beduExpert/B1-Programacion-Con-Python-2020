class Vehiculo:
    def describir(self):
        print("Es un vehiculo de {} ruedas".format(self.ruedas))
        print("se mueve a velocidad {}".format(self.velocidad))
        print("Su medio es {}".format(self.medio))

barco = Vehiculo()
barco.ruedas=0
barco.velocidad='lenta'
barco.medio = 'agua' 
barco.describir()

Avion = Vehiculo()
Avion.ruedas=4
Avion.velocidad='rapido'
Avion.medio = 'aire' 
Avion.describir()

auto = Vehiculo()
auto.ruedas=4
auto.velocidad='media'
auto.medio = 'asfalto' 
auto.describir()
