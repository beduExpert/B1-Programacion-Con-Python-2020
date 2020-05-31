 

	
## Reto tests 1

### OBJETIVO 

- Escribir tests unitarios
- Ejecutar tests unitarios

#### REQUISITOS 

1. Python 3
2. Pytest

#### DESARROLLO

1. Crea una función que genere  el promedio de dos números (inserta un error de forma intencional) 
2. Crea un test para la función anterior
3. Ejecuta el test
4. Haz las correcciones a la función
5. Vuelve a ejecutar el test


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

Agrega una imagen dentro del ejemplo o reto para dar una mejor experiencia al alumno (Es forzoso que agregages al menos una)

![imagen](https://picsum.photos/200/300)

