class Persona:
    def __init__(self, n, s):
        self.__nombre = n
        self.__escuela = s
     
    def get_nombre(self):
        return self.__nombre
         
    def get_escuela(self):
        return self.__escuela

    def describe(self):
        return "{} estudia en {}".format(self.__nombre, self.__escuela)