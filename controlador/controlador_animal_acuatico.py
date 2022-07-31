from vista.animal_acuatico import VentanaAnimalAcuatico
from controlador.controlador_entrenador import ControladorEntrenador


class ControladorAnimalAcuatico:

    def __init__(self, repo):
        self.vista = VentanaAnimalAcuatico(self)
        self.__repositorio = repo

    # Window main functions
    def iniciar(self):
        self.vista.setWindowTitle('Animales Acuaticos')
        self.vista.show()

    def cerrar(self):
        self.vista.close()

    # Windows calls functions

#    def admin_entrenadores(self):
#        pen = ControladorEntrenador(self.__repositorio)
#       pen.iniciar()

    # Functions for list management

    def last_id(self):
        print(1)
        return 1

    def insertar_animal_acuatico(self):
        pass

    def actualizar_animal_acuatico(self):
        pass

    def eliminar_animal_acuatico(self):
        pass

    def llenar_formulario_x_tabla(self):
        pass

