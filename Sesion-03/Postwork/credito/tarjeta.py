def crea_tarjeta():
    """
    Función que crea una tarjeta a partir de un formulario 
    """
    capturado = False
    while capturado == False:
        print("Inserta el nombre de tu tarjeta de crédito:")
        nombre = input()

        print("Inserta la tasa de interes de la tarjeta:")
        tasa = float(input())

        print("Inserta la deuda de la tarjeta en el último corte:")
        deuda = int(input())

        print("Inserta el monto total de los pagos realizados durante el último mes:")
        pagos = int(input())

        print("Inserta el monto total de las compras realizadas después del corte:")
        cargos = int(input())

        if pagos > deuda:
            print("ERROR: EL PRODUCTO NO PERMITE REALIZAR PAGOS MAYORES A LA DEUDA ACTUAL")
            print("Vuelve a insertar los datos")
        else:
            capturado = True
    tarjeta_data = {'nombre': nombre, 'tasa':tasa, 'deuda': deuda, 'pagos': pagos, 'cargos': cargos}
    return tarjeta_data


def calcula_nueva_deuda(tarjeta):
    """
    Función que calcula el nivel de deuda para el proximo mes
    """   
    tasa_decimal = tarjeta['tasa']/100
    interes_mensual = tasa_decimal/12
    tarjeta['deuda_recalculada'] = (tarjeta['deuda'] - tarjeta['pagos'])*(1+interes_mensual)
    tarjeta['nueva_deuda'] = tarjeta['deuda_recalculada'] + tarjeta['cargos']
    return tarjeta



def imprime_reporte(tarjeta):
    """
    Función que imprime el reporte de una tarjeta 
    """
    tarjeta = calcula_nueva_deuda(tarjeta)
    print("-------------------------------------------------------------------")
    print("Resumen de información sobre la tarjeta {}".format(tarjeta['nombre']))
    print("Tasa de interes del producto:                    {}".format(tarjeta['tasa']))
    print("Saldo de la tarjeta antes del corte              {}".format(tarjeta['deuda']))
    print("Total de pagos realizados:                       {}".format(tarjeta['pagos']))
    print("Deuda después del corte con intereses aplicados: {}".format(tarjeta['deuda_recalculada']))
    print("Cargos realizados después del corte:             {}".format(tarjeta['cargos']))
    print("Deuda actual:                                    {}".format(tarjeta['nueva_deuda']))
    print("-------------------------------------------------------------------")


def pago_recurrente(tarjeta, monto):
    """
    Función que calcula un pago recurrente sobre la tarjeta con un mionto preestablecido, hasta que la tarjeta quede en cero 
    """
    tarjeta['pagos'] = monto
    tarjeta['cargos'] = 0
    while tarjeta['deuda'] > 0:
        if tarjeta['deuda'] < tarjeta['pagos']:
            tarjeta['pagos'] = tarjeta['deuda']
        imprime_reporte(tarjeta)
        tarjeta['deuda'] = tarjeta['nueva_deuda']

def pagos_distintos(tarjeta, *args):
    """
    Función que calcula un pago recurrente sobre la tarjeta con distintos montos mes a mes 
    """
    tarjeta['cargos'] = 0
    for arg in args:
        tarjeta['pagos'] = arg
        if tarjeta['deuda'] < tarjeta['pagos']:
            tarjeta['pagos'] = tarjeta['deuda']
        imprime_reporte(tarjeta)
        tarjeta['deuda'] = tarjeta['nueva_deuda']

