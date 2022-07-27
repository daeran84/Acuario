class Repositorio:
    def __init__(self):
        self.__lista_especies = []
        self.__lista_espectaculos = []
        self.__lista_entrenadores = []

    @property
    def lista_especies(self):
        return self.__lista_especies

    @property
    def lista_espectaculos(self):
        return self.__lista_espectaculos

    @property
    def lista_entrenadores(self):
        return self.__lista_entrenadores