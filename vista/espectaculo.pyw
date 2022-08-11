import datetime
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import QTime


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
        self.tabla_espectaculos.setColumnCount(6)
        self.tabla_espectaculos.setHorizontalHeaderLabels(['Código', 'Nombre', 'Hora de inicio', 'Duración', 'Público', 'Animales que participan'])
        self.tabla_espectaculos.resizeColumnsToContents()
        self.cbx_tipo.activated[str].connect(self.__controlador.cargar_datos_combobox)

    # PROPS

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
        return self.time_inicio.text()

    @inicio.setter
    def inicio(self, value):
        self.time_inicio.setTime(value)
        
    @property
    def duracion(self):
        return self.spb_duracion.text()
    
    @duracion.setter
    def duracion(self, value):
        self.spb_duracion.setValue(value)

    @property
    def publico(self):
        return self.cbx_publico.currentText()

    @publico.setter
    def publico(self, value):
        index = self.cbx_publico.findText(value, QtCore.Qt.MatchFixedString)
        self.cbx_publico.setCurrentIndex(index)
        
    # Animals selection PROPS
    
    @property
    def tipo(self):
        return self.cbx_tipo.currentText()
    
    @tipo.setter
    def tipo(self, value):
        index = self.cbx_tipo.findText(value, QtCore.Qt.MatchFixedString)
        self.cbx_tipo.setCurrentIndex(index)
    
    @property
    def animal_1(self):
        return self.cbx_animal_1.currentText()
    
    @animal_1.setter
    def animal_1(self, value):
        self.cbx_animal_1.clear()
        self.cbx_animal_1.addItem('')
        for i in value:
            self.cbx_animal_1.addItem(i)
    
    @property
    def animal_2(self):
        return self.cbx_animal_2.currentText()
    
    @animal_2.setter
    def animal_2(self, value):
        self.cbx_animal_2.clear()
        self.cbx_animal_2.addItem('')
        for i in value:
            self.cbx_animal_2.addItem(i)
    
    @property
    def animal_3(self):
        return self.cbx_animal_3.currentText()
    
    @animal_3.setter
    def animal_3(self, value):
        self.cbx_animal_3.clear()
        self.cbx_animal_3.addItem('')
        for i in value:
            self.cbx_animal_3.addItem(i)
    
    @property
    def animal_4(self):
        return self.cbx_animal_4.currentText()
    
    @animal_4.setter
    def animal_4(self, value):
        self.cbx_animal_4.clear()
        self.cbx_animal_4.addItem('')
        for i in value:
            self.cbx_animal_4.addItem(i)

    # Functions

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def validar_datos(self):
        msg = 'El atributo {} es obligatorio.'
        codigo = self.codigo
        nombre = self.nombre
        publico = self.publico
        tipo = self.tipo
        animal1 = self.animal_1
        animal2 = self.animal_2
        animal3 = self.animal_3
        animal4 = self.animal_4
        duracion = self.duracion

        if codigo == '':
            raise Exception(msg.format('código'))

        if not codigo.isdigit():
            raise Exception('El código solo puede tener numeros')

        if nombre == '':
            raise Exception(msg.format('nombre'))

        if not nombre.replace(' ', '').isalpha():
            raise Exception('El nombre solo puede tener letras')

        if publico == '':
            raise Exception(msg.format('público'))

        if tipo == '':
            raise Exception(msg.format('tipo'))

        if animal1 == '' and animal2 == '' and animal3 == '' and animal4 == '':
            raise Exception('Debe seleccionar al menos un animal')

        if duracion == '0':
            raise Exception('La duracion del espectáculo no puede ser 0')

    def restablecer_datos(self):
        self.codigo = ''
        self.nombre = ''
        self.inicio = QTime(0, 0)
        self.duracion = 0
        self.publico = ''
        self.tipo = ''
        self.animal_1 = ''
        self.animal_2 = ''
        self.animal_3 = ''
        self.animal_4 = ''

    def especificar_animal_1(self, value):  # OK
        index = self.cbx_animal_1.findText(value, QtCore.Qt.MatchFixedString)
        self.cbx_animal_1.setCurrentIndex(index)

    def especificar_animal_2(self, value):  # OK
        index = self.cbx_animal_2.findText(value, QtCore.Qt.MatchFixedString)
        self.cbx_animal_2.setCurrentIndex(index)

    def especificar_animal_3(self, value):  # OK
        index = self.cbx_animal_3.findText(value, QtCore.Qt.MatchFixedString)
        self.cbx_animal_3.setCurrentIndex(index)

    def especificar_animal_4(self, value):  # OK
        index = self.cbx_animal_4.findText(value, QtCore.Qt.MatchFixedString)
        self.cbx_animal_4.setCurrentIndex(index)

    def vaciar_tabla(self):
        while self.tabla_espectaculos.rowCount() > 0:
            self.tabla_espectaculos.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto):
        self.tabla_espectaculos.setItem(fila, columna, QTableWidgetItem(texto))














