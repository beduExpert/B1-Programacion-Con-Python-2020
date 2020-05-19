 

agrega el programa que se desarrollara con backticks> [agrega la sesion con backticks] 
	
## Titulo del Ejemplo 

### OBJETIVO 

- Manejar excepciones usando try , excpt

#### REQUISITOS 

1. Crea una función que realice el promedio de dos números
2. Usa try, except para detectar si uno de los argumentos no es numerico
3. Detecta otros tipos de error

#### DESARROLLO



<details>
	def promedio(num1,num2):
		try:
			return  (num1+num2)/2
		except NameError:
			print("Datos nos validos")
			return 0
		except TypeError:
			print("Datos no validos")
			return 0
		except:
			print("ocurrió un error")
			return 0
		


	print(promedio(3,'a'))
	print(promedio(2,3))
</details> 

Agrega una imagen dentro del ejemplo o reto para dar una mejor experiencia al alumno (Es forzoso que agregages al menos una)

![imagen](https://picsum.photos/200/300)

