 

	
## Crear modulo

### OBJETIVO 

- Crear modulos
#### REQUISITOS 

1. Python 3
2. Reto 01 de esta sesión 

#### DESARROLLO

1. Convierte el archivo del reto 01 args en un modulo
2. Llama la funcion de suma y producto desde otro archivo

<details>
	Archivo del modulo

	def operacion(operacion, *args):
		resultado = 0
		if operacion == '*':
			resultado = 1
		for arg in args:
			if operacion == '+':
				resultado += arg
			elif operacion == '*':
				resultado *= arg
		return resultado

	Archivo de ejecución

	from argumentos import operacion

	suma = operacion('+',2,3,4)
	multiplicacion = operacion('*',1,3,4)
	print(suma)
	print(multiplicacion)
</details> 

Agrega una imagen dentro del ejemplo o reto para dar una mejor experiencia al alumno (Es forzoso que agregages al menos una)

![imagen](https://picsum.photos/200/300)

