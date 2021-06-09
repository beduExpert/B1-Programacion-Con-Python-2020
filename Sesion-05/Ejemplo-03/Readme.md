

## Manejo de errores y excepciones 

### OBJETIVO

- Utilizar try y except para manejar errores durante la ejecución

#### REQUISITOS

1. Python 3 

#### DESARROLLO
Usualmente, cuando se produce un error durante el tiempo de ejecución el programa se detiene imprimiendo en la terminal el tipo de error.

Por ejemplo si tratamos de dividir entre 0, nos arroja el siguiente error
```
ZeroDivisionError: division by zero
```
- try: El código en este bloque se ejecuta
- except: Si el código en try causa error, la ejecución no se detiene y en su lugar, se ejecuta este bloque
```
a = 4
b = 0

try:
    c = a/b
    print ("El resultado de la división es {}".format(c))
except:
    print("No puedes dividir entre 0")

```
Si se requiere tomar distintas medidas en caso de que haya distintos tipos de errores posibles, se pueden especificar en distintos except. 

En el siguiente ejemplo el último except maneja errore que no se han definido anteriormente.

```
#Se pueden definir distintas medidas a tomar para distinto tipo de error
try:
    c = a/x
except NameError:
    print("Alguna variable no fue definida")
except ZeroDivisionError:
    print("No puedes dividir entre 0")
except: #Si se cae en un error no definido anteriormente
    print("Ocurrió otro error")
```

Existe una última clausula opcional finally, la cuál se ejecuta indistintamente de si se produjo una excepción.

