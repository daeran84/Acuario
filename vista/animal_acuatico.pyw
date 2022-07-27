from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5 import uic


class VentanaAnimalAcuatico(QWidget):

    def __init__(self, repo):
        self.__repositorio = repo
        QWidget.__init__(self)
        uic.loadUi('vista/ui/animal_acuatico.ui', self)

        # configuracion de botones

        self.btn_cerrar.clicked.connect(self.close)
        #self.btn_administrar_entrenadores.triggered.connect(self.__controlador.admin_entrenadores)

