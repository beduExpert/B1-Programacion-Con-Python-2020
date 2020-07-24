## Reto 6

### OBJETIVO

- Ejecuta un programa como script y recibe argumentos
- Realiza lectura de archivos csv
- Escribe archivos de texto plano

#### REQUISITOS

1. Python 3

#### DESARROLLO
- Crea un script que tome la ruta de un archivo csv, con el formato del ejemplo.csv


```
Marco, 34, CDMX
```
Y lo convierta en unarchivo .txt (especificado en el segundo argumento del script), con el formato

```
Nombre = Marco, Edad = 34, Ciudad = CDMX
```


<details>
    import sys
    import csv 

    ruta = sys.argv[1]
    salida = sys.argv[2]
    archivoSal = open(salida, 'w')
    print(ruta)
    with open(ruta, 'r') as fcsv: 
        reader = csv.reader(fcsv) 
        for row in reader: 
            cadena = "Nombre = {}, Edad ={}, Ciudad ={}\n".format(row[0], row[1], row[2])
            archivoSal.write(cadena)

    archivoSal.close()


</details>
