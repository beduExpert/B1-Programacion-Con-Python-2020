
agrega el programa que se desarrollara con backticks> [agrega la sesion con backticks]

## Clases y objetos

### OBJETIVO

- Crear objetos a partir de una clase base
- Realizar la declaración de una clase

#### REQUISITOS

1. Python 3
#### DESARROLLO

La programación orientada a objetos (POO) es un paradigma de programación basado en el mundo real. Las partes básicas son clases y objetos, así como su interacción entre ellas en nuestro programa.



- Clase: Definición genérica a partir de la cual se elaboran objetos.

- Objeto es una instancia de una clase. Entre ellas, sus atributos pueden ser tener diferentes valores.

Se puede pensar una clase como una plantilla usada para crear objetos.

Al usar python muchos paquetes se basaran en la definicion de clase, por ejemplo podemos crear objetos para almacenar y manipular fechas usando el modulo datetime

```
#Importamos modulo que posee clases para fecha
import datetime

#Se crea un objeto date con fechas determinadas
fecha = datetime.date(1937, 10, 8)  #year, month, day
print(fecha)

#Al preguntar el tipo del objeto devuelve clase fecha
print(type (fecha))

#Podemos acceder a elementosdentro del objeto
mes = fecha.month
anyo = fecha.year
print("el mes es:" , mes)
print("el año es ", anyo)

#Las clases también contienen métodos, o funciones asociadas al comportamiento de la clase
print(fecha.strftime("%b %d %Y %H:%M:%S")) #Devuelve una cadena de texto con la fecha
```
Para crear una clase usamos la palabra reservada class, en su interior se definen metodos y atributos
```
#Para crear una clase usamos la palabra reservada class
#Para crear metodos usamos def
#self se refiere a los elementos(atributos y metodos) de la misma clase
class persona():
    def asignar_nombre(self,nombre):
        self.nombre = nombre
    def saluda(self):
        print("hola, soy {}".format(self.nombre))

#Crea objetos de clase persona
doctor = persona()
ingeniero = persona()

#Asignar a atributos
ingeniero.nombre = 'Gabriel'


#Usa Metodos de clase
doctor.asignar_nombre('Miguel')

#Accede a atributos
print(doctor.nombre)

ingeniero.saluda()
doctor.saluda()
```
