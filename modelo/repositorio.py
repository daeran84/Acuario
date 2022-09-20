from modelo.animal_acuatico import AnimalAquatico
from modelo.planta_aquatica import PlantaAquatica


class Repositorio:
    def __init__(self):
        self.__lista_especies = []
        self.__lista_espectaculos = []
        self.__lista_entrenadores = []
        self.__tipo_espectaculo = {}
        self.__familias_plantas = {}

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

    @property
    def familias_plantas(self):
        return self.__familias_plantas

    @familias_plantas.setter
    def familias_plantas(self, value):
        self.__familias_plantas = value

    # Functions for Dic

    def agregar_reg_tipo_esp(self, reg):
        self.tipo_espectaculo.update(reg)

    def eliminar_reg_tipo_esp(self, key):
        self.tipo_espectaculo.pop(key)

    def familia_plantas_mas_representada(self):
        max_ind = 0
        familias = self.familias_plantas
        familia = ''
        for fam in familias.keys():
            if familias[fam] > max_ind:
                max_ind = familias[fam]
                familia = fam
        return familia

    def get_familia_plantas(self):
        self.familias_plantas = {}
        plantas = self.planta_acuatica()
        for planta in plantas:
            if planta.familia not in self.familias_plantas.keys():
                self.familias_plantas.update({planta.familia: 0})
            value = planta.num_ejemplares
            self.familias_plantas.update({planta.familia: value})

    # Functions for lista_especies

    def datos_animales(self, entr):
        animales = []
        for anim in self.animal_acuatico():
            if anim.espectaculo and anim.nombre_entrenador == entr:
                animales.append(anim)
        return sorted(animales, key=lambda x: x.edad)

    def ind_acep(self, id):
        for esp in self.lista_especies:
            if int(esp.id) == id:
                return esp.ind_acep()

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
            raise Exception('Ese registro existe en el presentador')
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

    def actualizar_espectaculo(self, codigo, espect):
        ind_ant = self.ind_espectaculo(codigo)
        if ind_ant is None:
            raise Exception('El espectaculo no existe')
        ind_new = self.ind_espectaculo(espect.codigo)
        if ind_new is not None and ind_new != ind_ant:
            raise Exception('El entrenador existe en el presentador')
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
            raise Exception('El entrenador existe en el presentador')
        self.lista_entrenadores[ind_ant] = entrenador

    def eliminar_entrenador(self, ci):  # OK
        ind = self.id_entrenador(ci)
        if ind is None:
            raise Exception('El entrenador no existe')
        for i in self.animal_acuatico():
            if i.nombre_entrenador == self.lista_entrenadores[ind].nombre_apellidos:
                i.nombre_entrenador = ''
        self.lista_entrenadores.remove(self.lista_entrenadores[ind])

    def animales_del_entrenador(self, entr):
        anim = []
        for i in self.animal_acuatico():
            if i.nombre_entrenador == entr:
                anim.append(i.nombre)
        return anim
