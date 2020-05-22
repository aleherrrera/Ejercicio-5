class Numero:
    __numero:0

    def __init__(self,numero):
        self.__numero=numero

    def __str__(self):
        cadena='%d'%(self.__numero)
        return cadena