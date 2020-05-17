def operacion(operacion, *args):
    resultado = 0
    if operacion == '*':
        resultado = 1
    for arg in args:
        if operacion == '+':
            resultado += arg
        elif operacion == '*':
            resultado *= arg
    return resultado
