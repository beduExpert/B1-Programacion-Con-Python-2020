## Archivos .csv

### OBJETIVO

- Crear archivos .csv
- Leer archivos .csv
- Escribir archivos .csv

#### REQUISITOS

1. Python 3

#### DESARROLLO
Los archivos csv (comma separated values), son un formato de archivos conformados por valores separados por una coma, como si fueran un tabla, son muy usados para almacenar sets de datos.

Existen variantes que usan otro carcter para separar los valores, como lo son los tsv(tab separatted values), que usa tabuladores para separar los valores. Estos últimos suelen utilizarse para almacener corpus de oraciones para análisis de lenguaje natural.

El módulo csv cuenta con clases para facilitar leer y escribir archivos csv.
Funcionan de manera similar a los archivos, con conversión del archivo a listas y viceversa.

La forma de utilizarla, conserva ciertas similitudes con el acceso a otros tipos de archivos

`archivo_csv.py`
```
import csv 
# Escribir archivo
with open("ejemplo.csv", 'w') as fcsv: 
    writer = csv.writer(fcsv) 
    writer.writerow(["Nombre", "Apellido", "Genero"]) #Los archivos csv se estructuran en filas
    writer.writerow(["Maria", "Alvarado", "F"]) 
    writer.writerow(["Felipe", "Coutiño", "M"]) 

# Leer archivo csv iterando filas
with open("ejemplo.csv", 'r') as fcsv: 
    reader = csv.reader(fcsv) 
    for row in reader: 
        print(row) # Tipo lista
```

Aunque por defecto el CSV se maneja como listas, es posible que también se maneje como diccionarios, si la primera línea del CSV corresponde. Es posible también elegir el nombre de sus columnas

`archivo_csv_dict.py`

```
import csv

#Se puede usar with también con .csv
#Se pueden usar diccionarios como argumentos para writerow
with open("ejemplod.csv", 'w') as fcsv: 
    fields = ("Nombre", "Apellido", "Edad") 
    writer = csv.DictWriter(fcsv, fieldnames=fields)
    writer.writeheader() 
    writer.writerow({'Nombre': 'Ted', 'Apellido': 'Mosby', 'Edad': 30}) 
    writer.writerow({'Nombre': 'Marshall', 'Apellido': 'Ericksen', 'Edad': 29}) 

with open("ejemplod.csv", 'r') as fcsv: 
    reader = csv.DictReader(fcsv) 
    for row in reader: 
        print(row['Nombre'], row['Apellido'])
```

