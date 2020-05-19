 

	
## Reto de decoradores

### OBJETIVO 

- Crear decoradores
- Usarlos para decorar funciones

#### REQUISITOS 

1. Python 3

#### DESARROLLO

- Crea un decoradorador que ejecute tres veces la clase decorada
- Decora alguna función con el decorador recien creado

<details>
	def triple(funcion):
		def nueva_funcion(*args,**kwargs):
			a =''
			for _ in range(3):
				a = funcion(*args, **kwargs)
			return a
		return nueva_funcion

	@triple
	def hola_mundo():
		print("hola mundo :)")


	hola_mundo()
</details> 


