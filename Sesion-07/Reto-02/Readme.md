
	
## Reto tests 2 

### OBJETIVO 

- Crear tests múltiples y con distintos tipos de sets
- Seleccionar tests a ejecutar

#### REQUISITOS 

1. Python 3
2. Pytest

#### DESARROLLO

Vamos a probar que nuestra función de promedios de calificaciones se comporta correctamente en varias situaciones.
Crea un test para cada uno de estos casos.

1. El test anteriormente creado.
1. Un test para este caso: ¿Profesor, 6.5 sube a 7? La duda que corroe a muchos alumnos. Crea un test y valida su respuesta.
1. Rango de calificaciones: Si por alguna razón el resultado es mayor a 10 o menor a 0, hay que colocarlo en el rango de 0 a 10.

Edita la función para hacer pasar todos los tests.

Para terminar, desde terminal realiza la ejecución de:
	- Todos los tests
	- Primer test
	- Tercer test


<details>
	Se crea el siguiente archivo de tests
	from promedio import promedio

	def test_promedio_int():
		resultado = promedio(2,4)
		assert resultado == 3
		assert type(resultado) is float
		resultado = promedio(10,11)
		assert resultado == 10.5
		assert type(resultado) is float


	def test_promedio_float():
		resultado = promedio(10.1,10.3)
		assert resultado == 10.2
		assert type(resultado) is float
		resultado = promedio(6.0 ,6.5)
		assert resultado == 6.25
		assert type(resultado) is float

	Para ejecutar ambos tests

	$pytest -v
	======================================================================================== test session starts ========================================================================================
	platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /home/luisams/anaconda3/bin/python
	cachedir: .pytest_cache
	hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Reto-02/.hypothesis/examples')
	rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Reto-02
	plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
	collected 2 items                                                                                                                                                                                   

	test_promedio.py::test_promedio_int PASSED                                                                                                                                                    [ 50%]
	test_promedio.py::test_promedio_float PASSED       
	                                                                                                                                           [100%]

	========================================================================================= 2 passed in 0.02s =========================================================================================

	Para ejecutar el primer test
	$ pytest -v test_promedio.py::test_promedio_int
	======================================================================================== test session starts ========================================================================================
	platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /home/luisams/anaconda3/bin/python
	cachedir: .pytest_cache
	hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Reto-02/.hypothesis/examples')
	rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Reto-02
	plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
	collected 1 item                                                                                                                                                                                    

	test_promedio.py::test_promedio_int PASSED                                                                                                                                                    [100%]

	========================================================================================= 1 passed in 0.01s =========================================================================================

	Para el segundo tests 
	
	$ pytest -v test_promedio.py::test_promedio_float
	======================================================================================== test session starts ========================================================================================
	platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /home/luisams/anaconda3/bin/python
	cachedir: .pytest_cache
	hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Reto-02/.hypothesis/examples')
	rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Reto-02
	plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
	collected 1 item                                                                                                                                                                                    

	test_promedio.py::test_promedio_float PASSED                                                                                                                                                  [100%]

	========================================================================================= 1 passed in 0.02s ========================================================================================
</details> 



