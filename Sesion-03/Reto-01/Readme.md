 
	
## Args y kwargs
### OBJETIVO 

- Obtener un numero de argumentos no determinado usando args
- Obtener argumentos con nombre usando kwargs

#### REQUISITOS 

1. Python 3 

#### DESARROLLO
1. Crea una función que permita obtener una cantidad indeterminada de valores y sumarlos o multiplicarlos usando args
2. Crea una función que adquiera un número indeterminado de personas y su número de telefono e imprima el directorio ordenado alfabeticamente

Nota: Puedes usar sorted(dicc) para obtener una lista con las llaves ordenadas


<details>
	Ejercicio 1 
	def reto1(operacion, *args):
		resultado = 0
		if operacion == '*':
			resultado = 1
		for arg in args:
			if operacion == '+':
				resultado += arg
			elif operacion == '*':
				resultado *= arg
		return resultado

	suma = reto1('+',2,3,4)
	multiplicacion = reto1('*',1,3,4)
	print(suma)
	print(multiplicacion)


	Ejercicio 2 
	def directorio1(**kwargs):
		ordenado = sorted(kwargs)
		for dato in ordenado:
			print(dato, kwargs[dato])    


	directorio1(Richie='12345', Daniela = '0987')


</details> 



