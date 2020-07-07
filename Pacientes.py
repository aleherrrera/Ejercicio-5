import re

class Paciente(object):
    telefonoRegex = re.compile(r"[0-9]{3}-[0-9]{7}")
    alturaRegex = re.compile(r"[0-9]{3}")
    pesoRegex = re.compile(r"[0-9]")
    __apellido= None
    __nombre= None
    __telefono=None
    __altura=None
    __peso=None

    def __init__(self,apellido,nombre,telefono,altura,peso):
        self.__apellido=self.requerido(apellido,'Apellido requerido')
        self.__nombre=self.requerido(nombre,'Nombre requerido')
        self.__telefono=self.formatoValido(telefono,Paciente.telefonoRegex,'Telefono no tiene formato correcto')
        self.__altura=self.formatoValido(altura,Paciente.alturaRegex,'Altura no tiene formato correcto')
        self.__peso=self.formatoValido(peso,Paciente.pesoRegex,'Peso no tiene formato correcto')

    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getTelefono(self):
        return self.__telefono
    def getAltura(self):
        return self.__altura
    def getPeso(self):
        return self.__peso
    def getIMC(self):
        altura=float(float(self.getAltura())/100)
        peso=float(self.getPeso())
        imc = peso / (altura * altura)
        return imc

    def getCompCorporal(self,imc):
        mensaje=None
        if imc < 18.5:
            mensaje='Peso inferior al normal'
        else:
            if imc >= 18.5 and imc < 24.9:
                mensaje = 'Normal'
            else:
                if imc >= 25 and imc < 29.9:
                    mensaje = 'Peso superior al normal'
                else:
                    if imc >= 30:
                        mensaje = 'Obesidad'
        return mensaje

    def requerido(self,valor,mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    def formatoValido(self,valor,regex,mensaje):
        if not valor or not regex.match(valor):
            raise ValueError(mensaje)
        return valor

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                                apellido=self.__apellido,
                                nombre=self.__nombre,
                                telefono=self.__telefono,
                                altura=self.__altura,
                                peso=self.__peso
                            )
            )
        return d