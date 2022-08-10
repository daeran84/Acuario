from vista.animales_entrenador import VentanaAnimalesEntrenador


class ControladorAnimalesEntrenador:

    def __init__(self, repo):
        self.__vista = VentanaAnimalesEntrenador(self)
        self.__repositorio = repo
        self.cargar_datos_combobox()

    # Window main functions

    def iniciar(self):
        self.__vista.setWindowTitle('Animales por Entrenador')
        self.__vista.show()

    def cerrar(self):
        self.__vista.close()

    # Functions for list management

    def cargar_datos_combobox(self):
        nombres = []
        for entrenador in self.__repositorio.lista_entrenadores:
            nombres.append(entrenador.nombre_apellidos)
        self.__vista.combo_entr = nombres

    def nombres_entrenadores(self):
        nombres = []
        for entrenador in self.__repositorio.lista_entrenadores:
            nombres.append(entrenador.nombre_apellidos)
        return nombres

    def datos_animales(self, entr):
        animales = []
        for anim in self.__repositorio.animal_acuatico():
            if anim.espectaculo and anim.nombre_entrenador == entr:
                animales.append(anim)
        return animales

    def cargar_datos(self):  # OK
        try:
            self.__vista.vaciar_tabla()
            animales = self.datos_animales(self.__vista.combo_entr)
            for anim in animales:
                i = self.__vista.tabla_animales_entrenador.rowCount()
                self.__vista.tabla_animales_entrenador.insertRow(i)
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
                self.__vista.tabla_animales_entrenador.resizeColumnsToContents()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])
