import sys
from PyQt5.QtWidgets import QApplication
from modelo.repositorio import Repositorio
from vista.animal_acuatico import VentanaAnimalAcuatico
from controlador.controlador_entrenador import ControladorEntrenador


class ControladorAnimalAcuatico:

    def __init__(self, repo):
        self.vista = VentanaAnimalAcuatico(self)
        self.repositorio = repo


    def iniciar(self):
        self.vista.setWindowTitle('Animales Acuaticos')
        self.vista.show()

    def cerrar(self):
        self.vista.close()

    #def admin_entrenadores(self):
    #   pen = ControladorEntrenador(self.__repositorio)
    #    pen.iniciar()