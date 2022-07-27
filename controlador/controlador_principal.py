import sys
from PyQt5.QtWidgets import QApplication
from modelo.repositorio import Repositorio
from vista.ventana_principal import VentanaPrincipal
from controlador.controlador_animal_acuatico import ControladorAnimalAcuatico


class ControladorPrincipal:

    def __init__(self):
        self.__repositorio = Repositorio()

    def iniciar(self):
        app = QApplication(sys.argv)
        self.__vista = VentanaPrincipal(self)
        self.__vista.show()
        app.exec()

    def gestion_anim_ac(self):
        pen = ControladorAnimalAcuatico(self.__repositorio)
        pen.iniciar()



