from PyQt5.QtWidgets import QDialog
from PyQt5 import uic


class VentanaFamiliaPlantas(QDialog):

    def __init__(self, presentador):
        self.__presentador = presentador
        QDialog.__init__(self)
        uic.loadUi('vista/ui/familia_plantas.ui', self)

        self.btn_cerrar.clicked.connect(self.close)
        self.btn_calcular.clicked.connect(self.__presentador.get_familia_plantas_mas_representada)

    @property
    def familia(self):
        return self.lb_familia.text()
    
    @familia.setter
    def familia(self, value):
        self.lb_familia.setText(value)
    
