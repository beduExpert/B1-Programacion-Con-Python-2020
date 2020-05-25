## Argumentos en scripts

### OBJETIVO

- Crear archivos de texto plano incluyendo datos de la ejecución del programa

#### REQUISITOS

1. Python 3

#### DESARROLLO


Pedir al usuario una lista, con nombre un nombre de auto, color, nivel de equipamiento(bajo, medio,alto) y precio. Guardar la información en un archivo llamado autos.txt, separado por tabulador. Anexar al final la información si ya existe el archivo.

```
Inserte nombre del auto: Rio
Inserte color: rojo
inserte nivel de equipo:medio
Inserte precio: 210 000
Agregar otro hotel (s/N)? s

Inserte nombre del auto: swift
Inserte color: amarillo
inserte nivel de equipo:bajo
Inserte precio: 11111
Agregar otro hotel (s/N)? N
```
Para concatenar a un archivo, puedes usar el tipo de acceso 'a' (append)

<details>
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
</details> 
