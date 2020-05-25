
#La sentencia with coloca la lectura o escritura del archivo en una estructura que lo cierra al terminar
with open("arch2.txt", 'w') as archivo: 
    archivo.write("Primer linea de este archivo\n") 
    archivo.writelines(['Multiples Lineas\n', 'En Lista']) 
                                                                                                                                                 
with open("arch2.txt", 'r') as archivo: 
    print(archivo.readline()) 
    print(archivo.readlines())  
