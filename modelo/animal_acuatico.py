from modelo.especie_acuatica import EspecieAcuatica


class AnimalAquatico(EspecieAcuatica):

    def __init__(self, id, nombre, nombre_cientifico, familia, habitat_natural, edad, categoria, reproducido_en_cautiverio, espectaculo, fecha_inicio, nombre_entrenador):
        EspecieAcuatica.__init__(self, id, nombre_cientifico, familia, habitat_natural)
        self.__nombre = nombre
        self.__reproducido_en_cautiverio = reproducido_en_cautiverio
        self.__edad = edad
        self.__categoria = categoria
        self.__espectaculo = espectaculo
        self.__fecha_inicio = fecha_inicio
        self.__nombre_entrenador = nombre_entrenador

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

    @property
    def espectaculo(self):
        return self.__espectaculo

    @espectaculo.setter
    def espectaculo(self, value):
        self.__espectaculo = value

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value):
        self.__fecha_inicio = value

    @property
    def nombre_entrenador(self):
        return self.__nombre_entrenador

    @nombre_entrenador.setter
    def nombre_entrenador(self, value):
        self.__nombre_entrenador = value