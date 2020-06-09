def crea_tarjeta():
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
    tasa_decimal = tarjeta['tasa']/100
    interes_mensual = tasa_decimal/12
    tarjeta['deuda_recalculada'] = (tarjeta['deuda'] - tarjeta['pagos'])*(1+interes_mensual)
    tarjeta['nueva_deuda'] = tarjeta['deuda_recalculada'] + tarjeta['cargos']
    return tarjeta



def imprime_reporte(tarjeta):
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

def multiples_reportes(tarjetas):
    for tarjeta in tarjetas:
        imprime_reporte(tarjeta)

def pago_recurrente(tarjeta, monto):
    tarjeta['pagos'] = monto
    tarjeta['cargos'] = 0
    while tarjeta['deuda'] > 0:
        if tarjeta['deuda'] < tarjeta['pagos']:
            tarjeta['pagos'] = tarjeta['deuda']
        imprime_reporte(tarjeta)
        tarjeta['deuda'] = tarjeta['nueva_deuda']


t1 = {'nombre': 'oro', 'tasa': 40.0, 'deuda': 6000, 'pagos': 5000, 'cargos': 1000}
t2 = {'nombre': 'oro2', 'tasa': 30.0, 'deuda': 6000, 'pagos': 5000, 'cargos': 1000}
print(t1)
multiples_reportes([t1,t2])


t3 = {'nombre': 'oro', 'tasa': 40.0, 'deuda': 60000, 'pagos': 5000, 'cargos': 1000}
pago_recurrente(t3, 5000)
#lista_tarjeta = [crea_tarjeta(), crea_tarjeta(), crea_tarjeta()]


