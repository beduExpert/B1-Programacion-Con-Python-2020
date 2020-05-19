 	
## Reto clases y objetos

### OBJETIVO 

- Crear clases
- Crear objetos a partir de una clase

#### REQUISITOS 

1. Python 3

#### DESARROLLO
- Crea una clase llamada vehiculo con argumentos como velocidad, numero de ruedas, medio
- Agrega un metodo que describa el vehiculo
- Crea tres objetos de esta clase con distintos argumentos
<details>
	class Vehiculo:
		def describir(self):
			print("Es un vehiculo de {} ruedas".format(self.ruedas))
			print("se mueve a velocidad {}".format(self.velocidad))
			print("Su medio es {}".format(self.medio))

	barco = Vehiculo()
	barco.ruedas=0
	barco.velocidad='lenta'
	barco.medio = 'agua' 
	barco.describir()

	Avion = Vehiculo()
	Avion.ruedas=4
	Avion.velocidad='rapido'
	Avion.medio = 'aire' 
	Avion.describir()

	auto = Vehiculo()
	auto.ruedas=4
	auto.velocidad='media'
	auto.medio = 'asfalto' 
	auto.describir()

</details> 