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
        print('cargando datos')

    def incertar_entrenador(self):
        print('incertar')

    def actualizar_entrenador(self):
        print('actualizar')

    def eliminar_entrenador(self):
        print('eliminar')

    def llenar_formulario_x_tabla(self):
        print('tabla')