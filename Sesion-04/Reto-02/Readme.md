 
## Reto de métodos

### OBJETIVO 

- Escribir métodos de distintos tipos incluyendo constructores

#### REQUISITOS 

1. Python 3
2. Código de ejemplo 1

#### DESARROLLO


Con lo recién aprendido, podemos mejorar nuestros objetos para mantener control de los autos usados.
La mejora mas lógica que podemos hacer, es utilizar constructores para simplificar los objetos.
Utilizaremos también otros métodos implícitos para facilitar su uso.


1. Modifica el código del Reto 1 para aceptar los parametros en un constructor.
1. Guarda los parámetros como atributos para la clase.
1. Elimina funciones para crear o editar atributos que ya no sean necesarias.
1. Crea un método que `__str__` que devuelva una descripcion del objeto.
1. Crea un método Avanzar, que aumente el kilometraje, y opcionalmente imprima un mensaje.
1. Modifica la creacion a objetos para utilizar el constructor.
1. Utiliza los métodos creados para mostrar la información de los autos.

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


