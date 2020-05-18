
agrega el programa que se desarrollara con backticks> [agrega la sesion con backticks]

## Polimorfismo

### OBJETIVO

- Utilizar el polimorfismo eficientemente
- Realizar sobrecarga de funciones
- Realizar sobrecarga de operadores

#### REQUISITOS

1. Python 3

#### DESARROLLO

Se refiere a la habilidad de objetos de distintas clases a responder a un mismo mensaje. Puede ser mediante herencia o mediante clases diferentes, lo que se conoce en Python.

Por ejemplo, se puede llamar a un método con el mismo nombre y el comportamiento será distinto dependiendo de la clase

```
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

```
Una variante del polimorfismo es la sobrecarga de métodos, mediante la cuál en una clase hijo es posible re-escribir un método de la clase padre.

```
#En este ejemplo se sobrecarga el método mensaje
class Persona():
     def __init__(self):
       self.cedula = 13765890
     def mensaje(self):
         print("mensaje desde la clase Persona")

class Obrero(Persona):
     def __init__(self):
         self.__especialista = 1
     def mensaje(self):
         print("mensaje desde la clase Obrero")

obrero_planta = Obrero()
obrero_planta.mensaje()

```
De manera similar es posible sobrecargar algunos operadores

```

# Debido a que todas las clases heredan del objeto de clase, también es posible sobre cargar 
# algunos operadores

class Punto:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return x, y

punto1 = Punto(4,6)
punto2 = Punto(1,-2)
print (punto1 + punto2)

```