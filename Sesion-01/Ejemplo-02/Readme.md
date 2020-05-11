
agrega el programa que se desarrollara con backticks> [agrega la sesion con backticks]

## Titulo del Ejemplo

### OBJETIVO

- Usar los distintos tipos de datos deisponibles en Python
- Utiilizar funciones de cast para hacer conversiones de tipo

#### REQUISITOS

1. Python 3

#### DESARROLLO
El programa conversion_de_datos.py Aborda los distintos tipos de datos en Python.

La función type() retorna el tipo de dato de la variable que tenga como argumento.
```
#tipos de dato numéricos
entero = 4
print("El dato introducido contiene:")
print(entero)
print("Es de tipo:")
print(type(entero))


pi = 3.14159
print("El dato introducido contiene:")
print(pi)
print("Es de tipo:")
print(type(pi))

#Cadenas de texto
mensaje = "Hola Mundo"
print("El dato introducido contiene:")
print(mensaje)
print("Es de tipo:")
print(type(mensaje))

#Datos booleanos
verdadero = True
print("El dato introducido contiene:")
print(verdadero)
print("Es de tipo:")
print(type(verdadero))
```
El programa tipos_de_dato.py muestra como realizar cast para manipular el tipo de dato de una variable.
int() Cambia a tipo entero.

float() Cambia a tipo float.

str() Cambia a tipo string.

```
#Se puede definir números como cadenas si se encierran en comillas
numero1 = "100"
numero2 = "3.14159"
print(type(numero1))

#Para convertir a entero 
entero = int(numero1)
print(type(entero))

#Para convertir a flotante
flotante = float(numero2)
print(type(flotante))

#También se puede convertir un número a cadena de texto
num = 300
cadena = str(num)
print(type(cadena))
```


