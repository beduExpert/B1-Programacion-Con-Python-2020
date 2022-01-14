

## Herencia

### OBJETIVO

- Conocer el concepto de herencia de POO
- Escribir clases heredadas

#### REQUISITOS

1. Python 3

#### DESARROLLO

Proceso en el cual una clase, obtiene los atributos y métodos de otra(s), y para opcionalmente extenderlos y cambiarlos. La nueva clase se conoce como hija y la que se toma como base como padre.

```python
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
#Metodos de clase padre
Nemo.info()
Nemo.nadar()
Nemo.grito()

```

En este caso, Pez, aparte de su método nadar, puede utilizar los métodos de Animal.
Por su parte, `__init__`, cambió su funcionalidad.

Para extender su funcionalidad, se puede utilizar la función super, la cual 
manda llamar el método del padre, para antes o después agregar código extra:

```python

class Humano(Animal):

    def grito(self):
        super().grito()
        print("Despues de gritar, al humano le duele la garganta.")

pancho = Humano("Pancho", "Homo sapiens", "AAAAAAA")
pancho.grito()
```