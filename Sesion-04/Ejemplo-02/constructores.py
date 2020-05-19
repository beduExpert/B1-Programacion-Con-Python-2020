#Ejemplo de clase con constructor y __str__
class Mascota:
    def __init__(self,especie = 'animal' , edad = 0):
        self.especie = especie
        self.edad = edad
    def __str__(self):
        return "Es un {} de {} años".format(self.especie, self.edad)

#Clases creadas con diferentes parámetros    
michi = Mascota(especie='gato', edad= 2)
print(michi)
rufo = Mascota(especie='perro')
print(rufo)
bicho = Mascota(edad=2)
print(bicho)