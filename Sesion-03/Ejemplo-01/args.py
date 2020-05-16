#Usamos args cuando queremos que una función acepte un numero no determinado de argumentos
def imprime(*a2gs):  
    for arg in a2gs:  
        print (arg) 
    
imprime('Hola', 'A', 'Todos', '!')

#Se pueden mezclar argumentos comunes con args

def imprime_varias_veces(veces, *argv): 
    for i in range(veces):
        for arg in argv:
            print(arg)

  
imprime_varias_veces(3, 'Bienvenidos ', 'a', 'Bedu') 