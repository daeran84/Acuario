from vista.planta_acuatica import VentanaPlantaAcuatica
from modelo.planta_aquatica import PlantaAquatica


class ControladorPlantaAcuatica:

    def __init__(self, repo):
        self.__vista = VentanaPlantaAcuatica(self)
        self.__repositorio = repo

    def iniciar(self):
        self.__vista.setWindowTitle('Plantas Acuaticas')
        self.__vista.show()

    def cerrar(self):
        self.__vista.close()

    def cargar_datos(self):
        try:
            self.__vista.vaciar_tabla()
            pass

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def insertar_planta_acuatica(self):
        try:
            self.__vista.vaciar_tabla()
            id = self.__vista.id
            nombre_c = self.__vista.nombre_cient
            familia = self.__vista.planta_familia
            habitat = self.__vista.planta_habitat
            ejemplares = self.__vista.ejemplares
            profundas = self.__vista.aguas_profundas
            planta = PlantaAquatica(id, nombre_c, familia, habitat, ejemplares, profundas)
            self.__repositorio.insertar_especie(planta)
            self.cargar_datos()
            self.__vista.restablecer_datos()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def actualizar_planta_acuatica(self):
        try:
            pass

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def eliminar_planta_acuatica(self):
        try:
            pass

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def llenar_formulario_x_tabla(self):
        try:
            pass

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])
