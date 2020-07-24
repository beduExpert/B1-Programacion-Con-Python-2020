	
## Reto calculadora

### OBJETIVO 

- Utilizar distintos tipos de datos
- Utilizar operadores lógicos y algebraicos
- Escribir estructuras condicionales
- Leer y escribir cadenas de texto


#### REQUISITOS 

1. Python 3

#### DESARROLLO

Crea una calculadora:

- Se deben solicitar al usuario dos números

- Se puede seleccionar entre diferentes operaciones(suma, resta, multiplicación y división).

- Imprimir resultados

- Considerar división entre cero y caracteres no definidos como operaciones.


<details>
	Solución

	#Se solocotan los datos
	print("inserta el primer numero")
	num1 = int(input())
	print("inserta el segundo numero")
	num2 = int(input())
	print("Selecciona operación a realizar")
	print("+ -> Suma")
	print("- -> Resta")
	print("* -> Multiplicaión")
	print("/ -> División")
	print("% -> Modulo")
	operacion = input()

	#Estructura de condicionales
	if operacion == '+':
		resultado = num1 + num2
	elif operacion == '-':
		resultado = num1 + num2
	elif operacion == '*':
		resultado = num1 + num2
	elif operacion == '/':
		if num2 == '0':
			print("ERROR: División entre 0")
			resultado = 'ERROR'
		else:
			resultado = num1 / num2
	elif operacion == '%':
		resultado = num1 % num2
	else:
		resultado = 'ERROR'
		print("Operacion no definida")

	#Imprime el resultado
	print("{} {} {} = {}".format(num1,operacion, num2, resultado))
</details> 



