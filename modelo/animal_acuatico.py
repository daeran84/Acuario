from especie_acuatica import EspecieAcuatica


class AnimalAquatico(EspecieAcuatica):

    def __init__(self, id, nombre_cientifico, familia, habitat_natural, nombre, reproducido_en_cautiverio, edad, categoria):
        EspecieAcuatica.__init__(self, id, nombre_cientifico, familia, habitat_natural)
        self.__nombre = nombre
        self.__reproducido_en_cautiverio = reproducido_en_cautiverio
        self.__edad = edad
        self.__categoria = categoria

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def reproducido_en_cautiverio(self):
        return self.__reproducido_en_cautiverio

    @reproducido_en_cautiverio.setter
    def reproducido_en_cautiverio(self, value):
        self.__reproducido_en_cautiverio = value

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, value):
        self.__edad = value

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, value):
        self.__categoria = value

