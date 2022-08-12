from modelo.animal_acuatico import AnimalAquatico
from modelo.planta_aquatica import PlantaAquatica
from modelo.espectaculo import Espectaculo


class Repositorio:
    def __init__(self):
        self.__lista_especies = []
        self.__lista_espectaculos = []
        self.__lista_entrenadores = []
        self.__tipo_espectaculo = {}

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

    @property
    def tipo_espectaculo(self):
        return self.__tipo_espectaculo

    @tipo_espectaculo.setter
    def tipo_espectaculo(self, value):
        self.__tipo_espectaculo = value

    # Functions for Dic

    def agregar_reg_tipo_esp(self, reg):
        self.tipo_espectaculo.update(reg)
        print(self.tipo_espectaculo)

    def eliminar_reg_tipo_esp(self, key):
        self.tipo_espectaculo.pop(key)
        print(self.tipo_espectaculo)

    # Functions for lista_especies

    def ind_acep(self, id):
        pass

    def last_id(self):
        id = 0
        if not self.lista_especies:
            return id
        for esp in self.lista_especies:
            if int(esp.id) > id:
                id = esp.id
        return id

    def planta_acuatica(self):
        plantas = []
        for esp in self.lista_especies:
            if isinstance(esp, PlantaAquatica):
                plantas.append(esp)
        return plantas

    def animal_acuatico(self):  # OK
        animales = []
        for esp in self.lista_especies:
            if isinstance(esp, AnimalAquatico):
                animales.append(esp)
        return animales

    def ind_especie(self, id_esp):  # OK
        for i in range(len(self.__lista_especies)):
            if self.__lista_especies[i].es_id_especie(id_esp):
                return i

    def insertar_especie(self, especie):  # OK
        if self.ind_especie(especie.id) is not None:
            raise Exception('Ese numero de registro ya existe, si desea actualizarlo de clic en actualizar,\n '
                            'de lo contrario de clic en Nuevo registro para crear uno nuevo')
        self.__lista_especies.append(especie)

    def actualizar_especie(self, id_esp, especie):  # OK
        ind_ant = self.ind_especie(id_esp)
        if ind_ant is None:
            raise Exception('Ese registro no existe')
        ind_new = self.ind_especie(especie.id)
        if ind_new is not None and ind_new != ind_ant:
            raise Exception('Ese registro existe en el controlador')
        self.__lista_especies[ind_ant] = especie

    def eliminar_especie(self, id_esp):  # OK
        ind = self.ind_especie(id_esp)
        if ind is None:
            raise Exception('Ese registro no existe')
        self.__lista_especies.remove(self.__lista_especies[ind])

    # Functions for lista_espectaculos

    def ind_espectaculo(self, cod):  # Devuelve el indice de la lista que tiene el espectaculo del codigo dado
        for i in range(len(self.__lista_espectaculos)):
            if self.__lista_espectaculos[i].codigo == cod:
                return i

    def insertar_espectaculo(self, espect):
        if self.ind_espectaculo(espect.codigo) is not None:
            raise Exception(
                'Ya existe un Espectáculo con ese código, si desea actualizarlo de clic en actualizar,\n de lo contrario de clic en Nuevo registro para crear uno nuevo')
        self.__lista_espectaculos.append(espect)
        print(self.__lista_espectaculos)

    def actualizar_espectaculo(self, codigo, espect):
        ind_ant = self.ind_espectaculo(codigo)
        if ind_ant is None:
            raise Exception('El espectaculo no existe')
        ind_new = self.ind_espectaculo(espect.codigo)
        if ind_new is not None and ind_new != ind_ant:
            raise Exception('El entrenador existe en el controlador')
        self.lista_espectaculos[ind_ant] = espect

    def eliminar_espectaculo(self, cod):
        ind = self.ind_espectaculo(cod)
        if ind is None:
            raise Exception('El espectaculo no existe')
        self.lista_espectaculos.remove(self.lista_espectaculos[ind])
        self.eliminar_reg_tipo_esp(cod)

    # Functions for Lista_entrenadores

    def entr_x_nombre(self, nombre_entr):
        entrenador = None
        for i in range(len(self.__lista_entrenadores)):
            if self.__lista_entrenadores[i].es_nombre_entrenador(nombre_entr):
                entrenador = self.__lista_entrenadores[i]
        return entrenador

    def id_entrenador(self, ci):  # OK
        for i in range(len(self.lista_entrenadores)):
            if self.lista_entrenadores[i].es_ci_entrenador(int(ci)):
                return i

    def insertar_entrenador(self, entrenador):  # OK
        if self.id_entrenador(entrenador.ci) is not None:
            raise Exception('El Entrenador ya existe')
        self.lista_entrenadores.append(entrenador)

    def actualizar_entrenador(self, ci_ant, entrenador):  # OK
        ind_ant = self.id_entrenador(ci_ant)
        if ind_ant is None:
            raise Exception('El entrenador no existe')
        ind_new = self.id_entrenador(entrenador.ci)
        if ind_new is not None and ind_new != ind_ant:
            raise Exception('El entrenador existe en el controlador')
        self.lista_entrenadores[ind_ant] = entrenador

    def eliminar_entrenador(self, ci):  # OK
        ind = self.id_entrenador(ci)
        if ind is None:
            raise Exception('El entrenador no existe')
        self.lista_entrenadores.remove(self.lista_entrenadores[ind])
