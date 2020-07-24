 

	
## Minimo Común múltiplo

### OBJETIVO 

- Escribir funciones en Python
- Hacer uso de sets y listas
- Escribir estructuras basadas en ciclos
- Adquirir parámetos en funciones


#### REQUISITOS 

1. Python 3

#### DESARROLLO

Realiza una función que tome como entrada una lista de números, y devuelca una lista con los valores en orden y sin repetidos. Además la función debe imprimir los valores uno a uno.
<details>
	def borra_repetidos (lista):
		
		sin_repetir = set(lista)
		lista2 = list(sin_repetir)
		for elemento in lista2:
			print(elemento)
		return lista2

	lista = borra_repetidos([0,2,3,1,2,3])
	print(lista)

</details> 

