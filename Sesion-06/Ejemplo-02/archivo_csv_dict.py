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