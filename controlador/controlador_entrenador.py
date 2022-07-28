from vista.entrenador import VentanaEntrenador
from modelo.entrenador import Entrenador
from PyQt5.QtCore import QDate
from datetime import date


class ControladorEntrenador:

    def __init__(self, repo):
        self.vista = VentanaEntrenador(self)
        self.repositorio = repo

    # Window main functions

    def iniciar(self):
        self.vista.setWindowTitle('Entrenadores')
        self.vista.show()

    def cerrar(self):
        self.vista.close()

    # Functions for list management

    def cargar_datos(self):
        print('cargando datos')

    def insertar_entrenador(self):
        try:
            self.vista.validar_datos()
            ci = self.vista.ci
            nombre = self.vista.nombre_apellidos
            nombre_art = self.vista.nombre_artistico
            edad = self.vista.edad
            sexo = self.vista.sexo
            nac = self.vista.fecha_nacimiento
            nacimiento = date(nac.getDate()[0], nac.getDate()[1], nac.getDate()[2])
            experiencia = self.vista.anios_experiencia
            entrenador = Entrenador(ci, nombre, nombre_art, edad, sexo, nacimiento, experiencia)
            self.repositorio.incertar_entrenador(entrenador)

        except Exception as e:
            self.vista.mostrar_error(e.args[0])


    def actualizar_entrenador(self):
        print('actualizar')

    def eliminar_entrenador(self):
        print('eliminar')

    def llenar_formulario_x_tabla(self):
        print('tabla')