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
        #self.btn_insertar.clicked.connect(self.__controlador.incertar_entrenador)
        #self.btn_modificar.clicked.connect(self.__controlador.actualizar_entrenador)
        #self.btn_eliminar.clicked.connect(self.__controlador.eliminar_entrenador)
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
    
    """@property
    def valor_nombre_apellidos(self):
        return self.valor_nombre_apellidos.text().strip()
    
    @valor_nombre_apellidos.setter
    def valor_nombre_apellidos(self, value):
        self.valor_nombre_apellidos.setText(value)
    
    @property
    def valor_nombre_artistico(self):
        return self.valor_nombre_artistico.text().strip()
    
    @valor_nombre_artistico.setter
    def valor_nombre_artistico(self, value):
        self.valor_nombre_artistico.setText(value)
        
    @property
    def valor_ci(self):
        return self.valor_ci.text().strip()
    
    @valor_ci.setter
    def valor_ci(self, value):
        self.valor_ci.setText(value)
    
    @property
    def valor_experiencia(self):
        return self.valor_ci.text().strip()
    
    @valor_experiencia.setter
    def valor_experiencia(self, value):
        self.valor_ci.setText.strip(value)

    @property
    def date_nacimiento(self):
        return self.date_nacimiento.date()

    @date_nacimiento.setter
    def date_nacimiento(self, value):
        self.date_nacimiento.setDate(value)

    @property
    def valor_edad(self):
        return self.valor_edad.text().strip()

    @valor_edad.setter
    def valor_edad(self, value):
        self.valor_edad.setText.strip(value)"""