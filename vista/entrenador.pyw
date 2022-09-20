import datetime
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5 import uic


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
        self.btn_nuevo_reg.clicked.connect(self.restablecer_datos)
        self.tabla_entrenadores.itemClicked.connect(self.__controlador.llenar_formulario_x_tabla)
        self.tabla_entrenadores.setColumnCount(7)
        self.tabla_entrenadores.setHorizontalHeaderLabels(['Nombre', 'Nombre Artistico', 'CI', 'Edad', 'Sexo', 'Fecha de nacimiento', 'Años de experiencia'])
        self.tabla_entrenadores.horizontalHeaderItem(3).setToolTip('Carnet de Identidad')
        self.tabla_entrenadores.resizeColumnsToContents()

    # PROPS

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
        return self.valor_edad.value()

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
        return self.valor_experiencia.value()

    @anios_experiencia.setter
    def anios_experiencia(self, value):
        self.valor_experiencia.setValue(value)

    # Functions

    def validar_datos(self):
        msg = 'El atributo {} es obligatorio.'
        c_i = self.ci
        na = self.nombre_apellidos
        nar = self.nombre_artistico
        edad = self.edad
        exp = self.anios_experiencia

        if len(na) == 0:
            raise Exception(msg.format('nombre'))
        if not na.replace(' ', '').isalpha():
            raise Exception('El nombre solo puede tener letras')
        if len(nar) == 0:
            raise Exception(msg.format('nombre artístico'))
        if not nar.replace(' ', '').isalpha():
            raise Exception('El nombre artístico solo puede tener letras')
        if len(c_i) == 0:
            raise Exception(msg.format('carnet de identidad'))
        if not c_i.isdigit():
            raise Exception('El carnet de identidad solo puede tener dígitos')
        if len(c_i) != 11:
            raise Exception('El carnet de identidad debe tener 11 dígitos')
        if edad != self.__controlador.age(self.fecha_nacimiento):
            raise Exception('la edad no concuerda con la fecha de nacimiento')
        if exp > (edad - 18):
            raise Exception('La experiencia debe ser menor que la diferencia entre la edad  y la edad mínima laborable')

    def restablecer_datos(self):
        self.ci = ''
        self.nombre_apellidos = ''
        self.nombre_artistico = ''
        self.edad = 20
        self.fecha_nacimiento = datetime.date(int(1977), int(1), int(1))
        self.anios_experiencia = 0
        self.sexo = 'M'

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def mostrar_info(self, msg):
        QMessageBox.information(self, 'Información', msg)

    def vaciar_tabla(self):  # OK
        while self.tabla_entrenadores.rowCount() > 0:
            self.tabla_entrenadores.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto):  # OK
        self.tabla_entrenadores.setItem(fila, columna, QTableWidgetItem(texto))





