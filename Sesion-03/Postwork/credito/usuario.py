from credito.tarjeta import imprime_reporte

def multiples_reportes(tarjetas):
    """
    Función que imprime el reporte de todas las tarjetas de un usuario
    """
    for tarjeta in tarjetas:
        imprime_reporte(tarjeta)