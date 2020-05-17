
 
	
## Args y kwargs
### OBJETIVO 

- Obtener un numero de argumentos no determinado usando args
- Obtener argumentos con nombre usando kwargs

#### REQUISITOS 

1. Python 3 

#### DESARROLLO

Existen dos tipos de argumentos en Python: los convencionales y aquellos que están sujetos a un nombre específico, generalmente identificados como args (arguments) y kwargs (keyword arguments), respectivamente. 

Para obtener un número indeterminado de argumentos usamos *args, los argumentos en *args se consideran una tupla y se puede iterar sobre ellos.
```
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

