from vista.indice_aceptacion import VentanaIndiceAceptacion


class ControladorIndiceAceptacion:

    def __init__(self, repo):
        self.__vista = VentanaIndiceAceptacion(self)
        self.__repositorio = repo

    def iniciar(self):
        self.__vista.show()

    def cerrar(self):
        self.__vista.close()

    def get_indice(self):
        try:
            id = self.__vista.id
            if self.__repositorio.ind_especie(id) is None:
                raise Exception('No hay especie registrada con ese ID')
            self.__vista.indice = str(self.__repositorio.ind_acep(id))

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])
