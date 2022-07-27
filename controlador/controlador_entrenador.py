import sys
from PyQt5.QtWidgets import QApplication
from modelo.repositorio import Repositorio
from vista.entrenador import VentanaEntrenador


class ControladorEntrenador:

    def __init__(self):
        self.vista = VentanaEntrenador(self)
        self.repositorio = Repositorio()

    def iniciar(self):
        self.vista.setWindowTitle('Entrenadores')
        self.vista.show()

    def cerrar(self):
        self.vista.close()
