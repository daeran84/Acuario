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
    def anim_id(self):
        return self.anim_id.text().strip()
    
    @anim_id.setter
    def anim_id(self, value):
        
    

    # Validation & mandatory field check

