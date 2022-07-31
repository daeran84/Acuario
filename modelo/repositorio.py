from modelo.entrenador import Entrenador
from datetime import date

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

    def id_entrenador(self, ci):  # OK
        for i in range(len(self.lista_entrenadores)):
            if self.lista_entrenadores[i].es_ci_entrenador(int(ci)):
                return i

    def incertar_entrenador(self, entrenador):  # OK
        if self.id_entrenador(entrenador.ci) != None:
            raise Exception('El Entrenador ya existe')
        self.lista_entrenadores.append(entrenador)

    def actualizar_entrenador(self, ci_ant, entrenador):  # OK
        ind_ant = self.id_entrenador(ci_ant)
        if ind_ant == None:
            raise Exception('El entrenador no existe')
        ind_new = self.id_entrenador(entrenador.ci)
        if (ind_new != None and ind_new != ind_ant):
            raise Exception('El entrenador existe en el controlador')
        self.lista_entrenadores[ind_ant] = entrenador

    def eliminar_entrenador(self, ci):
        ind = self.id_entrenador(ci)
        if ind == None:
            raise Exception('El entrenador no existe')
        self.lista_entrenadores.remove(self.lista_entrenadores[ind])