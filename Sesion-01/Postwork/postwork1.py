print("Inserta el nombre de tu tarjeta de crédito:")
nombre = input()

print("Inserta la tasa de interes de la tarjeta:")
tasa = float(input())
tasa_decimal = tasa/100

print("Inserta la deuda de la tarjeta en el último corte:")
deuda = int(input())

print("Inserta el monto total de los pagos realizados durante el último mes:")
pagos = int(input())

print("Inserta el monto total de las compras realizadas después del corte:")
cargos = int(input())

if pagos > deuda:
    print("ERROR: EL PRODUCTO NO PERMITE REALIZAR PAGOS MAYORES A LA DEUDA ACTUAL")
else:
    interes_mensual = tasa_decimal/12
    deuda_recalculada = (deuda - pagos45)*(1+interes_mensual)
    nueva_deuda = deuda_recalculada + cargos

    print("-------------------------------------------------------------------")
    print("Resumen de información sobre la tarjeta {}".format(nombre))
    print("Tasa de interes del producto:                    {}".format(tasa))
    print("Saldo de la tarjeta antes del corte              {}".format(deuda))
    print("Total de pagos realizados:                       {}".format(pagos))
    print("Deuda después del corte con intereses aplicados: {}".format(deuda_recalculada))
    print("Cargos realizados después del corte:             {}".format(cargos))
    print("Deuda actual:                                    {}".format(nueva_deuda))
    print("-------------------------------------------------------------------")


