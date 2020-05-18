class Animal():
    def __init__(self, nombre='animal', especie='animal', sonido=''):
        self.nombre = nombre
        self.especie = especie
        self.sonido = sonido
    
    def grito(self):
        print("El {} hace {}".format(self.nombre, self.sonido))
    
    def info(self):
        print("Nombre: {} - Especie {}".format(self.nombre, self.especie))

class Pez(Animal):
    def __init__(self, nombre='pez', especie='pez'):
        super().__init__(nombre, especie, 'blooob')  # Extiende la clase

    def nadar(self):
        print("el {} está nadando".format(self.especie))

Nemo = Pez(nombre = 'Nemo', especie='pez payaso')
Nemo.info()
Nemo.nadar()
Nemo.grito()

