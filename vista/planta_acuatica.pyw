from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5 import QtCore
from PyQt5 import uic


class VentanaPlantaAcuatica(QDialog):

    def __init__(self, controlador):
        self.__controlador = controlador
        QDialog.__init__(self)
        uic.loadUi('vista/ui/planta_acuatica.ui', self)

        self.btn_cerrar.clicked.connect(self.close)
        self.btn_insertar.clicked.connect(self.__controlador.insertar_planta_acuatica)
        self.btn_actualizar.clicked.connect(self.__controlador.actualizar_planta_acuatica)
        self.btn_eliminar.clicked.connect(self.__controlador.eliminar_planta_acuatica)
        self.btn_nuevo_reg.clicked.connect(self.restablecer_datos)
        self.tabla_planta_acuatica.itemClicked.connect(self.__controlador.llenar_formulario_x_tabla)
        self.tabla_planta_acuatica.setColumnCount(6)
        self.tabla_planta_acuatica.setHorizontalHeaderLabels(['ID', 'Nombre científico', 'Familia', 'hábitat natural', 'Número de ejemplares', 'De aguas profundas'])
        self.tabla_planta_acuatica.resizeColumnsToContents()

    # PROPS

    @property
    def id(self):
        return self.lb_id.text()

    @id.setter
    def id(self, value):
        self.lb_id.setText(value)

    @property
    def nombre_cient(self):
        return self.valor_nombre_cient.text()

    @nombre_cient.setter
    def nombre_cient(self, value):
        self.valor_nombre_cient.setText(value)

    @property
    def planta_familia(self):
        return self.cbx_familia.currentText()

    @planta_familia.setter
    def planta_familia(self, value):
        index = self.cbx_familia.findText(value, QtCore.Qt.MatchFixedString)
        self.cbx_familia.setCurrentIndex(index)

    @property
    def planta_habitat(self):
        return self.cbx_habitat.currentText()
    
    @planta_habitat.setter
    def planta_habitat(self, value):
        index = self.cbx_habitat.findText(value, QtCore.Qt.MatchFixedString)
        self.cbx_habitat.setCurrentIndex(index)
    
    @property
    def ejemplares(self):
        return self.sb_ejemplares.text()
    
    @ejemplares.setter
    def ejemplares(self, value):
        self.sb_ejemplares.setValue(value)

    @property
    def aguas_profundas(self):
        if self.check_profundas.isChecked():
            prof = 'Si'
        else:
            prof = 'No'
        return prof

    @aguas_profundas.setter
    def aguas_profundas(self, value):
        if value == 'Si':
            self.check_profundas.setChecked(True)
        else:
            self.check_profundas.setChecked(False)

    # Functions

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def validar_datos(self):
        msg = 'El atributo {} es obligatorio.'
        nombre_c = self.nombre_cient
        familia = self.planta_familia
        habitat = self.planta_habitat
        ejemplares = self.ejemplares

        if nombre_c == '':
            raise Exception(msg.format('nombre científico'))
        if not nombre_c.replace(' ', '').isalpha():
            raise Exception('El nombre científico solo puede tener letras')

        if familia == '':
            raise Exception(msg.format('familia'))

        if habitat == '':
            raise Exception(msg.format('hábitat'))

        if ejemplares == '0':
            raise Exception('los números de ejemplares no pueden ser 0')

    def restablecer_datos(self):
        self.__controlador.get_id()
        self.nombre_cient = ''
        self.planta_familia = ''
        self.planta_habitat = ''
        self.ejemplares = 0
        self.aguas_profundas = 'No'

    def vaciar_tabla(self):
        while self.tabla_planta_acuatica.rowCount() > 0:
            self.tabla_planta_acuatica.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto):
        self.tabla_planta_acuatica.setItem(fila, columna, QTableWidgetItem(texto))
