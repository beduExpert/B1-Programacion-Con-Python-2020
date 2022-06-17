 	
## Reto clases y objetos

### OBJETIVO 

- Crear clases
- Crear objetos a partir de una clase

#### REQUISITOS 

1. Python 3

#### DESARROLLO

Vamos a crear una Clase para representar autos. Como en la vida real, cada auto en las calles tiene diferentes atributos:
mi auto no es el mismo que el del vecino, e incluso si dos autos salen de la misma agencia, sus atributos pueden cambiar
con el tiempo, por ejemplo, su kilometraje.

Imaginemos que vamos a crear un programa para llevar control de autos en una agencia de autos usados. Utilicemos Programación
Orientada a Objetos para facilitar esta tarea:


- Crea una clase llamada Vehiculo con atributos como kilometraje, marca, modelo... elementos que consideres importante
  conocer en un auto usado.
- Crea por lo menos un método que permita alterar uno de esos atributos.
- Agrega un metodo que describa el vehiculo, con los atributos anteriormente utilizando self. Este debe imprimar los datos
  o bien, regresar el valor como cadena de texto.
- Crea tres objetos de esta clase con distintos argumentos
- Prueba a utilizar el método anteriomente, para imprimir los datos de los autos.


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