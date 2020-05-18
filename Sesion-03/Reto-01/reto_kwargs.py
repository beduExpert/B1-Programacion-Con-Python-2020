def directorio1(**kwargs):
    ordenado = sorted(kwargs)
    for dato in ordenado:
        print(dato, kwargs[dato])    


directorio1(Richie='12345', Daniela = '0987')