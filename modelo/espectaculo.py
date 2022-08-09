

class Espectaculo:

    def __init__(self, codigo, nombre, hora_inicio, duracion, publico, animales):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__hora_inicio = hora_inicio
        self.__duracion = duracion
        self.__publico = publico
        self.__animales = animales

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, value):
        self.__codigo = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def hora_inicio(self):
        return self.__hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, value):
        self.__hora_inicio = value

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, value):
        self.__duracion = value

    @property
    def publico(self):
        return self.__publico

    @publico.setter
    def publico(self, value):
        self.__publico = value

    @property
    def animales(self):
        return self.__animales

    @animales.setter
    def animales(self, value):
        self.__animales = value