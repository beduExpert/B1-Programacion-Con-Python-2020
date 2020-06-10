from credito.tarjeta import Tarjeta_de_credito
from credito.servicios import Tarjeta_de_servicios
from credito.usuario import usuario


t1 = Tarjeta_de_servicios(nombre='oro', deuda=20000)
t1.imprime_reporte()

t2 = Tarjeta_de_credito(nombre='platino', tasa=24, deuda=2000, pagos=1300)
t2.imprime_reporte()

usuario1 = usuario(nombre='Juan', tarjetas=[t1,t2])

t2.crea_json()
t5 = Tarjeta_de_credito()
t5.lee_json('tarjeta_platino.json')

usuario2 = usuario(nombre='Alejandra', tarjetas=[t5])

t3 = Tarjeta_de_credito(nombre='gris', deuda=20000, pagos=1200, cargos=100, tasa = 22)
usuario3 = usuario(nombre='Pedro', tarjetas=[t3])

base_de_usuarios = [usuario1,usuario2,usuario3]
