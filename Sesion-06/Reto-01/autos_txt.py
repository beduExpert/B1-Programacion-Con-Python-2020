continuar  = True

while continuar:
    nombre = input("Inserte nombre del auto: ")
    color = input("Inserte color: ")
    equipo = input("inserte nivel de equipo:")
    precio = input("Inserte precio: ")
    with open("autos.txt", 'a') as autos_file:
        autos_file.write("{}\t{}\t{}\t{}\n".format(nombre, color, equipo,precio))
    valid = False
    while not valid:
        c = input("Agregar otro hotel (s/N)? ")
        c = c.lower()
        if c.startswith('s'):
            continuar = True
            valid = True
        elif c.startswith('n'):
            continuar = False
            valid = True
        else:
            print("Respuesta no válida")
            valid = False
    print("")
