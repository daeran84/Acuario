from vista.animales_entrenador import VentanaAnimalesEntrenador


class ControladorAnimalesEntrenador:

    def __init__(self, repo):
        self.__vista = VentanaAnimalesEntrenador(self)
        self.__repositorio = repo

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