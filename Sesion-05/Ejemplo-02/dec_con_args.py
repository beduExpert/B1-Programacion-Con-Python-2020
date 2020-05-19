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