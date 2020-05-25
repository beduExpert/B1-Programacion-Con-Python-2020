## Argumentos en scripts

### OBJETIVO

- Crear scripts que pueden llamarse directamente desde la terminal
- Recibir argumentos posicionales 
- Recibir argumentos con nombre usando argparse

#### REQUISITOS

1. Python 3

#### DESARROLLO
Un script puede invocarse desde la terminal sin la necesidad de tener abierto anteriormente el interprete de Python, para esto usamos la siguiente estructura:
```
$python script.py
```
También es posible incluir argumentos dentro de un script
```
$python script.py argumento1 argumento2
```
En Python, podemos acceder a los argumentos mediante `sys.argv`

`argumentos.py`

```python
import sys

for arg in sys.argv:
    print(arg)
```
El cual, al ser llamado con argumentos, lo podremos visualizar en pantalla:

```
$ python argumentos.py estos son mis argumentos
argumentos.py
estos
son
mis
argumentos
```

Nótese que siempre el primer argumento será cómo llamó el usuario el programa o script.

Debido a que los argumentos son almacenados en una lista, podemos utilizarlos de acuerdo al índice, recuerda que en la posición 0 está el nombre del mismo script

`argumentos2.py`

```
import sys


# Comprobación de seguridad, ejecutar sólo si se reciben 2 argumentos reales
if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range(repeticiones):
        print(texto)
else:
    print("Error - Introduce los argumentos correctamente")
    print('Ejemplo: escribir_lineas.py "Texto" 5')
```
```
$ python argumentos2.py hola 2
hola
hola
```
También podemos usar argparser para crear argumentos nombrados
`argumentos_nombre.py`
```
import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Mostrar información de depuración", action="store_true")
parser.add_argument("-f", "--file", help="Nombre de archivo a procesar")
args = parser.parse_args()
 
# Aquí procesamos lo que se tiene que hacer con cada argumento
if args.verbose:
    print ("depuración activada!!!")
 
if args.file:
    print ("El nombre de archivo a procesar es: ", args.file)
```

```
python argumentos_nombre.py -f readme.md
El nombre de archivo a procesar es:  readme.md
```






