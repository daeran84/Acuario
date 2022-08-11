from vista.animal_acuatico import VentanaAnimalAcuatico
from modelo.animal_acuatico import AnimalAquatico
from controlador.controlador_entrenador import ControladorEntrenador
from datetime import date


class ControladorAnimalAcuatico:

    def __init__(self, repo):
        self.__vista = VentanaAnimalAcuatico(self)
        self.__repositorio = repo
        self.cargar_datos_combobox()
        self.get_id()

    # Window main functions
    def iniciar(self):
        self.__vista.setWindowTitle('Animales Acuaticos')
        self.cargar_datos()
        self.__vista.show()

    def cerrar(self):
        self.__vista.close()

    # Windows calls functions

    def admin_entrenadores(self):
        pen = ControladorEntrenador(self.__repositorio)
        pen.iniciar()

    # Functions for list & view interactions

    def cargar_datos_combobox(self):
        nombres = []
        for entrenador in self.__repositorio.lista_entrenadores:
            nombres.append(entrenador.nombre_apellidos)
        self.__vista.combo_entr = nombres

    def datos_entrenador_x_combo(self):
        try:
            nombre_entr = self.__vista.combo_entr
            entrenador = self.__repositorio.entr_x_nombre(nombre_entr)
            self.__vista.entr_nombre = entrenador.nombre_apellidos
            self.__vista.entr_nomb_art = entrenador.nombre_artistico
            self.__vista.entr_ci = entrenador.ci
            self.__vista.entr_edad = entrenador.edad
            self.__vista.entr_sexo = entrenador.sexo
            self.__vista.entr_nac = str(entrenador.fecha_nacimiento)
            self.__vista.entr_exp = entrenador.anios_experiencia

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def nombres_entrenadores(self):
        nombres = []
        for entrenador in self.__repositorio.lista_entrenadores:
            nombres.append(entrenador.nombre_apellidos)
        return nombres

    def get_id(self):  # mover a Repositorio
        id = self.__repositorio.last_id() + 1
        self.__vista.id = str(id)

    def cargar_datos(self):
        try:
            self.__vista.vaciar_tabla()
            for anim in self.__repositorio.animal_acuatico():
                i = self.__vista.tabla_animal_acuatico.rowCount()
                self.__vista.tabla_animal_acuatico.insertRow(i)
                self.__vista.agregar_elemento_tabla(i, 0, str(anim.id))
                self.__vista.agregar_elemento_tabla(i, 1, anim.nombre)
                self.__vista.agregar_elemento_tabla(i, 2, anim.nombre_cientifico)
                self.__vista.agregar_elemento_tabla(i, 3, anim.familia)
                self.__vista.agregar_elemento_tabla(i, 4, anim.habitat_natural)
                self.__vista.agregar_elemento_tabla(i, 5, anim.reproducido_en_cautiverio)
                self.__vista.agregar_elemento_tabla(i, 6, str(anim.edad))
                self.__vista.agregar_elemento_tabla(i, 7, anim.categoria)
                self.__vista.agregar_elemento_tabla(i, 8, anim.espectaculo)
                self.__vista.agregar_elemento_tabla(i, 9, str(anim.fecha_inicio))
                self.__vista.agregar_elemento_tabla(i, 10, anim.nombre_entrenador)
                self.__vista.tabla_animal_acuatico.resizeColumnsToContents()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def insertar_animal_acuatico(self):
        try:
            self.__vista.validar_datos()
            id = int(self.__vista.id)
            nombre = self.__vista.nombre
            nombre_c = self.__vista.nombre_cientifico
            familia = self.__vista.anim_familia
            habitat = self.__vista.anim_habitat
            edad = int(self.__vista.edad)
            categoria = self.__vista.anim_categoria
            cautiverio = self.__vista.cautiverio
            espectaculo = self.__vista.espectaculo
            inicio = ''
            entr = ''
            if espectaculo == 'Si':
                fecha = self.__vista.inicio_espect
                inicio = date(fecha.getDate()[0], fecha.getDate()[1], fecha.getDate()[2])
                entr = self.__vista.entr_nombre
            animal = AnimalAquatico(id, nombre, nombre_c, familia, habitat, edad, categoria, cautiverio, espectaculo, inicio, entr)
            self.__repositorio.insertar_especie(animal)
            self.cargar_datos()
            self.__vista.restablecer_datos()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def actualizar_animal_acuatico(self):
        try:
            ind = self.__vista.tabla_animal_acuatico.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar un registro para actualizarlo')
            id_ant = self.__vista.tabla_animal_acuatico.item(ind, 0).text()
            self.__vista.validar_datos()
            id = int(self.__vista.id)
            nombre = self.__vista.nombre
            nombre_c = self.__vista.nombre_cientifico
            familia = self.__vista.anim_familia
            habitat = self.__vista.anim_habitat
            edad = int(self.__vista.edad)
            categoria = self.__vista.anim_categoria
            cautiverio = self.__vista.cautiverio
            espectaculo = self.__vista.espectaculo
            inicio = ''
            entr = ''
            if espectaculo == 'Si':
                fecha = self.__vista.inicio_espect
                inicio = date(fecha.getDate()[0], fecha.getDate()[1], fecha.getDate()[2])
                entr = self.__vista.entr_nombre
            animal = AnimalAquatico(id, nombre, nombre_c, familia, habitat, edad, categoria, cautiverio, espectaculo, inicio, entr)
            self.__repositorio.actualizar_especie(id_ant, animal)
            self.cargar_datos()
            self.__vista.restablecer_datos()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def eliminar_animal_acuatico(self):
        try:
            ind = self.__vista.tabla_animal_acuatico.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar un registro para eliminarlo')
            id = self.__vista.tabla_animal_acuatico.item(ind, 0).text()
            self.__repositorio.eliminar_especie(id)
            self.cargar_datos()
            self.__vista.restablecer_datos()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def llenar_formulario_x_tabla(self):
        try:
            ind = self.__vista.tabla_animal_acuatico.currentRow()
            if ind != -1:
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
                if espect == 'Si':
                    inicio = inicio.split('-')
                    inicio = date(int(inicio[0]), int(inicio[1]), int(inicio[2]))
                nombre_entr = self.__vista.tabla_animal_acuatico.item(ind, 10).text()

                self.__vista.id = id_esp
                self.__vista.nombre = nombre
                self.__vista.nombre_cientifico = nombre_c
                self.__vista.anim_familia = familia
                self.__vista.anim_habitat = habitat
                self.__vista.cautiverio = caut
                self.__vista.edad = int(edad)
                self.__vista.anim_categoria = categ
                self.__vista.espectaculo = espect
                self.__vista.frames_enabled(False)
                if espect == 'Si':
                    self.__vista.espectaculo = 'Si'
                    self.__vista.inicio_espect = inicio
                    self.__vista.especificar_entr_cbx(nombre_entr)
                    self.datos_entrenador_x_combo()
                    self.__vista.frames_enabled(True)

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

