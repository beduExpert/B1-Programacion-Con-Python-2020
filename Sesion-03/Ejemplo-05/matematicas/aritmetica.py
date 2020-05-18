"""Operaciones aritmeticas"""
def promedio(*args):
    """Obten promedio de valores"""
    suma = 0
    for arg in args:
        suma += arg
    resultado = suma/len(args)
    return resultado

def suma(*args):
    """Suma de valores"""
    suma = 0
    for arg in args:
        suma += arg
    return suma

def producto(*args):
    """Producto de múltiples valores """
    suma = 1
    for arg in args:
        suma *= arg
    return suma
