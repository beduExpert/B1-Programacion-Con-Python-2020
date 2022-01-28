## Reto tests 3

### OBJETIVO 


1. Se incluiran marks en los text
2. Inclir skips en los test
3. Filtrar los tests a realzar de distinta manera

#### REQUISITOS 
- Python 3
- Pytest

#### DESARROLLO

Vamos a utilizar mark para poder realizar filtrados. Para eso dividiremos en dos partes
los problemas: Pruebas que trabajen con enteros, y pruebas que trabajen con flotantes. 

1. En los test realizados para el promedio agrega marks para realizar filtrados
2. Ejecuta tests con las siguientes condiciones
	- Filtrando por nombre
	- Filtrando por mark
3. Coloca un skip en alguno de los tests y ejecutalo.


<details>
	Para los fines de este reto modificamos el archivo de test a esta manera, la cuál incluye marks

	from promedio import promedio
	import pytest

	@pytest.mark.entero
	def test_promedio_int():
		resultado = promedio(2,4)
		assert resultado == 3
		assert type(resultado) is float

	@pytest.mark.entero
	def test_promedio_int_2():
		resultado = promedio(10,11)
		assert resultado == 10.5
		assert type(resultado) is float

	@pytest.mark.numero
	def test_promedio_float():
		resultado = promedio(10.1,10.3)
		assert resultado == 10.2
		assert type(resultado) is float

	@pytest.mark.numero
	def test_promedio_float_2():
		resultado = promedio(6.0 ,6.5)
		assert resultado == 6.25
		assert type(resultado) is float

	Podemos realizar tests filtrando por nombre:

	$ pytest test_promedio.py -k "float" -v
	======================================================================================== test session starts ========================================================================================
	platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /home/luisams/anaconda3/bin/python
	cachedir: .pytest_cache
	hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Reto-03/.hypothesis/examples')
	rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Reto-03
	plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
	collected 4 items / 2 deselected / 2 selected                                                                                                                                                       

	test_promedio.py::test_promedio_float PASSED                                                                                                                                                  [ 50%]
	test_promedio.py::test_promedio_float_2 PASSED    

	Tests filtrados por marks

	$ pytest test_promedio.py -m entero -v
	======================================================================================== test session starts ========================================================================================
	platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /home/luisams/anaconda3/bin/python
	cachedir: .pytest_cache
	hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Reto-03/.hypothesis/examples')
	rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Reto-03
	plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
	collected 4 items / 2 deselected / 2 selected                                                                                                                                                       

	test_promedio.py::test_promedio_int PASSED                                                                                                                                                    [ 50%]
	test_promedio.py::test_promedio_int_2 PASSED                                                                                                                                                  [100%]

	Colocamos un skip en el tercer test

	@pytest.mark.skip()
	@pytest.mark.numero
	def test_promedio_float():
		resultado = promedio(10.1,10.3)
		assert resultado == 10.2
		assert type(resultado) is float

	Al ejecutarlo tenemos el siguiente resultado:

	$ pytest test_promedio.py  -v
	======================================================================================== test session starts ========================================================================================
	platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /home/luisams/anaconda3/bin/python
	cachedir: .pytest_cache
	hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Reto-03/.hypothesis/examples')
	rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Reto-03
	plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
	collected 4 items                                                                                                                                                                                   

	test_promedio.py::test_promedio_int PASSED                                                                                                                                                    [ 25%]
	test_promedio.py::test_promedio_int_2 PASSED                                                                                                                                                  [ 50%]
	test_promedio.py::test_promedio_float SKIPPED                                                                                                                                                 [ 75%]
	test_promedio.py::test_promedio_float_2 PASSED                                                                                                                                                [100%]
</details> 



