
agrega el programa que se desarrollara con backticks> [agrega la sesion con backticks]

## Metodos

### OBJETIVO

- Incluir metodos dentro de las clases
- Incluir constructores o inicializadores
- Incluir destructores y otros metodos integrados

#### REQUISITOS

1. Python 3

#### DESARROLLO

Los métodos son funciones asociadas al comportamiento de los objetos de cierta clase, deben definirse usando init en el cuerpo de la clase.

En el ejemplo  persona.py se crearon tres metodos 

```
class persona():
    def asignar_nombre(self,nombre):
        self.nombre = nombre
    def saluda(self):
        print("hola, soy {}".format(self.nombre))
    def get_nombre(self):
        return self.nombre
```
Como las funciones, los metodos pueden tener parametros (ver asignar_nombre) o retornar valores (ver get_nombre).

La palabra self, apunta a los atributos y métodos de la clase. Es importante incluirla en la definición de los métodos.

```

Todas las clases en Python 3 cuentan con ciertos métodos integrados, que sirven de apoyo y mejor uso de los objetos. Algunas importantes son:

- __init__ - Llamada al crear un objeto, se le conoce como constructor o inicializador.
-  __del__ - Llamada a punto de destruir un objeto, se le conoce como destructor.
- __str__ - Representación en string de un objeto. 
- __bool__ - Para evaluar el objeto como booleano.

```
class MiClase():
    def __init__(self):
        print("Objeto de clase MiClase creado")
    
    def __del__(self):
        print("Objeto de clase MiClase destruido")
    
    def __str__(self):
        return "Objeto de clase MiClase"

#Llama a __init__
objeto = MiClase()

#Llama a _str__
print(objeto)

#__del__ se llama automaticamente cuando el objeto ya no se utilizará, en este caso al final del programa


```

Usualmente en el constructor se obtienen parametros de la clase, a diferencia de otros lenguajes de programación en Python no se pueden incluir múltiples constructores, pero si se usan parametros nombrados, se pueden poner valores por default.

Se muestra un ejemplo en constructores.py
```
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
```



