#Operaciones con listas
numeros = [1,2,3,4,5]
print("Datos en la lista:", numeros)

#Acceso por indice
dato = numeros[2]
print(dato)

#Obtener porciones de lista
sublista = numeros[1:3]
print(sublista)

#Agregar elementos a la lista
numeros.append(100)
print(numeros)

#Insertar numeros en la lista
numeros.insert(2,'python') 
print(numeros)

#Tomar elementos de lista
dato = numeros.pop(2)
print(numeros)
print(dato)

#Convertir a lista una cadena
l3 = list("abc123")
print(l3)


