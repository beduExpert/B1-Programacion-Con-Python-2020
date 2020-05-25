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
