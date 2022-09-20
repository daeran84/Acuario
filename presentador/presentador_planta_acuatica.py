from vista.planta_acuatica import VentanaPlantaAcuatica
from modelo.planta_aquatica import PlantaAquatica


class PresentadorPlantaAcuatica:

    def __init__(self, repo):
        self.__vista = VentanaPlantaAcuatica(self)
        self.__repositorio = repo
        self.get_id()

    def iniciar(self):
        self.__vista.setWindowTitle('Plantas Acuaticas')
        self.cargar_datos()
        self.__vista.show()

    def cerrar(self):
        self.__vista.close()

    def get_id(self):  # mover a Repositorio
        id = self.__repositorio.last_id() + 1
        self.__vista.id = str(id)

    def cargar_datos(self):
        try:
            self.__vista.vaciar_tabla()
            for plant in self.__repositorio.planta_acuatica():
                ind = self.__vista.tabla_planta_acuatica.rowCount()
                self.__vista.tabla_planta_acuatica.insertRow(ind)
                self.__vista.agregar_elemento_tabla(ind, 0, str(plant.id))
                self.__vista.agregar_elemento_tabla(ind, 1, plant.nombre_cientifico)
                self.__vista.agregar_elemento_tabla(ind, 2, plant.familia)
                self.__vista.agregar_elemento_tabla(ind, 3, plant.habitat_natural)
                self.__vista.agregar_elemento_tabla(ind, 4, str(plant.num_ejemplares))
                self.__vista.agregar_elemento_tabla(ind, 5, plant.aguas_profundas)
                self.__vista.tabla_planta_acuatica.resizeColumnsToContents()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def insertar_planta_acuatica(self):
        try:
            self.__vista.validar_datos()
            id = int(self.__vista.id)
            nombre_c = self.__vista.nombre_cient
            familia = self.__vista.planta_familia
            habitat = self.__vista.planta_habitat
            ejemplares = int(self.__vista.ejemplares)
            profundas = self.__vista.aguas_profundas
            planta = PlantaAquatica(id, nombre_c, familia, habitat, ejemplares, profundas)
            self.__repositorio.insertar_especie(planta)
            self.cargar_datos()
            self.__vista.restablecer_datos()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def actualizar_planta_acuatica(self):
        try:
            ind = self.__vista.tabla_planta_acuatica.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para actualizarla')
            ind_ant = self.__vista.tabla_planta_acuatica.item(ind, 0)
            self.__vista.validar_datos()
            id = int(self.__vista.id)
            nombre_c = self.__vista.nombre_cient
            familia = self.__vista.planta_familia
            habitat = self.__vista.planta_habitat
            ejemplares = int(self.__vista.ejemplares)
            profundas = self.__vista.aguas_profundas
            planta = PlantaAquatica(id, nombre_c, familia, habitat, ejemplares, profundas)
            self.__repositorio.actualizar_especie(id, planta)
            self.cargar_datos()
            self.__vista.restablecer_datos()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def eliminar_planta_acuatica(self):
        try:
            ind = self.__vista.tabla_planta_acuatica.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar un registro para eliminarlo')
            id = self.__vista.tabla_planta_acuatica.item(ind, 0).text()
            self.__repositorio.eliminar_especie(id)
            self.cargar_datos()
            self.__vista.restablecer_datos()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def llenar_formulario_x_tabla(self):
        try:
            ind = self.__vista.tabla_planta_acuatica.currentRow()
            if ind != -1:
                id = self.__vista.tabla_planta_acuatica.item(ind, 0).text()
                nombre_c = self.__vista.tabla_planta_acuatica.item(ind, 1).text()
                familia = self.__vista.tabla_planta_acuatica.item(ind, 2).text()
                habitat = self.__vista.tabla_planta_acuatica.item(ind, 3).text()
                ejemplares = self.__vista.tabla_planta_acuatica.item(ind, 4).text()
                profunda = self.__vista.tabla_planta_acuatica.item(ind, 5).text()

                self.__vista.id = id
                self.__vista.nombre_cient = nombre_c
                self.__vista.planta_familia = familia
                self.__vista.planta_habitat = habitat
                self.__vista.ejemplares = int(ejemplares)
                self.__vista.aguas_profundas = profunda

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])
