import sys
from datetime import date
from PyQt5.QtWidgets import QApplication
from modelo.repositorio import Repositorio
from modelo.entrenador import Entrenador
from modelo.animal_acuatico import AnimalAquatico
from modelo.planta_aquatica import PlantaAquatica
from vista.ventana_principal import VentanaPrincipal
from controlador.controlador_animal_acuatico import ControladorAnimalAcuatico
from controlador.controlador_entrenador import ControladorEntrenador
from controlador.controlador_planta_acuatica import ControladorPlantaAcuatica
from controlador.controlador_espectaculo import ControladorEspectaculo


class ControladorPrincipal:

    def __init__(self):
        self.__repositorio = Repositorio()

        # Carga inicial de entrenadores para pruebas

        entrenador1 = Entrenador('98765432132','Elizabeth Perez Usbert', 'Eli', '26', 'F', date(1998, 6, 16), '3')
        entrenador2 = Entrenador('20041226321', 'Pedro Hernandez Gonzalez', 'Pepe', '20', 'M', date(2004, 12, 26), '1')

        self.__repositorio.lista_entrenadores.append(entrenador1)
        self.__repositorio.lista_entrenadores.append(entrenador2)

        # Carga inicial de especies para pruebas

        animal1 = AnimalAquatico(1, 'Millie', 'Delphinidae', 'delfines', 'Mar', 3, 'Mamíferos', 'Si', 'Si', date(2017, 1, 17), 'Elizabeth Perez Usbert')
        animal2 = AnimalAquatico(2, 'Bart', 'Otaria flavescens', 'lobos marinos', 'Mar', 3, 'Mamíferos', 'Si', 'Si', date(2006, 5, 28), 'Pedro Hernandez Gonzalez')
        animal3 = AnimalAquatico(7, 'Lili', 'Spheniscidae', 'otros', 'Mar', 1, 'Aves', 'Si', 'No', '', '')
        animal4 = AnimalAquatico(8, 'Bily', 'Spheniscidae', 'otros', 'Mar', 2, 'Aves', 'Si', 'No', '', '')

        planta1 = PlantaAquatica(3, 'Nymphaea odorata alba blanca', 'Nympháceas', 'Rio', 26, 'No')
        planta2 = PlantaAquatica(4, 'Limnobium laevigatum', 'Hidrocaritáceas', 'Rio', 7, 'No')
        planta3 = PlantaAquatica(5, 'Azolla filiculoides', 'Salviniáceas', 'Rio', 13, 'No')
        planta4 = PlantaAquatica(6, 'Spirodela intermedia', 'Lemnáceas', 'Rio', 21, 'No')

        self.__repositorio.lista_especies.append(animal1)
        self.__repositorio.lista_especies.append(animal2)
        self.__repositorio.lista_especies.append(planta1)
        self.__repositorio.lista_especies.append(planta2)
        self.__repositorio.lista_especies.append(planta3)
        self.__repositorio.lista_especies.append(planta4)
        self.__repositorio.lista_especies.append(animal3)
        self.__repositorio.lista_especies.append(animal4)

    # Main start and child windows call functions

    def iniciar(self):
        app = QApplication(sys.argv)
        self.vista = VentanaPrincipal(self)
        self.vista.setWindowTitle('Acuario')
        self.vista.show()
        app.exec_()

    def gestion_anim_ac(self):
        pen = ControladorAnimalAcuatico(self.__repositorio)
        pen.iniciar()

    def gestion_entrenadores(self):
        pen = ControladorEntrenador(self.__repositorio)
        pen.iniciar()

    def gestion_planta_ac(self):
        pen = ControladorPlantaAcuatica(self.__repositorio)
        pen.iniciar()

    def gestion_espectaculos(self):
        pen = ControladorEspectaculo(self.__repositorio)
        pen.iniciar()