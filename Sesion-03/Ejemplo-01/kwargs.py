#Usamos kwargs para pasar parametros poe nombre y no por posicion

def saludo(**kwargs):
    print('Hola {} de {}'.format(kwargs['nombre'], kwargs['empresa']))

saludo(empresa='Bedu',nombre='Luis')
saludo(nombre='Luis',empresa='Bedu')

#Podemos extraer llaves y valores de kwargs como de diccionarios
def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
myFun(nombre ='Fernando', empresa ='Bedu', ciudad='CDMX') 