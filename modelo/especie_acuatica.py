class EspecieAcuatica:

    def __init__(self, id, nombre_cientifico, familia, habitat_natural):
        self.__id = id
        self.__nombre_cientifico = nombre_cientifico
        self.__familia = familia
        self.__habitat_natural = habitat_natural

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__idr = value


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

    def es_id_especie(self, id):
        return int(self.id) == int(id)

    def ind_acep_base(self):
        if self.habitat_natural == 'Mar':
            return 0.9
        if self.habitat_natural == 'Rio':
            return 0.75
    