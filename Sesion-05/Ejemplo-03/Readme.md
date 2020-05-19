

## Decoradores

### OBJETIVO

- Usar decoradores para incrementar funcionalidad de funciones con o sin argumentos

#### REQUISITOS

1. Python 3


#### DESARROLLO

Los decoradores son funciones que reciben otra función como parámetro, y devuelve otra función. Se suelen usar para incrementar la funcionalidad de esta.

Para aplicar un decorador sobre una función, se coloca @decorador en la linea que precede a la definición de la función.

```
#Ejemplo de decorador sin argumentos
def decorador(funcion):
    def nueva_funcion():
        print("Se incrementa código antes")
        funcion()
        print("Se incrementa código después")
    return nueva_funcion

@decorador
def hola_mundo():
    print("hola mundo")

hola_mundo()
```

Si la función tiene argumentos, podemos usar (*args, **kwargs) para que el decorador pueda decorar funciones con cualquier número de argumentos.

```
#Ejemplo de decorador con argumentos
def imprime_resultado(funcion):
    def nueva_funcion(*args, **kwargs):
        resultado = funcion(*args, **kwargs)
        print("El resultado es {}".format(resultado))
        return resultado
    return nueva_funcion

@imprime_resultado
def promedio(a,b):
    return(a + b)/2

@imprime_resultado
def sumatoria(*args):
    suma = 0
    for arg in args:
        suma += arg
    return suma

res = promedio(2,5)
print(res)

suma = sumatoria(1,2,3,4)
```
