# Creando una tupla vacia
t1 = ()
t2 = tuple()
# Obteniendo el tipo de dato

type(t1)

# Tupla de un elemento

t3 = (1, )  # Sin la coma no se detecta como tupla
# Asignacion multiple con tupla

a, b = (10, 20)

print(a, b)

#No se puede modificar una tupla, quitar comentarios para comprobar

#t1.insert(0, 1)
#t1.append(10)

#Pero si podemos acceder a los valores almacenados
a = t3[0]
print(a)

#O convertir a listas, las cuales si se pueden modificar
l1 = list(t3)
print(l1)
