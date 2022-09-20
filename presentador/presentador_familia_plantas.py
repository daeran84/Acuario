from vista.familia_plantas import VentanaFamiliaPlantas


class PresentadorFamiliaPlantas:

    def __init__(self, repo):
        self.__vista = VentanaFamiliaPlantas(self)
        self.__repositorio = repo
        self.__repositorio.get_familia_plantas()

    def iniciar(self):
        self.__vista.setWindowTitle('Familia de plantas más representada')
        self.__vista.show()

    def cerrar(self):
        self.__vista.close()

    def get_familia_plantas_mas_representada(self):
        self.__vista.familia = self.__repositorio.familia_plantas_mas_representada()

