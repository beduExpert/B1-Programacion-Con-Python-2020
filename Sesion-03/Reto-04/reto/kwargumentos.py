"""ejemplos con kwargs"""
def directorio1(**kwargs):
    """imprime un directorio telefonico"""
    ordenado = sorted(kwargs)
    for dato in ordenado:
        print(dato, kwargs[dato])    


