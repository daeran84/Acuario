from vista.espectaculo import VentanaEspectaculo
from modelo.espectaculo import Espectaculo
from PyQt5.QtCore import QDate
from datetime import date


class ControladorEspectaculo:

    def __init__(self, repo):
        self.__vista = VentanaEspectaculo(self)
        self.__repositorio = repo

    # Window main functions

    def iniciar(self):
        self.__vista.setWindowTitle('Espectaculos')
        self.cargar_datos()
        self.__vista.show()

    def cerrar(self):
        self.__vista.close()

    # Functions for list management

    def cargar_datos(self):
        try:
            pass

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def insertar_espectaculo(self):
        try:
            self.__vista.validar_datos()
            codigo = self.__vista.codigo
            nombre = self.__vista.nombre
            inicio = self.__vista.f_inicio
            duracion = self.__vista.duracion
            publico = self.__vista.publico
            espect = Espectaculo(codigo, nombre, inicio, duracion, publico)
            self.__repositorio.insertar_espectaculo(espect)
            self.cargar_datos()
            self.__vista.restablecer_datos()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def actualizar_espectaculo(self):
        try:
            pass

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def eliminar_espectaculo(self):
        try:
            pass

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def llenar_formulario_x_tabla(self):
        try:
            pass

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])