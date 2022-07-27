import sys
from PyQt5.QtWidgets import QApplication
from modelo.repositorio import Repositorio
from vista.ventana_principal import VentanaPrincipal
from controlador.controlador_animal_acuatico import ControladorAnimalAcuatico
from controlador.controlador_entrenador import ControladorEntrenador


class ControladorPrincipal:

    def __init__(self):
        self.__repositorio = Repositorio()

    # Main start and child windows call functions

    def iniciar(self):
        app = QApplication(sys.argv)
        self.vista = VentanaPrincipal(self)
        self.vista.setWindowTitle('Acuario')
        self.vista.show()
        app.exec_()

    def gestion_anim_ac(self):
        pen = ControladorAnimalAcuatico(self.__repositorio)
        pen.iniciar()

    def gestion_entrenadores(self):
        pen = ControladorEntrenador(self.__repositorio)
        pen.iniciar()

