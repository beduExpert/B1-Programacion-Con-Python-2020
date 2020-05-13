
agrega el programa que se desarrollara con backticks> [agrega la sesion con backticks]

## Funciones

### OBJETIVO

- Identificar funciones
- Realizar llamados a funciones
- Declarar funciones
- Utilizar parámetros y valores de retorno en funciones

#### REQUISITOS

1. Lo necesario para desarrollar el ejemplo o el Reto

#### DESARROLLO

Las funciones son porciones de código que se pueden llamar para hacer uso de su codigo

Algunas que ya hemos utilizado, las funciones se llaman usando su nombre y a veces parámetros
```
print("Hola Mundo")
input()
```

Para definirlas usamos def
```
def hola_mundo():
    print("Hola Mundo")
#Para llamarlas, lo hacemos por su nombre
hola_mundo()
```

Las funciones pueden tener parámetros
```
def saludo(persona):
    print("Hola {}".format(persona))

saludo("Luis")
saludo("Bedu")
saludo("Mundo")
```

Las funciones pueden devolver algun dato
```
def area_rectangulo(base, altura):
    area = base * altura
    return area

b = 5
h = 3
area = area_rectangulo(b, h)
```


