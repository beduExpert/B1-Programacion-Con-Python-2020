
agrega el programa que se desarrollara con backticks> [agrega la sesion con backticks]

## Paquetes

### OBJETIVO

- Crear paquetes
- Acceder a modulos y funciones que estan en paquetes

#### REQUISITOS

1. Python 3

#### DESARROLLO

Los paquetes nos permiten reunir varios modulos dentro de una carpeta, para que python reconozca una carpeta como un modulo, es necesario que tenga un archivo con nombre __init__.py (incluso puede estar vacio)

La siguiente imagen, muestra un ejemplo de estructura de un paquete

![imagen](https://www.tutorialesprogramacionya.com/pythonya/imagentema/foto231.jpg)

Para acceder a los elementos de un paquete usamos import, de manera similar a un modulo

```
#Se pueden importar modulos contenidos dentro del paquete
import matematicas.otros
matematicas.otros.tabla(2)

#Tambien asi
from matematicas import aritmetica
print(aritmetica.suma(4,3))

#Importar solo una funcion
from matematicas.aritmetica import promedio
print(promedio(2,3))
```




