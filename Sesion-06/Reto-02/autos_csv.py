import csv
import datetime

def add_car():
    nombre = input("Inserte nombre del auto: ")
    color = input("Inserte color: ")
    equipo = input("inserte nivel de equipo:")
    precio = input("Inserte precio: ")
    fecha_actual = datetime.datetime.now()
    with open("autos.csv", "a") as fcsv:
        writer = csv.writer(fcsv)
        writer.writerow([nombre, color, equipo, precio, fecha_actual])



cont = True
while cont:
    add_car()
    c = input("Agregar otro auto (s/N)? ")
    c = c.lower()
    if c.startswith("n") or c == "":
        cont = False
    elif c.startswith("s"):
        pass
    else:
        print("Comando no reconocido. Escriba si o no.")
    print("")

