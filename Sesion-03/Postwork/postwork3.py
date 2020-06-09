from credito.tarjeta import crea_tarjeta, pagos_distintos
from credito.usuario import multiples_reportes

t1 = crea_tarjeta()
tarjetas = [t1,t1,t1]
multiples_reportes(tarjetas)

pagos_distintos(t1, 100, 200, 1000)