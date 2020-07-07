from RepositorioPacientes import RepositorioPacientes
from vistaPacientes import PacientesView
from ControladorPacientes import ControladorPacientes
from ObjectEncoder import ObjectEncoder

def main():
    conn=ObjectEncoder('pacientes.json')
    repo=RepositorioPacientes(conn)
    vista=PacientesView()
    ctrl=ControladorPacientes(repo,vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__=='__main__':
    main()