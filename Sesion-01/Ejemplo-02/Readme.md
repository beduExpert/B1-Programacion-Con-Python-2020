
## Variables y tipos de datos

## Objetivos

- Declarar variables, manipularlas y obtenerlas mediante `input`
- Usar los distintos tipos de datos disponibles en Python
- Utilizar funciones de cast para hacer conversiones de tipo

### Requisitos

1. Python 3

### Desarrollo

#### Variables

Una variable te permite asignar datos a un elemento:

```python
nombre = "Beto"
edad = 20
```

Las variables pueden tener cualquier nombre que no utilice el lenguaje. Tampoco pueden
comenzar con números, o llevar otro signo que sea el guión bajo.

### Tipos de datos en Python.
Python permite declarar cualquier tipo de dato en Python. Sin embargo, es importante
reconocer el tipo de dato con el cual trabajamos, debido a que es un lenguaje **fuertemente tipado**,
o sea, no suele convertir los datos por nosotros. Entre los datos básicos están:

* Numéricos:   
    - int: Números enteros.
    - float: Números con punto flotante.
    - complex: Numeros complejos.
* Texto:
    - string: Una o varios caracteres.
* Booleanos: True(Verdadero) o False(Falso).
* None: Sin ningún valor (vacío)

El programa `conversion_de_datos.py` Aborda los distintos tipos de datos en Python.

La función `type()` retorna el tipo de dato de la variable que tenga como argumento.
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

### Convirtiendo datos (casting)

Convertir datos de un tipo a otro es una tarea importante en Python. En algunas situaciones, por ejemplo,
al recibir datos por el usuario mediante `input`, siempre recibimos cadenas (str). Si en este caso, esperábamos un número (int o float),
entonces hay que convertirlo:

```python
numero = input("Ingresa un número entero: ")
numero_entero = int(numero)
numero_cuadrado = numero_entero ** 2
print("Tu numero al cuadrado es:", numero_cuadrado)
```

El programa `tipos_de_dato.py` muestra como realizar cast para manipular el tipo de dato de una variable.

* int() Cambia a tipo entero.
* float() Cambia a tipo float.
* str() Cambia a tipo string.

Si no se puede hacer el casting, recibiremos un error.

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


