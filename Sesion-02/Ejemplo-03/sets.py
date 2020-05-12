
# Declarar un set 
s1 = set()
print(type(set))

s1 = {1, 2, 4, 5}

# Agregar elementos a un set
s1.add(3)  
print(s1)

#Los datos en un set no se pueden repetir
s1.add(3)
print(s1)

# Quitar elementos
s1.remove(3)  
print(s1)

print(list(s1))

#Se pueden realizar operaciones de conjuntos
s2 = {4, 5, 6, 7, 8}
print(s1 & s2) # Union 
print(s1.intersection(s2))  # Interseccion