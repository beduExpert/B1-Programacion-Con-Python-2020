 	
## Herencia

### OBJETIVO 

- Crear clases heredadas

#### REQUISITOS 

1. Python 3
2. Código de reto 3

#### DESARROLLO

La venta de autos usados continúa siendo un éxito, tanto así, que han llegado los primeros autos electrícos a la compañía.
Sabemos que funcionan de forma similar a los autos de gas, pero también tienen diferencias.
Utilicemos la herencia para poder agregar estos nuevos autos a nuestro programa.

1. Crear una clase Vehículo la cual sea genérica: Que no tenga nada de manejo del auto a gasolina o electrico.
2. Heredar de Vehiculo, para crear la clase VehiculoGas: Este tendrá la implementación para vehículos a gasolinas,
   como por ejemplo, un tanque de gas y su capacidad.
3. Volver a hereder de Vehiculo, ahora con otra clase: VehiculoElectrico. Aquí colocarás elementos de un auto electrico,
   por ejemplo, la capacidad de sus baterías.


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

	class Vehiculo_acuatico(Vehiculo):
		def __init__(self, velocidad='no se mueve'):
			super().__init__(0, 'agua', velocidad)
		def undirse(self):
			print("El vehiculo se undió")

	class Vehiculo_aereo(Vehiculo):
		def __init__(self, ruedas=0, velocidad='no se mueve'):
			super().__init__(ruedas, 'aire', velocidad)
		def despegar(self):
			print("El vehiculo está despegando")

	barco = Vehiculo_acuatico(velocidad='lenta')

	avion = Vehiculo_aereo(ruedas=4,velocidad='rapida')

	auto = Vehiculo_terrestre(ruedas=4,velocidad='media')
	barco.describir()

	avion.describir()

	auto.describir()

	auto.avanzar()

	print(avion)
	auto.estacionarse()
	avion.despegar()
	barco.undirse()
</details> 


