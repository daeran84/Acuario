class EspecieAcuatica:

    def __init__(self,identificador, nombre_cientifico, familia, habitat_natural):
        self.__identificador = identificador
        self.__nombre_cientifico = nombre_cientifico
        self.__familia = familia
        self.__habitat_natural = habitat_natural

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, value):
        self.__identificador = value


    @property
    def nombre_cientifico(self):
        return self.__nombre_cientifico

    @nombre_cientifico.setter
    def nombre_cientifico(self, value):
        self.__nombre_cientifico = value


    @property
    def familia(self):
        return self.__familia

    @familia.setter
    def familia(self, value):
        self.__familia = value


    @property
    def habitat_natural(self):
        return self.__habitat_natural

    @habitat_natural.setter
    def habitat_natural(self, value):
        self.__habitat_natural = value
    