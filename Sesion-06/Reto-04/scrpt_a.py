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