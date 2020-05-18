

## Modulos

### OBJETIVO

- Crear modulos
- Importar funciones desde modulos 

#### REQUISITOS

1. Python 3

#### DESARROLLO

Los modulos nos permiten estructurar nuestro código en más de un archivo, cualquier archivo .py puede considerarse un modulo

Para acceder a código que se encuentra en un modulo (en la misma carpeta) usamos import con el nombre del archivo(sin el .py)

```
#Se importa el paquete completo
import aritmetica
print(aritmetica.promedio(1,3,5))

#importar una función desde el paquete
from aritmetica import suma
print(suma(1,3,5))

#Usar alias para elementos importados
from aritmetica import producto as prod
print(prod(1,2))
```
