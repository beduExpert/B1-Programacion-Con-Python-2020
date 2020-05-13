#Formas de declarar una lista vacia
lista_vacia = [] #Dentro de los corchetes se especifican los datos
lista_vacia2 = list() #Usando La función list

print(lista_vacia, type(lista_vacia))
print(lista_vacia2, type(lista_vacia2))

#Las listas pueden inicializarse con datos
lista_int = [1, 2, 3, 4, 5]
lista_fl = [1.4, 3.1415, 2.12, 12.7, 0.22]
lista_str = ['hola','mundo','!']
print(lista_fl)

# Las listas pueden contener datos de distinto tipo
lista_mix = [1, 1.4, "hola"]
print(lista_mix)

#O incluso otras listas
listas = [lista_int,lista_str,lista_fl]
print(listas)