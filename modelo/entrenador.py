class Entrenador:

    def __init__(self, ci, nombre_apellidos, nombre_artistico, edad, sexo, fecha_nacimiento, anios_experiencia):
        self.__ci = ci
        self.__nombre_apellidos = nombre_apellidos
        self.__nombre_artistico = nombre_artistico
        self.__edad = edad
        self.__sexo = sexo
        self.__fecha_nacimiento = fecha_nacimiento
        self.__anios_experiencia = anios_experiencia

    # PROPS

    @property
    def ci(self):
        return self.__ci

    @ci.setter
    def ci(self, value):
        self.__ci = value

    @property
    def nombre_apellidos(self):
        return self.__nombre_apellidos

    @nombre_apellidos.setter
    def nombre_apellidos(self, value):
        self.__nombre_apellidos = value

    @property
    def nombre_artistico(self):
        return self.__nombre_artistico

    @nombre_artistico.setter
    def nombre_artistico(self, value):
        self.__nombre_artistico = value

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, value):
        self.__edad = value

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, value):
        self.__sexo = value

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        self.__fecha_nacimiento = value

    @property
    def anios_experiencia(self):
        return self.__anios_experiencia

    @anios_experiencia.setter
    def anios_experiencia(self, value):
        self.__anios_experiencia = value

    def es_ci_entrenador(self, ci):
        return int(self.ci) == int(ci)

#    def __repr__(self):
#        return f'Nombre: {self.__nombre_apellidos}\n Nombre Artistico: {self.__nombre_artistico}\n Carnet de Identidad: {self.__ci}\n Fecha de nacimiento: {self.__fecha_nacimiento}\n Edad: {self.__edad}\n Sexo: {self.__sexo}\n Años de experiencia: {self.__anios_experiencia}'