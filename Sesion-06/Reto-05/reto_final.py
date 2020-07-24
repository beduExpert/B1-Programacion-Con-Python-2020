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

