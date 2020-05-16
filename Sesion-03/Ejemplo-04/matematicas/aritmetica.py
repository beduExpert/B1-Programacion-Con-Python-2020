def promedio(*args):
    suma = 0
    for arg in args:
        suma += arg
    resultado = suma/len(args)
    return resultado

def suma(*args):
    suma = 0
    for arg in args:
        suma += arg
    return suma

def producto(*args):
    suma = 1
    for arg in args:
        suma *= arg
    return suma
