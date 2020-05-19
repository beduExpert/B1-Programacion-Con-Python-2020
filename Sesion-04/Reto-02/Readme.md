 
## Reto de métodos

### OBJETIVO 

- Escribir métodos de distintos tipos incluyendo constructores

#### REQUISITOS 

1. Python 3
2. Código de ejemplo 1

#### DESARROLLO

1. Modifica el código del reto 1 para aceptar los parametros en un constructor
2. Crea un método que __str__ que devuelva una descripcion del objeto
3. Crea un método Avanzar (puede solo imprimir un mensaje)
4. Modifica la creacion a objetos para utilizar el constructor
5. Ejecuta los métodos creados

<details>
	class Vehiculo:
		def __init__(self,ruedas = 0, medio = 'medio', velocidad = 'no se mueve'):
			self.ruedas = ruedas
			self.velocidad = velocidad
			self.medio = medio
		def avanzar(self):
			print("El vehiculo se mueve a velocidad {}".format(self.velocidad))
		def __str__(self):
			return "ruedas {}, medio: {}, velocidad:{}".format(self.ruedas, self.medio, self.velocidad)
		def describir(self):
			print("Es un vehiculo de {} ruedas".format(self.ruedas))
			print("se mueve a velocidad {}".format(self.velocidad))
			print("Su medio es {}".format(self.medio))


	barco = Vehiculo(ruedas=0, medio='agua',velocidad='lenta')

	avion = Vehiculo(ruedas=4, medio='aire',velocidad='rapida')

	auto = Vehiculo(ruedas=4, medio='asfalto',velocidad='media')
	barco.describir()

	avion.describir()

	auto.describir()

	auto.avanzar()

	print(avion)
</details> 


