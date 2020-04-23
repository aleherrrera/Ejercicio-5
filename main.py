from Alumnos import Alumno
from ManejadorAlumnos import Lista

def opcion0():
    print("Adiós")

def opcion1():
    print("Ingresar año y division:")
    anio = int(input('Año:'))
    div = int(input('Division:'))
    max = Alumno.getMaxInasistencias()
    ListaAlumno.muestraPorcentaje(anio,div,max)

def opcion2():
    max = int(input("Ingrese cantidad maxima de inasistencias:"))
    Alumno.maxInasistencias = max
    actual = Alumno.getMaxInasistencias()
    print('Se cambio la cantida maxima de inasistencias a {}'.format(actual))

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':

    ListaAlumno = Lista()
    ListaAlumno.cargarLista()

    bandera = False  # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("")
        print("0 Salir")
        print("1. Listado de alumnos que superen la cantidad de inasistencias maximas")
        print('2. Cambiar la cantidad de inasistencias')
        opcion = int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion) == 0  # Si lee el 0 cambia la bandera a true y sale del menú
