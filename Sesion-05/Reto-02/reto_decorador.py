def triple(funcion):
    def nueva_funcion(*args,**kwargs):
        a =''
        for _ in range(3):
            a = funcion(*args, **kwargs)
        return a
    return nueva_funcion

@triple
def hola_mundo():
    print("hola mundo :)")


hola_mundo()