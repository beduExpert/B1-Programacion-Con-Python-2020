 

	
## Reto tests 4

### OBJETIVO 


1. Se incluiran marks en los text
2. Inclir skips en los test
3. Filtrar los tests a realzar de distinta manera

#### REQUISITOS 
- Python 3
- Pytest

#### DESARROLLO

Vamos a agregar parametrización al pequeño proyecto de calificaciones:
Esto no ayudará a probar nuestra función con varias entradas y salidas, sin tener
que estar repitiendo código.

Crea mínimo 10 parámetros para la pruebas de la función de promedio de calificaciones.
Procura que cubras al menos una vez los siguientes casos:

- La calificación de 6.5, 7.5... no sube a 7 u 8.
- Calificaciones como 5.9 si suben a 6.
- Calificaciones negativas no son posibles, cambian a 0.
- Calificaciones mayores a 10 no son posibles, cambian a 10.

Revisa que el test corra correctamente con todos los parámetros.

<details>

	Se creo el siguiente archivo para tests

	from promedio import promedio
	import pytest

	@pytest.mark.parametrize('num1, num2, resultado',[
						(2,3,2.5),
						(2,0,1),
						(2,4,3),
						(10,11,10.5),
						(10.1,10.3,10.2),
						(1,1,1),
						(6.0,6.5,6.25,),
						(15,10,12.5),
						(0,0,0),
						(6,5.5,5.75)
					])
	def test_promedio(num1,num2,resultado):
		res = promedio(num1,num2)
		assert res == resultado
		assert type(res) is float

	Al ejecutar esta prueba tenemos el siguiente resultado

	$ pytest -v
	======================================================================================== test session starts ========================================================================================
	platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /home/luisams/anaconda3/bin/python
	cachedir: .pytest_cache
	hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Reto-04/.hypothesis/examples')
	rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Reto-04
	plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
	collected 10 items                                                                                                                                                                                  

	test_promedio.py::test_promedio[2-3-2.5] PASSED                                                                                                                                               [ 10%]
	test_promedio.py::test_promedio[2-0-1] PASSED                                                                                                                                                 [ 20%]
	test_promedio.py::test_promedio[2-4-3] PASSED                                                                                                                                                 [ 30%]
	test_promedio.py::test_promedio[10-11-10.5] PASSED                                                                                                                                            [ 40%]
	test_promedio.py::test_promedio[10.1-10.3-10.2] PASSED                                                                                                                                        [ 50%]
	test_promedio.py::test_promedio[1-1-1] PASSED                                                                                                                                                 [ 60%]
	test_promedio.py::test_promedio[6.0-6.5-6.25] PASSED                                                                                                                                          [ 70%]
	test_promedio.py::test_promedio[15-10-12.5] PASSED                                                                                                                                            [ 80%]
	test_promedio.py::test_promedio[0-0-0] PASSED                                                                                                                                                 [ 90%]
	test_promedio.py::test_promedio[6-5.5-5.75] PASSED                                                                                                                                            [100%]

	======================================================================================== 10 passed in 0.05s ========================================================================================
</details> 

