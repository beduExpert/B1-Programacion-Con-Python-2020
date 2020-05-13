 

	
## Minimo Común múltiplo

### OBJETIVO 

- Escribir funciones en Python
- Adquirir parámetos en funciones


#### REQUISITOS 

1. Python 3

#### DESARROLLO

Realiza un programa que calcule el minimo común múltiplo utilizando el algoritmo descrito en la siguiente [página](https://www.smartick.es/blog/matematicas/recursos-didacticos/minimo-comun-multiplo-mcm/)

<details>
	Código
	def min_com_multiplo (num1, num2):
		divisor = 2
		mcm = 1
		while num1 > 1 or num2 > 1:
			if num1 % divisor == 0:
				num1 = num1 / divisor
				dividido = True
			if num2 % divisor == 0:
				num2 = num2 / divisor
				dividido = True
			if dividido:
				mcm *= divisor
				dividido = False
			else:
				divisor += 1
		return mcm

	print(min_com_multiplo(18,91))

</details> 

