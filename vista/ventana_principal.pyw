from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class VentanaPrincipal(QMainWindow):

    def __init__(self, controlador):
        self.__controlador = controlador
        QMainWindow.__init__(self)
        uic.loadUi('vista/ui/ventana_principal.ui', self)

        # configuracion de botones

        self.btn_salir.triggered.connect(self.close)

        self.btn_animales_acuaticos.triggered.connect(self.__controlador.gestion_anim_ac)
