from vista.animal_acuatico import VentanaAnimalAcuatico
from modelo.animal_acuatico import AnimalAquatico
from PyQt5.QtCore import QDate
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

    def last_id(self):
        print(1)
        return 1

    def cargar_datos(self):  # OK
        try:
            self.__vista.vaciar_tabla()
            for anim in self.__repositorio.especie_acuatica():
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

    def insertar_animal_acuatico(self):
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
                inicio = date(fecha.getDate()[0], fecha.getDate()[1], fecha.getDate()[2])
                entr = self.__vista.entr_ci
            animal = AnimalAquatico(id, nombre, nombre_c, familia, habitat, edad, categoria, cautiverio, espectaculo, inicio, entr)
            self.__repositorio.insertar_especie_acuatica(animal)
            self.cargar_datos()
            self.__vista.restablecer_datos()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def actualizar_animal_acuatico(self):
        pass

    def eliminar_animal_acuatico(self):
        pass

    def llenar_formulario_x_tabla(self):
        pass

