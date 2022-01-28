 

	
## Reto tests 1

### OBJETIVO 

- Escribir tests unitarios
- Ejecutar tests unitarios

#### REQUISITOS 

1. Python 3
2. Pytest

#### DESARROLLO

Vamos a crear una función para promediar calificaciones, que utilizaremos
en una app hipotética para entregar calificaciones:

1. Crea una función que genere el promedio de dos o más números.
1. Inserta un error de forma intencional.
1. Crea un test para la función anterior. Coloca tres calificaciones, por ejemplo: 6, 8, 7.5.
1. Ejecuta el test.
1. Haz las correcciones a la función.
1. Vuelve a ejecutar el test.

Después validar que tu función es correcta, acaba de llegar un nuevo requerimiento:
Se necesita redondear ese promedio, sin décima:

1. Modifica el test **primero**, con el nuevo valor esperado.
1. Corre el test y revisa que ahora ha fallado.
1. Edita la función. Si tienes dudas de como redondear, revisa la función [round](https://www.w3schools.com/python/ref_func_round.asp)

Esta practica de primero comenzar con el test y después con la implementación, se conoce como Test Driven Development.
¡Algunos desarrolladores comienzan siempre escribiendo tests! 


<details>
	Se crea el archivo promedio.py:

	def promedio(num1 ,num2):
    	return (num1 - num2)/2

	Y se crea el test_promedio.py:

	from promedio import promedio

	def test_promedio():
		assert promedio(2,4) == 3
		assert promedio(10,11) == 10.5
		assert promedio(4,4) == 4

	
	Si ejecutamos el test obtenemos

	$ pytest test_promedio.py 
	======================================================================================== test session starts ========================================================================================
	platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
	rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Reto-01
	plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
	collected 1 item                                                                                                                                                                                    

	test_promedio.py F                                                                                                                                                                            [100%]

	============================================================================================= FAILURES ==============================================================================================
	___________________________________________________________________________________________ test_promedio ___________________________________________________________________________________________

		def test_promedio():
	>       assert promedio(2,4) == 3
	E       assert -1.0 == 3
	E        +  where -1.0 = promedio(2, 4)

	test_promedio.py:4: AssertionError
	========================================================================================= 1 failed in 0.04s =========================================================================================

	Si corregimos la función promedio 
	$ pytest test_promedio.py 
	======================================================================================== test session starts ========================================================================================
	platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
	rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Reto-01
	plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
	collected 1 item                                                                                                                                                                                    

	test_promedio.py .                                                                                                                                                                            [100%]

	========================================================================================= 1 passed in 0.02s =========================================================================================
		

</details> 

