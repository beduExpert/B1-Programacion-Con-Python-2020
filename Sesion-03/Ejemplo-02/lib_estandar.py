# Importando modulos desde la libreria estandar
import os 

# Obteniendo ayuda sobre el modulo
help(os)

# Lista de archivos
# q para salir, jk para moverse arriba / abajo
files = os.listdir()
print(files)

# Obteniendo el tamaño de un archivo en kB   

size = os.path.getsize('Readme.md')
print(size)

# Otras maneras de importar modulos
import os.path # Solo algun submodulo, llamando os.path
from os import path # Similar, se llama path directamente