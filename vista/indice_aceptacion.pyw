from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5 import uic


class VentanaIndiceAceptacion(QDialog):

    def __init__(self, presentador):
        self.__presentador = presentador
        QDialog.__init__(self)
        uic.loadUi('vista/ui/indice_aceptacion.ui', self)

        self.btn_cerrar.clicked.connect(self.close)
        self.btn_calcular.clicked.connect(self.__presentador.get_indice)

    # PROPS

    @property
    def id(self):
        return self.sbx_id.value()

    @id.setter
    def id(self, value):
        self.sbx_id.setValue(value)
    
    @property
    def indice(self):
        return self.lb_indice.text()

    @indice.setter
    def indice(self, value):
        self.lb_indice.setText(value)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)
