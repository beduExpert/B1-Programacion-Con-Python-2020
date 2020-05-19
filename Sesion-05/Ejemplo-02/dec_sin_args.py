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