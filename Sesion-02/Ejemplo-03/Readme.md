
agrega el programa que se desarrollara con backticks> [agrega la sesion con backticks]

## Tuplas

### OBJETIVO

- Declarar sets
- Acceder a datos dentro de un set
- Realizar operaciones de conjuntos usando sets

#### REQUISITOS

1. Python 3

#### DESARROLLO

Los conjuntos o sets, son colecciones no mutables y no ordenadas, utilizadas principalmente en operaciones de lógica y matemática.

A diferencia de las listas y tuplas, al no estar ordenadas, no se puede acceder mediante un índice. Se puede utlizar un for para acceder a todos sus elementos uno por uno. Tampoco permite elementos repetidos.

 Declarar un set 
```
s1 = set()

s1 = {1, 2, 4, 5}
```
Agregar elementos a un set
```
s1.add(3)  

#Los datos en un set no se pueden repetir
s1.add(3) #No agrega un nuevo elemento
```

Quitar elementos
```
s1.remove(3)  
```
Se pueden realizar operaciones de conjuntos
```
s2 = {4, 5, 6, 7, 8}
print(s1 & s2) # Union 
print(s1.intersection(s2))  # Interseccion
```