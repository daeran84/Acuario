import datetime
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import QDate


class VentanaEntrenador(QDialog):

    def __init__(self, controlador):
        self.__controlador = controlador
        QDialog.__init__(self)
        uic.loadUi('vista/ui/entrenador.ui', self)

        # Buttons & table data configuration

        self.btn_cerrar.clicked.connect(self.close)
        self.btn_incertar.clicked.connect(self.__controlador.incertar_entrenador)
        self.btn_actualizar.clicked.connect(self.__controlador.actualizar_entrenador)
        self.btn_eliminar.clicked.connect(self.__controlador.eliminar_entrenador)
        #self.tabla_entrenadores.itemClicked.connect(self.__controlador.llenar_formulario_x_tabla)
        #self.tabla_entrenadores.setColumnCount(8)
        #self.tabla_entrenadores.setHorizontalHeaderLabels(
        #    ['Nombre', 'CI', 'Fecha de Inicio', '# Metros Cuadrados', '# Cuartos',
        #     'Direccion', 'Cochera',
        #     'Tipo de Techo'])
        #self.tabla_entrenadores.resizeColumnsToContents()
        #self.date_nacimiento.setMaximumDate(QDate.currentDate())
        #self.date_nacimiento.setDate(QDate.currentDate())

    # PROPS of fields

    @property
    def ci(self):
        return self.valor_ci.text().strip()

    @ci.setter
    def ci(self, value):
        self.valor_ci.setText(value)

    @property
    def nombre_apellidos(self):
        return self.velor_nombre_apellidos.text().strip()

    @nombre_apellidos.setter
    def nombre_apellidos(self, value):
        self.velor_nombre_apellidos.setText(value)

    @property
    def nombre_artistico(self):
        return self.valor_nombre_artistico.text().strip()

    @nombre_artistico.setter
    def nombre_artistico(self, value):
        self.valor_nombre_artistico.setText(value)

    @property
    def edad(self):
        return self.valor_edad.text().strip()

    @edad.setter
    def edad(self, value):
        self.valor_edad.setText(value)

    @property
    def sexo(self):
        return self.valor_sexo.text().strip()

    @sexo.setter
    def sexo(self, value):
        self.valor_sexo.setText(value)

    @property
    def fecha_nacimiento(self):
        return self.date_nacimiento.date()

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        self.date_nacimiento.setDate(value)

    @property
    def anios_experiencia(self):
        return self.valor_experiencia.text().strip()

    @anios_experiencia.setter
    def anios_experiencia(self, value):
        self.valor_experiencia.setText(value)

