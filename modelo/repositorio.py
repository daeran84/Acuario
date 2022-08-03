from modelo.animal_acuatico import AnimalAquatico


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

    def planta_acuatica(self):
        pass

    def animal_acuatico(self):  # OK
        acuatica_id = []
        for esp in self.__lista_especies:
            if isinstance(esp, AnimalAquatico):
                acuatica_id.append(esp)
        return acuatica_id

    def ind_especie(self, id_esp):  # OK
        for i in range(len(self.__lista_especies)):
            if self.__lista_especies[i].es_id_especie(id_esp):
                return i

    def insertar_especie(self, especie):  # OK
        if self.ind_especie(especie.id) != None:
            raise Exception('La especie acuática ya existe')
        self.__lista_especies.append(especie)
        print(self.__lista_especies)

    def actualizar_especie(self, id_esp, especie):  # OK
        ind_ant = self.ind_especie(id_esp)
        if ind_ant == None:
            raise Exception('Ese registro no existe')
        ind_new = self.ind_especie(especie.id)
        if (ind_new != None and ind_new != ind_ant):
            raise Exception('Ese registro existe en el controlador')
        self.__lista_especies[ind_ant] = especie

    def eliminar_especie(self, id_esp):  # OK
        ind = self.ind_especie(id_esp)
        if ind == None:
            raise Exception('Ese registro no existe')
        self.__lista_especies.remove(self.__lista_especies[ind])

    # Functions for lista_espectaculos


    def insertar_espectaculo(self):
        pass

    def actualizar_espectaculo(self):
        pass

    def eliminar_espectaculo(self):
        pass

    # Functions for Lista_entrenadores

    def ind_entr_x_nombre(self, nombre_entr):
        for i in range(len(self.__lista_entrenadores)):
            if self.__lista_entrenadores[i].es_nombre_entrenador(nombre_entr):
                return i

    def id_entrenador(self, ci):  # OK
        for i in range(len(self.lista_entrenadores)):
            if self.lista_entrenadores[i].es_ci_entrenador(int(ci)):
                return i

    def insertar_entrenador(self, entrenador):  # OK
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

    def eliminar_entrenador(self, ci):  # OK
        ind = self.id_entrenador(ci)
        if ind == None:
            raise Exception('El entrenador no existe')
        self.lista_entrenadores.remove(self.lista_entrenadores[ind])