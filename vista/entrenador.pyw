from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5 import uic


class VentanaEntrenador(QWidget):

    def __init__(self, repo):
        self.__repositorio = repo
        QWidget.__init__(self)
        uic.loadUi('vista/ui/entrenador.ui', self)

        # configuracion de botones

        self.btn_cerrar.triggered.connect(self.close)