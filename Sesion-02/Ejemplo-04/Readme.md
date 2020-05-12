
agrega el programa que se desarrollara con backticks> [agrega la sesion con backticks]

## Diccionarios

### OBJETIVO

- Declarar diccionarios.
- Acceder a los valores y llaves en diccionarios.
- Obtener valores mediante su llave.
- Realizar operaciones básicas con diccionarios.

#### REQUISITOS

1. Python 3

#### DESARROLLO

Los diccionarios son estructuras de datos que nos permiten almacenar datos, asignandolas a llaves.

El acceso a los diccionarios debe realizarse mediante las llaves, no permiten realizarlo por índice.


Declarar diccionarios 
``` 
d1 = {}
d2 = dict() 


#Crear diccionario con datos
d3 = {"Usuario": "usser123", "Correo": "us12@bedu.org", "Compañia": "Bedu"} 
```
Es importante señalar que la información se almacena en pares en formato llave:valor     

Se pueden obtener las llaves y valores en formato de lista.
```
# Se pueden obtener las llaves en una lista
d3.keys() 

# Se pueden obtener los valores en una lista
d3.values() # Lista de valores
```

Agregar datos a diccionario
```
#Se pueden agregar entradas en un diccionario
d3['ciudad']= "CDMX"
```

Se puede acceder a los valores del diccionario usando su llave
```
print(d3['ciudad'])

#Tambien podemos extraer datos usando pop
a = d3.pop('ciudad')
```
