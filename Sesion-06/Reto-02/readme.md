## Reto 2

### OBJETIVO

- Crear archivos csv incluyendo datos de la ejecución del programa

#### REQUISITOS

1. Python 3

#### DESARROLLO

Basándose en el reto anterior, y con el uso de la librería csv, crea un archivo csv, con los siguientes datos:
 *  modelo de auto,
 * color 
 * nivel de equipamiento(bajo, medio,alto)
 * Fecha de captura (no ingresado por el usuario)

 Para obtener la fecha de captura puedes usar datetime.datetime.now() del paquete datetime

```
Inserte nombre del auto: Sentra 
Inserte color: rojo
inserte nivel de equipo:medio
Inserte precio: 190 000 
Agregar otro auto (s/N)? s

Inserte nombre del auto: murcielago
Inserte color: negro
inserte nivel de equipo:alto 
Inserte precio: 1200000
Agregar otro auto (s/N)? N

$ cat autos.csv 
Sentra,rojo,medio,190 000 ,2020-05-24 21:20:08.790518
murcielago,negro,alto 1200000,1200000,2020-05-24 21:20:36.950413

```
<details>
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


</details>