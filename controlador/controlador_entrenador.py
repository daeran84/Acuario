from vista.entrenador import VentanaEntrenador


class ControladorEntrenador:

    def __init__(self, repo):
        self.vista = VentanaEntrenador(self)
        self.repositorio = repo

    # Window main functions

    def iniciar(self):
        self.vista.setWindowTitle('Entrenadores')
        self.vista.show()

    def cerrar(self):
        self.vista.close()

    # Functions for list management

    def cargar_datos(self):
        pass

    def incertar_entrenador(self):
        pass

    def actualizar_entrenador(self):
        pass

    def eliminar_entrenador(self):
        pass

    def llenar_formulario_x_tabla(self):
        pass