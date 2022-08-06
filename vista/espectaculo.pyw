import datetime
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import QDate


class VentanaEspectaculo(QDialog):

    def __init__(self, controlador):
        self.__controlador = controlador
        QDialog.__init__(self)
        uic.loadUi('vista/ui/espectaculo.ui', self)

        # Buttons & table data configuration

        self.btn_cerrar.clicked.connect(self.close)
        self.btn_insertar.clicked.connect(self.__controlador.insertar_espectaculo)
        self.btn_actualizar.clicked.connect(self.__controlador.actualizar_espectaculo)
        self.btn_eliminar.clicked.connect(self.__controlador.eliminar_espectaculo)
        self.btn_nuevo_reg.clicked.connect(self.restablecer_datos)
        self.tabla_espectaculos.itemClicked.connect(self.__controlador.llenar_formulario_x_tabla)
        self.tabla_espectaculos.setColumnCount(5)
        self.tabla_espectaculos.setHorizontalHeaderLabels(['Código', 'Nombre', 'Hora de inicio', 'Duración', 'Público'])
        self.tabla_espectaculos.resizeColumnsToContents()

    @property
    def codigo(self):
        return self.txt_codigo.text()

    @codigo.setter
    def codigo(self, value):
        self.txt_codigo.setText(value)

    @property
    def nombre(self):
        return self.txt_nombre.text()

    @nombre.setter
    def nombre(self, value):
        self.txt_nombre.setText(value)

    @property
    def inicio(self):
        return self.time_inicio.QTime()

    @inicio.setter
    def inicio(self, value):
        self.time_inicio.setTime(value)
        
    @property
    def duracion(self):
        return self.spb_duracion.value()
    
    @duracion.setter
    def duracion(self, value):
        self.spb_duracion.setValue()

    @property
    def publico(self):
        return self.cbx_publico.currentText()

    @publico.setter
    def publico(self, value):
        index = self.cbx_publico.findText(value, QtCore.Qt.MatchFixedString)
        self.cbx_publico.setCurrentIndex(index)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def validar_datos(self):
        pass

    def restablecer_datos(self):
        pass

    def vaciar_tabla(self):
        while self.tabla_espectaculos.rowCount() > 0:
            self.tabla_espectaculos.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto):
        self.tabla_espectaculos.setItem(fila, columna, QTableWidgetItem(texto))
