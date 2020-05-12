
agrega el programa que se desarrollara con backticks> [agrega la sesion con backticks]

## Tuplas

### OBJETIVO

- Declarar tuplas
- Acceder a datos mediante indices
- Identificar la inmutabilidad de las tuplas y sus implicaciones

#### REQUISITOS

1. Python 3

#### DESARROLLO

Las tuplas son estructuras de datos  similares a las listas, pero que se caracterizan por ser inmutables.

Formas de declarar una tupla

```
# Creando una tupla vacia
t1 = ()
t2 = tuple()


# Tupla de un elemento

t3 = (1, )  # Sin la coma no se detecta como tupla

```

Se pueden asignar de forma simultanea los valores de una tupla a variables.
```
# Asignacion multiple con tupla

a, b = (10, 20)

```

Las tuplas son inmutables, por lo que el intentar modificarlas es causa de error.
```
#No se puede modificar una tupla, quitar comentarios para comprobar

t1.insert(0, 1)
t1.append(10)
```
Pero si podemos acceder a los valores almacenados
```
a = t3[0]
```
O convertir a listas, las cuales si se pueden modificar
```
l1 = list(t3)
```
<details>
	<summary>Solucion</summary>
        <p> Agrega aqui la solucion</p>
        <p>Recuerda! escribe cada paso para desarrollar la solución del ejemplo o reto </p>
</details>

Agrega una imagen dentro del ejemplo o reto para dar una mejor experiencia al alumno (Es forzoso que agregages al menos una) 

![imagen](https://picsum.photos/200/300)


