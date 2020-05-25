import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Mostrar información de depuración", action="store_true")
parser.add_argument("-f", "--file", help="Nombre de archivo a procesar")
args = parser.parse_args()
 
# Aquí procesamos lo que se tiene que hacer con cada argumento
if args.verbose:
    print ("depuración activada!!!")
 
if args.file:
    print ("El nombre de archivo a procesar es: ", args.file)