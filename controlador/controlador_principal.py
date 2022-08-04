import sys
from datetime import date
from PyQt5.QtWidgets import QApplication
from modelo.repositorio import Repositorio
from modelo.entrenador import Entrenador
from vista.ventana_principal import VentanaPrincipal
from controlador.controlador_animal_acuatico import ControladorAnimalAcuatico
from controlador.controlador_entrenador import ControladorEntrenador
from controlador.controlador_planta_acuatica import ControladorPlantaAcuatica


class ControladorPrincipal:

    def __init__(self):
        self.__repositorio = Repositorio()

        entrenador1 = Entrenador('98765432132','Elizabeth Perez Usbert', 'Eli', '26', 'F', date(1998, 6, 16), '3')
        entrenador2 = Entrenador('20041226321', 'Pedro Hernandez Gonzalez', 'Pepe', '20', 'M', date(2004, 12, 26), '1')

        self.__repositorio.lista_entrenadores.append(entrenador1)
        self.__repositorio.lista_entrenadores.append(entrenador2)

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

    def gestion_planta_ac(self):
        pen = ControladorPlantaAcuatica(self.__repositorio)
        pen.iniciar()