from credito.tarjeta import Tarjeta_de_credito
from credito.servicios import Tarjeta_de_servicios

tarjeta1 = None
tarjeta2 = None
def setup_module(module):
    global tarjeta1 
    global tarjeta2
    tarjeta1 = Tarjeta_de_credito(nombre='a', deuda=10000, pagos = 5000, cargos=100, tasa = 0)
    tarjeta2 = Tarjeta_de_servicios(nombre='b', deuda=10000, cargos = 29)


#teardown_module sirve para acciones que de realizan al final
#def teardown_module(module):


def test_tarjeta_credito():
    assert tarjeta1.get_nombre() == 'a'
    assert tarjeta1.get_deuda() == 10000
    tarjeta1.imprime_reporte()
    assert tarjeta1.get_nueva_deuda() == 5100

def test_tarjeta_servicio():
    assert tarjeta2.get_nombre() == 'b'
    assert tarjeta2.get_pagos() == 10000
    tarjeta2.imprime_reporte()
    assert tarjeta2.get_nueva_deuda() == 29

def test_reporte():
    a = tarjeta1.get_reporte()
    assert len(a) > 20
    assert type(a) == str

def test_reporte_html():
    a = tarjeta2.get_reporte_html()
    assert len(a) > 20
    assert type(a) == str

