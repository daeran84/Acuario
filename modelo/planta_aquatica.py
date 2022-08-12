from modelo.especie_acuatica import EspecieAcuatica


class PlantaAquatica(EspecieAcuatica):

    def __init__(self, id, nombre_cientifico, familia, habitat_natural, num_ejemplares, aguas_profundas):
        EspecieAcuatica.__init__(self, id, nombre_cientifico, familia, habitat_natural)
        self.__num_ejemplares = num_ejemplares
        self.__aguas_profundas = aguas_profundas

    @property
    def num_ejemplares(self):
        return self.__num_ejemplares

    @num_ejemplares.setter
    def num_ejemplares(self, value):
        self.__num_ejemplares = value

    @property
    def aguas_profundas(self):
        return self.__aguas_profundas

    @aguas_profundas.setter
    def aguas_profundas(self, value):
        self.__aguas_profundas = value

    def ind_acep(self):
        acept = self.ind_acep_base()
        if self.aguas_profundas == 'Si':
            acept += 0.05
        acept += (self.num_ejemplares / 100)
        return acept
