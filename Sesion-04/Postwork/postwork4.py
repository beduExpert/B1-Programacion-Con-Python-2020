from credito.tarjeta import Tarjeta_de_credito
from credito.usuario import usuario

t1 = Tarjeta_de_credito(nombre='oro', tasa=24, deuda=20000, pagos=1300)
t1.imprime_reporte()

t2 = Tarjeta_de_credito(nombre='platino', tasa=24, deuda=2000, pagos=1300)
t2.imprime_reporte()


usuario1 = usuario(nombre='Juan', tarjetas=[t1])
usuario1.agrega_tarjeta(t2)
usuario1.multiples_reportes()
usuario1.cancela_tarjeta('oro')

usuario1.multiples_reportes()