def reto1(operacion, *args):
    resultado = 0
    if operacion == '*':
        resultado = 1
    for arg in args:
        if operacion == '+':
            resultado += arg
        elif operacion == '*':
            resultado *= arg
    return resultado

suma = reto1('+',2,3,4)
multiplicacion = reto1('*',1,3,4)
print(suma)
print(multiplicacion)
