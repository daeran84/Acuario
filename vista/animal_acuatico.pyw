from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5 import QtCore
import datetime
from PyQt5 import uic


class VentanaAnimalAcuatico(QDialog):

    def __init__(self, controlador):
        self.__controlador = controlador
        QDialog.__init__(self)
        uic.loadUi('vista/ui/animal_acuatico.ui', self)

        # Auxiliary windows call, table & buttons configuration

        self.btn_cerrar.clicked.connect(self.close)
        self.btn_adm_entrenador.clicked.connect(self.__controlador.admin_entrenadores)
        self.btn_insertar.clicked.connect(self.__controlador.insertar_animal_acuatico)
        self.btn_actualizar.clicked.connect(self.__controlador.actualizar_animal_acuatico)
        self.btn_eliminar.clicked.connect(self.__controlador.eliminar_animal_acuatico)
        self.btn_nuevo_reg.clicked.connect(self.restablecer_datos)
        self.tabla_animal_acuatico.itemClicked.connect(self.__controlador.llenar_formulario_x_tabla)
        self.tabla_animal_acuatico.setColumnCount(11)
        self.tabla_animal_acuatico.setHorizontalHeaderLabels(['ID', 'Nombre', 'Nombre cientifico', 'Familia', 'Habitat natural', 'Reproducido en cautiverio', 'Edad', 'Categoria', 'Participa en Espectaculos', 'Fecha de inicio', 'Entrenador'])
        self.tabla_animal_acuatico.resizeColumnsToContents()
        self.btn_act_combobox.clicked.connect(self.__controlador.cargar_datos_combobox)
        self.cbx_selec_entr.activated[str].connect(self.__controlador.datos_entrenador_x_combo)

    #  PROPS of field values

    @property
    def combo_entr(self):
        return self.cbx_selec_entr.currentText()

    @combo_entr.setter
    def combo_entr(self, value):
        self.cbx_selec_entr.clear()
        self.cbx_selec_entr.addItem('')
        for i in value:
            self.cbx_selec_entr.addItem(i)

    @property
    def id(self):
        return self.anim_id.text()

    @id.setter
    def id(self, value):
        self.anim_id.setText(value)

    @property
    def nombre(self):
        return self.anim_nombre.text().strip()

    @nombre.setter
    def nombre(self, value):
        self.anim_nombre.setText(value)
    
    @property
    def nombre_cientifico(self):
        return self.anim_nombre_cientifico.text().strip()

    @nombre_cientifico.setter
    def nombre_cientifico(self, value):
        self.anim_nombre_cientifico.setText(value)
    
    @property
    def anim_familia(self):
        return self.comboBox_anim_familia.currentText()

    @anim_familia.setter
    def anim_familia(self, value):
        index = self.comboBox_anim_familia.findText(value, QtCore.Qt.MatchFixedString)
        self.comboBox_anim_familia.setCurrentIndex(index)
    
    @property
    def anim_habitat(self):
        return self.comboBox_anim_habitat.currentText()

    @anim_habitat.setter
    def anim_habitat(self, value):
        index = self.comboBox_anim_habitat.findText(value, QtCore.Qt.MatchFixedString)
        self.comboBox_anim_habitat.setCurrentIndex(index)

    @property
    def edad(self):
        return self.anim_edad.value()

    @edad.setter
    def edad(self, value):
        self.anim_edad.setValue(value)

    @property
    def anim_categoria(self):
        return self.comboBox_anim_categoria.currentText()
    
    @anim_categoria.setter
    def anim_categoria(self, value):
        index = self.comboBox_anim_categoria.findText(value, QtCore.Qt.MatchFixedString)
        self.comboBox_anim_categoria.setCurrentIndex(index)
    
    @property
    def cautiverio(self):
        if self.check_cautiverio.isChecked():
            cautiv = 'Si'
        else:
            cautiv = 'No'
        return cautiv

    @cautiverio.setter
    def cautiverio(self, value):
        if value == 'Si':
            self.check_cautiverio.setChecked(True)
        else:
            self.check_cautiverio.setChecked(False)
    
    @property
    def espectaculo(self):
        if self.check_espectaculos.isChecked():
            espect = 'Si'
        else:
            espect = 'No'
        return espect
            
    @espectaculo.setter
    def espectaculo(self, value):
        if value == 'Si':
            self.check_espectaculos.setChecked(True)
        else:
            self.check_espectaculos.setChecked(False)
    
    @property
    def inicio_espect(self):
        return self.valor_inicio.date()
    
    @inicio_espect.setter
    def inicio_espect(self, value):
        self.valor_inicio.setDate(value)

    #  PROPS trainer values

    @property
    def entr_nombre(self):
        return self.entrenador_nombre_apellidos.text()
    
    @entr_nombre.setter
    def entr_nombre(self, value):
        self.entrenador_nombre_apellidos.setText(value)
    
    @property
    def entr_nomb_art(self):
        return self.entrenador_nombre_artistico.text()
    
    @entr_nomb_art.setter
    def entr_nomb_art(self, value):
        self.entrenador_nombre_artistico.setText(value)

    @property
    def entr_ci(self):
        return self.entrenador_carnet_identidad.text()

    @entr_ci.setter
    def entr_ci(self, value):
        self.entrenador_carnet_identidad.setText(value)

    @property
    def entr_edad(self):
        return self.entrenador_edad.text()

    @entr_edad.setter
    def entr_edad(self, value):
        self.entrenador_edad.setText(value)

    @property
    def entr_sexo(self):
        return self.entrenador_sexo.text()
    
    @entr_sexo.setter
    def entr_sexo(self, value):
        self.entrenador_sexo.setText(value)

    @property
    def entr_nac(self):
        return self.entrenador_nacimiento.text()
    
    @entr_nac.setter
    def entr_nac(self, value):
        self.entrenador_nacimiento.setText(value)

    @property
    def entr_exp(self):
        return self.entrenador_experiencia.text()

    @entr_exp.setter
    def entr_exp(self, value):
        self.entrenador_experiencia.setText(value)

    # Functions

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def validar_datos(self):
        msg = 'El atributo {} es obligatorio.'
        nombre = self.nombre
        nombre_c = self.nombre_cientifico
        familia = self.anim_familia
        categoria = self.anim_categoria
        espect = self.espectaculo
        entrenador = self.combo_entr

        if len(nombre) == 0:
            raise Exception(msg.format('nombre'))
        if not nombre.replace(' ', '').isalpha():
            raise Exception('El nombre solo puede tener letras')

        if len(nombre_c) == 0:
            raise Exception(msg.format('nombre científico'))
        if not nombre_c.replace(' ', '').isalpha():
            raise Exception('El nombre científico solo puede tener letras')

        if familia == '':
            raise Exception(msg.format('familia'))

        if categoria == '':
            raise Exception(msg.format('categoría'))

        if espect == 'Si' and entrenador == '':
            raise Exception('Si participa en espectáculos debe seleccionar un entrenador')

    def restablecer_datos(self):
        self.__controlador.get_id()
        self.nombre = ''
        self.nombre_cientifico = ''
        self.anim_familia = ''
        self.anim_habitat = 'Mar'
        self.cautiverio = "No"
        self.edad = 0
        self.anim_categoria = ''
        self.frames_enabled(False)

    def frames_enabled(self, value):
        if value:
            self.frame_entr.setEnabled(True)
            self.frame_f_inicio.setEnabled(True)
        else:
            self.frame_entr.setEnabled(False)
            self.frame_f_inicio.setEnabled(False)
            self.espectaculo = 'No'
            self.inicio_espect = datetime.date(int(1965), int(1), int(1))
            self.cbx_selec_entr.setCurrentIndex(0)
            self.entr_nombre = ''
            self.entr_nomb_art = ''
            self.entr_ci = ''
            self.entr_edad = ''
            self.entr_sexo = ''
            self.entr_nac = ''
            self.entr_exp = ''

    def especificar_entr_cbx(self, value):
        index = self.cbx_selec_entr.findText(value, QtCore.Qt.MatchFixedString)
        self.cbx_selec_entr.setCurrentIndex(index)

    def vaciar_tabla(self):  # OK
        while self.tabla_animal_acuatico.rowCount() > 0:
            self.tabla_animal_acuatico.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto):
        self.tabla_animal_acuatico.setItem(fila, columna, QTableWidgetItem(texto))

