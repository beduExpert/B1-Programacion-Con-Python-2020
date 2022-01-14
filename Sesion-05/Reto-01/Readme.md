 


## Titulo del Ejemplo 

### OBJETIVO 

- Utilizar polimorfismo y sobrecarga de métodos

#### REQUISITOS 

1. Python 3
2. Código del reto 4 de la sesión pasada

#### DESARROLLO

Vamos a continuar aplicando los conceptos a nuestro programa de autos usados.

- Modifica el código del reto 4 de la sesión pasada para sobrecargar el método avanzar de la clase Vehiculo en sus clases hijas, para ser mas descriptiva de acuerdo al tipo de vehiculo
- Agrega verificaciones para revisar si el auto puede avanzar: si no tiene gasolina o la batería esta gastada, no debería ser capaz de avanzar.
- También, agrega la representación en texto con `__str__` si no la has agregado.
  Deberá mostrar información del auto. Es una de los métodos muy utilizados por polimorfismo.

<details>
	class Vehiculo:
		def __init__(self,ruedas = 0, medio = 'medio', velocidad = 'no se mueve'):
			self.__ruedas = ruedas
			self.__velocidad = velocidad
			self.__medio = medio
		def avanzar(self):
			print("El vehiculo se mueve a velocidad {}".format(self.__velocidad))
		def __str__(self):
			return "ruedas {}, medio: {}, velocidad:{}".format(self.__ruedas, self.__medio, self.__velocidad)
		def describir(self):
			print("Es un vehiculo de {} ruedas".format(self.__ruedas))
			print("se mueve a velocidad {}".format(self.__velocidad))
			print("Su medio es {}".format(self.__medio))

	class Vehiculo_terrestre(Vehiculo):
		def __init__(self, ruedas=0, velocidad='no se mueve'):
			super().__init__(ruedas, 'tierra', velocidad)
		def estacionarse(self):
			print("El vehiculo está estacionado")
		def avanzar(self):
			print("El vehiculo avanza por el camino")

	class Vehiculo_acuatico(Vehiculo):
		def __init__(self, velocidad='no se mueve'):
			super().__init__(0, 'agua', velocidad)
		def undirse(self):
			print("El vehiculo se undió")
		def avanzar(self):
			print("El vehiculo avanza por el mar")

	class Vehiculo_aereo(Vehiculo):
		def __init__(self, ruedas=0, velocidad='no se mueve'):
			super().__init__(ruedas, 'aire', velocidad)
		def despegar(self):
			print("El vehiculo está despegando")
		def avanzar(self):
			print("El vehículo está volando")

	barco = Vehiculo_acuatico(velocidad='lenta')

	avion = Vehiculo_aereo(ruedas=4,velocidad='rapida')

	auto = Vehiculo_terrestre(ruedas=4,velocidad='media')
	barco.describir()

	avion.describir()

	auto.describir()

	auto.avanzar()
	avion.avanzar()

	print(avion)
	auto.estacionarse()
	avion.despegar()
	barco.undirse()
</details> 

Agrega una imagen dentro del ejemplo o reto para dar una mejor experiencia al alumno (Es forzoso que agregages al menos una)

![imagen](https://picsum.photos/200/300)

