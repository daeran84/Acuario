from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5 import uic


class VentanaAnimalesEntrenador(QDialog):

    def __init__(self, controlador):
        self.__controlador = controlador
        QDialog.__init__(self)
        uic.loadUi('vista/ui/animales_entrenador.ui', self)

        # Buttons & table data configuration

        self.btn_cerrar.clicked.connect(self.close)
        self.cbx_selec_entr.activated[str].connect(self.__controlador.cargar_datos)
        self.tabla_animales_entrenador.setColumnCount(11)
        self.tabla_animales_entrenador.setHorizontalHeaderLabels(['ID', 'Nombre', 'Nombre cientifico', 'Familia', 'Habitat natural', 'Reproducido en cautiverio', 'Edad', 'Categoria', 'Participa en Espectaculos', 'Fecha de inicio', 'Entrenador'])
        self.tabla_animales_entrenador.resizeColumnsToContents()

    # PROPS

    @property
    def combo_entr(self):
        return self.cbx_selec_entr.currentText()

    @combo_entr.setter
    def combo_entr(self, value):
        self.cbx_selec_entr.clear()
        self.cbx_selec_entr.addItem('')
        for i in value:
            self.cbx_selec_entr.addItem(i)

    # Functions

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def vaciar_tabla(self):  # OK
        while self.tabla_animales_entrenador.rowCount() > 0:
            self.tabla_animales_entrenador.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto):  # OK
        self.tabla_animales_entrenador.setItem(fila, columna, QTableWidgetItem(texto))
