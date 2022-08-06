from vista.espectaculo import VentanaEspectaculo
from PyQt5.QtCore import QDate
from datetime import date


class ControladorEspectaculo:

    def __init__(self, repo):
        self.__vista = VentanaEspectaculo(self)
        self.__repositorio = repo

    # Window main functions

    def iniciar(self):
        self.__vista.setWindowTitle('Espectaculos')
        #self.cargar_datos()
        self.__vista.show()

    def cerrar(self):
        self.__vista.close()

    # Functions for list management