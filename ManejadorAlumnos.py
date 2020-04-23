from Alumnos import Alumno

class Lista:

    __alumnos = []

    def __init__(self):
        self.__alumnos = []

    def agregarAlumno(self,alumno):
        self.__alumnos.append(alumno)

    def cargarLista(self):
        import csv
        archivo = open('ListadoAlumnos.csv')
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            nom = fila[0]
            anio = int(fila[1])
            div = int(fila[2])
            inas = int(fila[3])
            unAlumno = Alumno(nom,anio,div,inas)
            self.agregarAlumno(unAlumno)
        archivo.close()

    def inasisMax(self,anio,div,max,alumno):
        if (alumno.getAnio() == anio) and (alumno.getDivision() == div):
            if alumno.getInasisitencias() > max:
                nom = alumno.getNom()
                inas = alumno.getInasisitencias()
                porcentaje = (inas*100)/max
                print(' {}         {}%'.format(nom,porcentaje))

    def muestraPorcentaje(self,anio,div,max):
        print('ALUMNO     PORCENTAJE')
        for alumno in self.__alumnos:
            self.inasisMax(anio,div,max,alumno)
