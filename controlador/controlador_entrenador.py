from vista.entrenador import VentanaEntrenador
from modelo.entrenador import Entrenador
from PyQt5.QtCore import QDate
from datetime import date


class ControladorEntrenador:

    def __init__(self, repo):
        self.__vista = VentanaEntrenador(self)
        self.__repositorio = repo

        """entr_ini = Entrenador('84101118140', 'Camilo Rioseco Rodriguez', 'Camilo', 37, 'M', '1984-11-10', 0)
        self.__repositorio.incertar_entrenador(entr_ini)
        print(self.__repositorio.lista_entrenadores)"""

    # Window main functions

    def iniciar(self):
        self.__vista.setWindowTitle('Entrenadores')
        self.cargar_datos()
        self.__vista.show()

    def cerrar(self):
        self.__vista.close()

    # Functions for list management

    def cargar_datos(self):
        self.__vista.vaciar_tabla()
        for entrenadores in self.__repositorio.lista_entrenadores:
            i = self.__vista.tabla_entrenadores.rowCount()
            self.__vista.tabla_entrenadores.rowCount(i)
            self.__vista.agregar_elemento_tabla(i, 0, entrenadores.nombre)


        pass

    def insertar_entrenador(self):  # OK
        try:
            self.__vista.validar_datos()
            ci = self.__vista.ci
            nombre = self.__vista.nombre_apellidos
            nombre_art = self.__vista.nombre_artistico
            edad = self.__vista.edad
            sexo = self.__vista.sexo
            nac = self.__vista.fecha_nacimiento
            nacimiento = date(nac.getDate()[0], nac.getDate()[1], nac.getDate()[2])
            experiencia = self.__vista.anios_experiencia
            entrenador = Entrenador(ci, nombre, nombre_art, edad, sexo, nacimiento, experiencia)
            self.__repositorio.incertar_entrenador(entrenador)
            self.cargar_datos()
            self.__vista.restablecer_datos()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def actualizar_entrenador(self):
        print('actualizar')

    def eliminar_entrenador(self):
        print('eliminar')

    def llenar_formulario_x_tabla(self):
        print('tabla')