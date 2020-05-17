 

	
## Crear paquete

### OBJETIVO 

- Crear paquetes
- Usar Docstrings

#### REQUISITOS 

1. Python 3
2. Reto 01 de esta sesión 

#### DESARROLLO

1. Convierte los archivos del reto 01 en un paquete
2. Llama la funcion de operacion y directorio desde otro archivo
3. No olvides colocar docstrings
4. Solicita help de alguna función

<details>
	Ver la carpeta reto para ver la estructura del paquete

	Para llamar los archivos del paquete

	from reto.argumentos import operacion
	from reto.kwargumentos import directorio1

	suma = operacion('+',2,3,4)
	multiplicacion = operacion('*',1,3,4)
	print(suma)
	print(multiplicacion)

	directorio1(Richie='12345', Daniela = '0987')
	help(operacion)

</details> 

