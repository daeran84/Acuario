from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5 import uic


class VentanaFamiliaPlantas(QDialog):

    def __init__(self, controlador):
        self.__controlador = controlador
        QDialog.__init__(self)
        uic.loadUi('vista/ui/familia_plantas.ui', self)

        self.btn_cerrar.clicked.connect(self.close)
        self.btn_calcular.clicked.connect(self.__controlador.get_indice_familia)
    
    @property
    def familia(self):
        return self.lb_familia.text()
    
    @familia.setter
    def familia(self, value):
        self.lb_familia.setText(value)
    
    # Functions

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)
