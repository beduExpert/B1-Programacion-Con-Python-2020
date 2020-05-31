import json

class EstudianteDB:
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)

    def get_data(self,nombre):
        for estudiante in self.__data['estudiantes']:
            if estudiante ['nombre'] == nombre:
                return estudiante
