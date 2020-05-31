

## Pytest básicos

### OBJETIVO

- LRealizar tests unitarios usando Pytest
- Ejecutar Pytest desde la terminal

#### REQUISITOS

1. Python 3
2. Pytest

#### DESARROLLO

Pytest es un paquete que nos permite automatizar pruebas unitarias de software escrito en Python.

Si no tienes instalado Pytest, puedes instalarlo usando PIP
´´´
$pip install pytest
´´´

Al utilizar Pytest, se suelen utilizar sentencias assert, este tipo de sentencias se evaluan, en caso de resultar True la ejecución de un programa continua, en caso contrario se lanza una señal de error.

Para realizar nuestro primer ejercicio de Pytest, necesitamos crear un módulo con las funciones a utilizar.

´´´
def suma(a , b=0):
    return a + b

def producto(a,b=1):
    return a*b

´´´

Para usar pytest creamos otro archivo .py, cuyo nombre comienza por test. En el cual importamos el módulo con las funciones a probar.

En este archivo podemos crear las funciones con nobre test_funcion(), en estas podemos incluir sentencias assert que llamen a la función a testear y las podemos comparar con el valor de return esperado. 

´´´
import operaciones

def test_suma():
    assert operaciones.suma(2,3) ==5
    assert operaciones.suma(2)==2

def test_producto():
    assert operaciones.producto(3,5) == 15
    assert operaciones.producto(2) == 2


´´´

Para ejecutar la prueba podemos dirigirnos en terminal a la carpeta contenedora de nuestro proyecto y ejecutamos
´´´
$pytest test_operaciones.py
´´´
En este caso la prueba es aprobada así que vemos el siguiente mensaje
´´´
$ pytest test_operaciones.py
======================================================================================== test session starts ========================================================================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-01
plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
collected 2 items                                                                                                                                                                                   

test_operaciones.py ..                                                                                                                                                                        [100%]

========================================================================================= 2 passed in 0.02s =========================================================================================
´´´

En caso de de que la función evaluada contenga errores, por ejemplo si modificamos la función suma de la siguiente manera 
´´´
def suma(a , b=0):
    return a - b
´´´
Podemos ver la siguiente salida en la terminal
´´´
======================================================================================== test session starts ========================================================================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-01
plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
collected 2 items                                                                                                                                                                                   

test_operaciones.py F.                                                                                                                                                                        [100%]

============================================================================================= FAILURES ==============================================================================================
_____________________________________________________________________________________________ test_suma _____________________________________________________________________________________________

    def test_suma():
>       assert operaciones.suma(2,3) ==5
E       assert -1 == 5
E        +  where -1 = <function suma at 0x7f491594f830>(2, 3)
E        +    where <function suma at 0x7f491594f830> = operaciones.suma

test_operaciones.py:4: AssertionError
==================================================================================== 1 failed, 1 passed in 0.03s ====================================================================================
´´´
De forma similar se debe tener cuidado al crear las funciones test, por que si existe algún error en ella por ejemplo
´´´
def test_suma():
    assert operaciones.suma(2,3) ==4
    assert operaciones.suma(2)==2

´´´

También se provocará un error  


