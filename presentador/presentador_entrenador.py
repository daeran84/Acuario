from vista.entrenador import VentanaEntrenador
from modelo.entrenador import Entrenador
from PyQt5.QtCore import QDate
from datetime import date


class PresentadorEntrenador:

    def __init__(self, repo):
        self.__vista = VentanaEntrenador(self)
        self.__repositorio = repo

    # Window main functions

    def iniciar(self):
        self.__vista.setWindowTitle('Entrenadores')
        self.cargar_datos()
        self.__vista.show()

    def cerrar(self):
        self.__vista.close()

    # Functions for list & view interactions

    def cargar_datos(self):
        try:
            self.__vista.vaciar_tabla()
            for entrenadores in self.__repositorio.lista_entrenadores:
                i = self.__vista.tabla_entrenadores.rowCount()
                self.__vista.tabla_entrenadores.insertRow(i)
                self.__vista.agregar_elemento_tabla(i, 0, entrenadores.nombre_apellidos)
                self.__vista.agregar_elemento_tabla(i, 1, entrenadores.nombre_artistico)
                self.__vista.agregar_elemento_tabla(i, 2, entrenadores.ci)
                self.__vista.agregar_elemento_tabla(i, 3, str(entrenadores.edad))
                self.__vista.agregar_elemento_tabla(i, 4, entrenadores.sexo)
                self.__vista.agregar_elemento_tabla(i, 5, str(entrenadores.fecha_nacimiento))
                self.__vista.agregar_elemento_tabla(i, 6, str(entrenadores.anios_experiencia))
                self.__vista.tabla_entrenadores.resizeColumnsToContents()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def insertar_entrenador(self):
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
            self.__repositorio.insertar_entrenador(entrenador)
            self.cargar_datos()
            self.__vista.restablecer_datos()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def actualizar_entrenador(self):
        try:
            ind = self.__vista.tabla_entrenadores.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar un registro para actualizarlo')
            ci_ant = self.__vista.tabla_entrenadores.item(ind, 2).text()
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
            self.__repositorio.actualizar_entrenador(ci_ant, entrenador)
            self.cargar_datos()
            self.__vista.restablecer_datos()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def eliminar_entrenador(self):
        try:
            ind = self.__vista.tabla_entrenadores.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar un registro para eliminarlo')
            animales = self.__repositorio.animales_del_entrenador(self.__vista.tabla_entrenadores.item(ind, 0).text())
            ci = self.__vista.tabla_entrenadores.item(ind, 2).text()
            self.__repositorio.eliminar_entrenador(ci)
            self.cargar_datos()
            self.__vista.restablecer_datos()
            if len(animales) == 1:
                self.__vista.mostrar_info(f'El animale acuático {animales[0]} ya no tiene entrenador, debe asignarle uno para que pueda participar en un espectáculo')
            if len(animales) > 1:
                animales_str = f' y {animales[-1]}'
                for i in range(len(animales)-1):
                    animales_str = f', {animales[i]}' + animales_str
                    animales.pop()
                self.__vista.mostrar_info(f"Los animales acuáticos {animales_str.strip(',').strip()} ya no tienen entrenador, debe asignarles uno para que puedan participar en un espectáculo")

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def llenar_formulario_x_tabla(self):  # OK
        try:
            ind = self.__vista.tabla_entrenadores.currentRow()
            if ind != -1:
                nombre = self.__vista.tabla_entrenadores.item(ind, 0).text()
                nombre_art = self.__vista.tabla_entrenadores.item(ind, 1).text()
                ci = self.__vista.tabla_entrenadores.item(ind, 2).text()
                edad = self.__vista.tabla_entrenadores.item(ind, 3).text()
                sexo = self.__vista.tabla_entrenadores.item(ind, 4).text()
                nac = self.__vista.tabla_entrenadores.item(ind, 5).text().split('-')
                nacimiento = QDate(int(nac[0]), int(nac[1]), int(nac[2]))
                experiencia = self.__vista.tabla_entrenadores.item(ind, 6).text()

                self.__vista.nombre_apellidos = nombre
                self.__vista.nombre_artistico = nombre_art
                self.__vista.ci = ci
                self.__vista.edad = int(edad)
                self.__vista.sexo = sexo
                self.__vista.fecha_nacimiento = nacimiento
                self.__vista.anios_experiencia = int(experiencia)

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def age(self, fecha):
        fecha = date(fecha.getDate()[0], fecha.getDate()[1], fecha.getDate()[2])
        today = date.today()
        try:
            birthday = fecha.replace(year=today.year)
        except ValueError:  # raised when birth date is February 29 and the current year is not a leap year
            birthday = fecha.replace(year=today.year, month=fecha.month + 1, day=1)
        if birthday > today:
            return today.year - fecha.year - 1
        else:
            return today.year - fecha.year






















