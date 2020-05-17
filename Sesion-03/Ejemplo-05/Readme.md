
agrega el programa que se desarrollara con backticks> [agrega la sesion con backticks]

## Docstrings

### OBJETIVO

- Utilizar docstrings

#### REQUISITOS

1. Python 3

#### DESARROLLO

Cuando escribimos software es de utilidad dar una ayuda a quien podria consumirlos, para esto nos sirven los docstrings.

Los docstrings se generan entre comillas triples

Para agregar ayuda general en un paquete, se hace en el archivo __init__.py
```
"""Paquete de funciones sencillas"""
```
Para agregarla en un modulo, se hace en la parte superior
Para funciones, debajo de su nombre
```
#Aplicaciones extras
def tabla(n):
    #Imprime la tabla de multiplicar del numero introducido
    for i in range(1,11):
        print("{} x {} = {}".format(n, i, n * i))
```
Para solicitar la ayuda incluida dentro del docstring usa help()
```

from matematicas import aritmetica
help(aritmetica)
help(aritmetica.suma)
```

