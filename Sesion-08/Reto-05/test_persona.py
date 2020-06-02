from persona import Persona
import pytest



def setup_module(module):
    global alumno1, alumno2
    alumno1 = Persona('Juan', 'UNAM')
    alumno2 = Persona('Ricardo', 'IPN')

def test_nombre():
    assert alumno1.get_nombre() == 'Juan'
    assert alumno2.get_nombre() == 'Ricardo'

def test_escuela():
    assert alumno1.get_escuela() == 'UNAM'
    assert alumno2.get_escuela() == 'IPN'

def test_descripcion():
    assert alumno1.describe() == 'Juan estudia en UNAM'
    assert alumno2.describe() == 'Ricardo estudia en IPN'

