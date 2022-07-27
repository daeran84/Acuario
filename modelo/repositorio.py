class Repositorio:
    def __init__(self):
        self.__lista_especies = []
        self.__lista_espectaculos = []
        self.__lista_entrenadores = []

    # PROPS of list values

    @property
    def lista_especies(self):
        return self.__lista_especies

    @lista_especies.setter
    def lista_especies(self, value):
        self.__lista_especies = value

    @property
    def lista_espectaculos(self):
        return self.__lista_espectaculos

    @lista_espectaculos.setter
    def lista_espectaculos(self, value):
        self.__lista_espectaculos = value

    @property
    def lista_entrenadores(self):
        return self.__lista_entrenadores

    @lista_entrenadores.setter
    def lista_entrenadores(self, value):
        self.__lista_entrenadores = value

    # Functions for lista_especies

    def incertar_animal_acuatico(self):
        pass

    def actualizar_animal_acuatico(self):
        pass

    def eliminar_animal_acuatico(self):
        pass

    # Functions for lista_espectaculos


    def incertar_espectaculo(self):
        pass

    def actualizar_espectaculo(self):
        pass

    def eliminar_espectaculo(self):
        pass

    # Functions for Lista_entrenadores

    def incertar_entrenador(self):
        pass

    def actualizar_entrenador(self):
        pass

    def eliminar_entrenador(self):
        pass