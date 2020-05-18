#En este ejemplo se sobrecarga el método mensaje
class Persona():
     def __init__(self):
       self.cedula = 13765890
     def mensaje(self):
         print("mensaje desde la clase Persona")

class Obrero(Persona):
     def __init__(self):
         self.__especialista = 1
     def mensaje(self):
         print("mensaje desde la clase Obrero")

obrero_planta = Obrero()
obrero_planta.mensaje()



# Debido a que todas las clases heredan del objeto de clase, también es posible sobre cargar 
# algunos operadores

class Punto:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return x, y

punto1 = Punto(4,6)
punto2 = Punto(1,-2)
print (punto1 + punto2)
