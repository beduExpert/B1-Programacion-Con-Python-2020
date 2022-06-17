
 
	
## Argumentos, args y kwargs
### Objetivo 

- Utilizar argumentos opcionales y en diferente orden
- Obtener un numero de argumentos no determinado usando args
- Obtener argumentos con nombre usando kwargs

#### Requisitos 

1. Python 3 

#### Desarrollo

Los argumentos tienen más propiedades de las que hemos visto en la sesión anterior. En primer lugar, puede ser opcionales,
al agregarse un valor por defecto, y así también, se pueden indicar por nombre, cambiando incluso su posición.

```python
def funcion(arg1, arg2, arg_opcional=0):
    print(arg1, arg2, arg_opcional)

funcion(arg2="Dos", arg1="Uno")  # Uno Dos 0
```

Los argumentos opcionales son útiles cuando no queremos que siempre se indiquen, y llevan un valor por defecto, por lo general un valor que haga sentido a la función en cuestión.

Llamando a los argumentos por nombre, con su nombre seguido de un `=`, también se puede cambiar su orden de llamado.

Así también, aparte de estos argumentos convencionales, existen otros dos tipos de argumentos en Python: aquellos que están sujetos a un nombre específico, generalmente identificados como args (arguments) y kwargs (keyword arguments), respectivamente. 

Para obtener un número indeterminado de argumentos usamos *args, los argumentos en *args se consideran una tupla y se puede iterar sobre ellos.
```python
def imprime(*a2gs):  
    for arg in a2gs:  
        print (arg) 
    
imprime('Hola', 'A', 'Todos', '!')
```
Se pueden mezclar argumentos comunes con args
```
def imprime_varias_veces(veces, *argv): 
    for i in range(veces):
        for arg in argv:
            print(arg)

  
imprime_varias_veces(3, 'Bienvenidos ', 'a', 'Bedu') 
```
**kwargs nos permite pasar argumentos nombrados (también un número indeterminado)
```
def saludo(**kwargs):
    print('Hola {} de {}'.format(kwargs['nombre'], kwargs['empresa']))

saludo(empresa='Bedu',nombre='Luis')
saludo(nombre='Luis',empresa='Bedu')
```
Los valores se tratan como un diccionario y se pueden utilizar sus llaves y valores
```
def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
myFun(nombre ='Fernando', empresa ='Bedu', ciudad='CDMX') 
```

