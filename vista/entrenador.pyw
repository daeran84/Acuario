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
        self.btn_incertar.clicked.connect(self.__controlador.insertar_entrenador)
        self.btn_actualizar.clicked.connect(self.__controlador.actualizar_entrenador)
        self.btn_eliminar.clicked.connect(self.__controlador.eliminar_entrenador)
        self.tabla_entrenadores.itemClicked.connect(self.__controlador.llenar_formulario_x_tabla)
        self.tabla_entrenadores.setColumnCount(7)
        self.tabla_entrenadores.setHorizontalHeaderLabels(['Nombre', 'Nombre Artistico', 'CI', 'Edad', 'Sexo', 'Fecha de nacimiento', 'Años de experiencia'])
        self.tabla_entrenadores.horizontalHeaderItem(3).setToolTip('Carnet de Identidad')
        self.tabla_entrenadores.resizeColumnsToContents()

    # PROPS of fields working

    @property
    def ci(self):
        return self.valor_ci.text().strip()

    @ci.setter
    def ci(self, value):
        self.valor_ci.setText(value)

    @property
    def nombre_apellidos(self):
        return self.valor_nombre_apellidos.text().strip()

    @nombre_apellidos.setter
    def nombre_apellidos(self, value):
        self.valor_nombre_apellidos.setText(value)

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
        self.valor_edad.setValue(value)

    @property
    def sexo(self):
        if self.check_masculino.isChecked():
            sex = 'M'
        else:
            sex = 'F'
        return sex

    @sexo.setter
    def sexo(self, value):
        if value == 'M':
            self.check_masculino.setChecked(True)
        else:
            self.check_femenino.setChecked(True)

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
        self.valor_experiencia.setValue(value)

    def validar_datos(self):
        msg = 'El atributo {} es obligatorio.'
        c_i = self.ci
        na = self.nombre_apellidos
        nar = self.nombre_artistico

        if len(na) == 0:
            raise Exception(msg.format('nombre completo'))
        if len(nar) == 0:
            raise Exception(msg.format('nombre artistico'))
        if not nar.isalpha():
            raise Exception('El nombre artistico solo puede tener letras')
        if len(c_i) == 0:
            raise Exception(msg.format('carnet de identidad'))
        if not c_i.isdigit():
            raise Exception('El carnet de identidad solo puede tener digitos')
        if len(c_i) != 11:
            raise Exception('El carnet de identidad debe tener 11 digitos')

    def restablecer_datos(self):
        self.ci = ''
        self.nombre_apellidos = ''
        self.nombre_artistico = ''
        self.edad = 20
        self.fecha_nacimiento = datetime.date(int(1965), int(1), int(1))
        self.anios_experiencia = 0
        self.sexo = 'M'

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def vaciar_tabla(self):  # OK
        while self.tabla_entrenadores.rowCount() > 0:
            self.tabla_entrenadores.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto):  # OK
        self.tabla_entrenadores.setItem(fila, columna, QTableWidgetItem(texto))





