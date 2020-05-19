#Para crear una clase usamos la palabra reservada class
#Para crear metodos usamos def
#self se refiere a los elementos(atributos y metodos) de la misma clase
class Persona:
    def asignar_nombre(self,nombre):
        self.nombre = nombre
    def saluda(self):
        print("hola, soy {}".format(self.nombre))

#Crea objetos de clase persona
doctor = Persona()
ingeniero = Persona()

#Asignar a atributos
ingeniero.nombre = 'Gabriel'


#Usa Metodos de clase
doctor.asignar_nombre('Miguel')

#Accede a atributos
print(doctor.nombre)

ingeniero.saluda()
doctor.saluda()