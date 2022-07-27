from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox



class VentanaPrincipal(QMainWindow):

    def __init__(self, controlador):
        self.__controlador = controlador
        QMainWindow.__init__(self)
        uic.loadUi('vista/ui/ventana_principal.ui', self)

        # Windows call buttons configuration

        self.btn_salir.triggered.connect(self.close)
        self.btn_animales_acuaticos.triggered.connect(self.__controlador.gestion_anim_ac)
        self.btn_entrenadoes.triggered.connect(self.__controlador.gestion_entrenadores)

    # Start, close and message functions, nothing more should appear next #

    def iniciar(self):
        self.show()

    def cerrar(self):
        self.close()

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)
