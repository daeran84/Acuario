from vista.animal_acuatico import VentanaAnimalAcuatico
from modelo.animal_acuatico import AnimalAquatico
from modelo.entrenador import Entrenador
from PyQt5.QtCore import QDate
from PyQt5 import QtCore
from datetime import date


class ControladorAnimalAcuatico:

    def __init__(self, repo):
        self.__vista = VentanaAnimalAcuatico(self)
        self.__repositorio = repo

    # Window main functions
    def iniciar(self):
        self.__vista.setWindowTitle('Animales Acuaticos')
        self.__vista.show()

    def cerrar(self):
        self.__vista.close()

    # Windows calls functions

#    def admin_entrenadores(self):
#        pen = ControladorEntrenador(self.__repositorio)
#       pen.iniciar()

    # Functions for list management

    def cargar_combobox(self):
        for entrenador in self.__repositorio.lista_entrenadores:
            self.__vista.cbx_selec_entr.addItem(entrenador.nombre_apellidos)



    def last_id(self):
        print(1)
        return 1

    def cargar_datos(self):  # OK
        try:
            self.__vista.vaciar_tabla()
            for anim in self.__repositorio.animal_acuatico():
                i = self.__vista.tabla_animal_acuatico.rowCount()
                self.__vista.tabla_animal_acuatico.insertRow(i)
                self.__vista.agregar_elemento_tabla(i, 0, anim.id)
                self.__vista.agregar_elemento_tabla(i, 1, anim.nombre)
                self.__vista.agregar_elemento_tabla(i, 2, anim.nombre_cientifico)
                self.__vista.agregar_elemento_tabla(i, 3, anim.familia)
                self.__vista.agregar_elemento_tabla(i, 4, anim.habitat_natural)
                self.__vista.agregar_elemento_tabla(i, 5, anim.reproducido_en_cautiverio)
                self.__vista.agregar_elemento_tabla(i, 6, anim.edad)
                self.__vista.agregar_elemento_tabla(i, 7, anim.categoria)
                self.__vista.agregar_elemento_tabla(i, 8, anim.espectaculo)
                self.__vista.agregar_elemento_tabla(i, 9, anim.fecha_inicio)
                self.__vista.agregar_elemento_tabla(i, 10, anim.id_entrenador)
                self.__vista.tabla_animal_acuatico.resizeColumnsToContents()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def insertar_animal_acuatico(self):  # OK
        try:
            self.__vista.validar_datos()
            id = self.__vista.id
            nombre = self.__vista.nombre
            nombre_c = self.__vista.nombre_cientifico
            familia = self.__vista.anim_familia
            habitat = self.__vista.anim_habitat
            edad = self.__vista.edad
            categoria = self.__vista.anim_categoria
            cautiverio = self.__vista.cautiverio
            espectaculo = self.__vista.espectaculo
            inicio = ''
            entr = ''
            if espectaculo == 'Si':
                fecha = self.__vista.inicio_espect
                inicio = fecha.toString(QtCore.Qt.ISODate)
                entr = self.__vista.entr_ci
            animal = AnimalAquatico(id, nombre, nombre_c, familia, habitat, edad, categoria, cautiverio, espectaculo, inicio, entr)
            self.__repositorio.insertar_especie(animal)
            self.cargar_datos()
            self.__vista.restablecer_datos()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def actualizar_animal_acuatico(self):  # OK
        try:
            ind = self.__vista.tabla_animal_acuatico.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para actualizarla')
            id_ant = self.__vista.tabla_animal_acuatico.item(ind, 0).text()
            self.__vista.validar_datos()
            id = self.__vista.id
            nombre = self.__vista.nombre
            nombre_c = self.__vista.nombre_cientifico
            familia = self.__vista.anim_familia
            habitat = self.__vista.anim_habitat
            edad = self.__vista.edad
            categoria = self.__vista.anim_categoria
            cautiverio = self.__vista.cautiverio
            espectaculo = self.__vista.espectaculo
            inicio = ''
            entr = ''
            if espectaculo == 'Si':
                fecha = self.__vista.inicio_espect
                inicio = fecha.toString(QtCore.Qt.ISODate)
                entr = self.__vista.entr_ci
            animal = AnimalAquatico(id, nombre, nombre_c, familia, habitat, edad, categoria, cautiverio, espectaculo, inicio, entr)
            self.__repositorio.actualizar_especie(id_ant, animal)
            self.cargar_datos()
            self.__vista.restablecer_datos()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])




    def eliminar_animal_acuatico(self):  # ok
        try:
            ind = self.__vista.tabla_animal_acuatico.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para eliminarla')
            id = self.__vista.tabla_animal_acuatico.item(ind, 0).text()
            self.__repositorio.eliminar_especie(id)
            self.cargar_datos()
            self.__vista.restablecer_datos()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def llenar_formulario_x_tabla(self):  # OK
        try:
            # Obteniendo fila a mostrar
            ind = self.__vista.tabla_animal_acuatico.currentRow()
            if ind != -1:

                # Obteniendo datos de las columnas
                id_esp = self.__vista.tabla_animal_acuatico.item(ind, 0).text()
                nombre = self.__vista.tabla_animal_acuatico.item(ind, 1).text()
                nombre_c = self.__vista.tabla_animal_acuatico.item(ind, 2).text()
                familia = self.__vista.tabla_animal_acuatico.item(ind, 3).text()
                habitat = self.__vista.tabla_animal_acuatico.item(ind, 4).text()
                caut = self.__vista.tabla_animal_acuatico.item(ind, 5).text()
                edad = self.__vista.tabla_animal_acuatico.item(ind, 6).text()
                categ = self.__vista.tabla_animal_acuatico.item(ind, 7).text()
                espect = self.__vista.tabla_animal_acuatico.item(ind, 8).text()
                inicio = self.__vista.tabla_animal_acuatico.item(ind, 9).text()
                if inicio != '':
                    inicio = QDate(int(inicio[0]), int(inicio[1]), int(inicio[2]))
                id_entr = self.__vista.tabla_animal_acuatico.item(ind, 10).text()

                # Dando valores a los atributos
                self.__vista.id = int(id_esp)
                self.__vista.nombre = nombre
                self.__vista.nombre_cientifico = nombre_c
                self.__vista.anim_familia = familia
                self.__vista.anim_habitat = habitat
                self.__vista.cautiverio = False
                if caut == 'Si':
                    self.__vista.cautiverio = True
                self.__vista.edad = int(edad)
                self.__vista.anim_categoria = categ
                self.__vista.espectaculo = False
                if espect == 'Si':
                    self.__vista.espectaculo = True
                if inicio != '':
                    self.__vista.inicio_espect = inicio
                self.__vista.entr_ci = id_entr


        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

