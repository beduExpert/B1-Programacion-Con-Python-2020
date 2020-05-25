## Reto 4

### OBJETIVO

- Ejecuta un programa como script y recibe argumentos

#### REQUISITOS

1. Python 3

#### DESARROLLO
- Crea un script que reciba como argumentos un nombre de archivo y un número
- Usa argparse para parsear tus argumentos(con nombre)
- El script debe imprimir la linea del archivo solicitada por el número

```
python scrpt_a.py -f readme.md -l 10
* Capturar la excepción en caso de que el argumento sea un archivo e informar al usuario del error.
```

<details>
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Mostrar información de depuración", action="store_true")
    parser.add_argument("-f", "--file", help="Nombre de archivo a procesar")
    parser.add_argument("-l","--line", help="Veces que se imprimirá el contenido del archivo")
    args = parser.parse_args()
    
    # Aquí procesamos lo que se tiene que hacer con cada argumento
    if args.verbose:
        print ("depuración activada!!!")
    
    if args.file:
        archivo=open(args.file,'r')
        contador = 1
        for linea in archivo:
            if int(args.line) == contador:
                print (linea)
            contador += 1
</details>
