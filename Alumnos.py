
class Alumno:

    maxInasistencias = 5
    cantClases = 3

    def __init__(self,nombre='',anio=0,division=0,cantInas=0):
        self.__nombre = nombre
        self.__anio = anio
        self.__division = division
        self.__inasisitencias = cantInas

    def getNom(self):
        return self.__nombre

    def getInasisitencias(self):
        return self.__inasisitencias

    def getAnio(self):
        return self.__anio

    def getDivision(self):
        return self.__division

    @classmethod
    def getMaxInasistencias(cls):
        return cls.maxInasistencias
