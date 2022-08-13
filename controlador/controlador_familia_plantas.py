from vista.familia_plantas import VentanaFamiliaPlantas


class ControladorFamiliaPlantas:

    def __init__(self, repo):
        self.__vista = VentanaFamiliaPlantas(self)
        self.__repositorio = repo
        self.__repositorio.get_familia_plantas()

    def iniciar(self):
        self.__vista.show()

    def cerrar(self):
        self.__vista.close()

    def get_indice_familia(self):
        max_ind = 0
        familias = self.__repositorio.indice_familias_plantas
        familia = ''
        for fam in familias.keys():
            if familias.get(fam) > max_ind:
                max_ind = familias.get(fam)
                familia = fam
        self.__vista.familia = familia
