from zope.interface import implementer
from Interfaces import IConjunto
from Numero import Numero

@implementer(IConjunto)

class Conjunto:
    __numeros = []

    def __init__(self):
        self.__numeros = []

    def Cargar(self):
        cant = int(input('Ingresar cantidad de numeros para el conjunto: '))
        print('Ingrese {} numeros'.format(cant))
        for i in range(cant):
            num = int(input(''))
            unNumero=Numero(num)
            self.__numeros.append(unNumero)

    def insertarElemento(self,posicion):
        if posicion<len(self.__numeros) and posicion>=0:
            num = int(input('Ingresar numero: '))
            unNumero=Numero(num)
            self.__numeros  .insert(posicion,unNumero)
        else:
            raise Exception('Posicion incorrecta')

    def agregarElemento(self):
        num=int(input('Ingresar numero: '))
        self.__numeros.append(num)

    def mostrarElemento(self,posicion):
        if posicion<len(self.__numeros) and posicion>=0:
            print(self.__numeros[posicion])
        else:
            raise Exception('Posicion incorrecta')

    def Mostrar(self):
        for i in range(len(self.__numeros)):
            print(self.__numeros[i])