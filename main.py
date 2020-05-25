from Conjunto import Conjunto

def opcion0():
        print("Adiós")

def opcion1():
    Lista.Cargar()
    Lista.Mostrar()

def opcion2():
    posicion = int(input('Ingresar posicion: '))
    try:
        Lista.insertarElemento(posicion-1)
    except IndexError:
        print('Posicion incorrecta')

def opcion3():
    Lista.agregarElemento()
    Lista.Mostrar()

def opcion4():
    posicion = int(input('Ingresar posicion: '))
    try:
        Lista.mostrarElemento(posicion-1)
    except IndexError:
        print('Posicion incorrecta')

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':
    Lista = Conjunto()

    bandera = False  # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("")
        print("0 Salir")
        print("1. Cargar el conjunto numerico")
        print("2. Insertar un elemento en el conjunto")
        print("3. Agregar un elemento al final del conjunto")
        print('4. Mostrar un elemento del conjunto')
        opcion = int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion) == 0  # Si lee el 0 cambia la bandera a true y sale del menú