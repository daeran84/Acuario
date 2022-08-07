from vista.espectaculo import VentanaEspectaculo
from modelo.espectaculo import Espectaculo
from PyQt5.QtCore import QTime
from datetime import date


class ControladorEspectaculo:

    def __init__(self, repo):
        self.__vista = VentanaEspectaculo(self)
        self.__repositorio = repo

    # Window main functions

    def iniciar(self):
        self.__vista.setWindowTitle('Espectáculos')
        self.cargar_datos()
        self.__vista.show()

    def cerrar(self):
        self.__vista.close()

    # Functions for list management

    def cargar_datos(self):  # OK
        try:
            self.__vista.vaciar_tabla()
            for espect in self.__repositorio.lista_espectaculos:
                i = self.__vista.tabla_espectaculos.rowCount()
                self.__vista.tabla_espectaculos.insertRow(i)
                self.__vista.agregar_elemento_tabla(i, 0, espect.codigo)
                self.__vista.agregar_elemento_tabla(i, 1, espect.nombre)
                self.__vista.agregar_elemento_tabla(i, 2, espect.hora_inicio)
                self.__vista.agregar_elemento_tabla(i, 3, str(espect.duracion))
                self.__vista.agregar_elemento_tabla(i, 4, espect.publico)
                self.__vista.tabla_espectaculos.resizeColumnsToContents()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def insertar_espectaculo(self):  # OK
        try:
            self.__vista.validar_datos()
            codigo = self.__vista.codigo
            nombre = self.__vista.nombre
            inicio = self.__vista.inicio
            duracion = int(self.__vista.duracion)
            publico = self.__vista.publico
            espect = Espectaculo(codigo, nombre, inicio, duracion, publico)
            self.__repositorio.insertar_espectaculo(espect)
            self.cargar_datos()
            self.__vista.restablecer_datos()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def actualizar_espectaculo(self):  # OK
        try:
            ind = self.__vista.tabla_espectaculos.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para actualizarla')
            cod = self.__vista.tabla_espectaculos.item(ind, 0).text()
            self.__vista.validar_datos()
            self.__vista.validar_datos()
            codigo = self.__vista.codigo
            nombre = self.__vista.nombre
            inicio = self.__vista.inicio
            duracion = int(self.__vista.duracion)
            publico = self.__vista.publico
            espect = Espectaculo(codigo, nombre, inicio, duracion, publico)
            self.__repositorio.actualizar_espectaculo(cod, espect)
            self.cargar_datos()
            self.__vista.restablecer_datos()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def eliminar_espectaculo(self):
        try:
            ind = self.__vista.tabla_espectaculos.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para actualizarla')
            codigo = self.__vista.tabla_espectaculos.item(ind, 0).text()
            self.__repositorio.eliminar_espectaculo(codigo)

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def llenar_formulario_x_tabla(self):  # OK
        try:
            ind = self.__vista.tabla_espectaculos.currentRow()
            if ind != -1:

                codigo = self.__vista.tabla_espectaculos.item(ind, 0).text()
                nombre = self.__vista.tabla_espectaculos.item(ind, 1).text()
                inicio = self.__vista.tabla_espectaculos.item(ind, 2).text()
                if inicio.split(' ')[1] == 'AM':
                    hora = QTime(int(inicio.split(' ')[0].split(":")[0]), int(inicio.split(' ')[0].split(":")[1]))
                else:
                    hora = QTime(int(inicio.split(' ')[0].split(":")[0]) + 12, int(inicio.split(' ')[0].split(":")[1]))
                duracion = self.__vista.tabla_espectaculos.item(ind, 3).text()
                publico = self.__vista.tabla_espectaculos.item(ind, 4).text()

                self.__vista.codigo = codigo
                self.__vista.nombre = nombre
                self.__vista.inicio = hora
                self.__vista.duracion = int(duracion)
                self.__vista.publico = publico

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])


















