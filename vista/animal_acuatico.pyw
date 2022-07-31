from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5 import uic


class VentanaAnimalAcuatico(QDialog):

    def __init__(self, controlador):
        self.__controlador = controlador
        QDialog.__init__(self)
        uic.loadUi('vista/ui/animal_acuatico.ui', self)

        # Auxiliary window call & buttons configuration

        self.btn_cerrar.clicked.connect(self.close)
        # self.btn_administrar_entrenadores.clicked.connect(self.__controlador.admin_entrenadores)
    
    #  PROPS of field values
    
    @property
    def id(self):
        return self.anim_id.text().strip()

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
    
    """@property
    def comboBox_anim_familia(self):
        return self.comboBox_anim_familia.text()
    
    @comboBox_anim_familia.setter
    def comboBox_anim_familia(self, value):
        pass
    
    @property
    def comboBox_anim_habitat(self):
        return self.comboBox_anim_habitat.text()
    
    @comboBox_anim_habitat.setter
    def comboBox_anim_habitat(self, value):
        pass"""

    """@property
    def edad(self):
        return self.anim_edad.text().strip()

    @edad.setter
    def edad(self, value):
        self.anim_edad.setValue(value)"""
    
    """@property
    def comboBox_anim_categoria(self):
        return self.comboBox_anim_categoria.text()
    
    @comboBox_anim_categoria.setter
    def comboBox_anim_categoria(self, value):
        pass"""
    
    """@property
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
            self.check_cautiverio.setChecked(False)"""

    
    # Validation & mandatory field check

