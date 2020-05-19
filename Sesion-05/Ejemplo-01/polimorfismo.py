#Se pueden crear métodos con el mismo nombre para distintas clases, implicando un comportamiento distinto
class Persona:
    def saludar(self):
        print("Hola!")

class Perro:
    def saludar(self):
        print("Guau!")

Daniel = Persona()
forest = Perro()

#Al llamar saludar, el comportamiento depende de cada clase
Daniel.saludar()
forest.saludar()

lista = [Daniel, forest]  # Clases distintas
#Al ejecutar saludar iterando la lista, se hará de acuerdo a la definición para cada clase
for objeto in lista:
    objeto.saludar()