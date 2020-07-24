def borra_repetidos (lista):
    
    sin_repetir = set(lista)
    lista2 = list(sin_repetir)
    for elemento in lista2:
        print(elemento)
    return lista2

lista = borra_repetidos([0,2,3,1,2,3])
print(lista)
