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
from controlador.controlador_animales_entrenador import ControladorAnimalesEntrenador
from controlador.controlador_indice_aceptacion import ControladorIndiceAceptacion
from controlador.controlador_familia_plantas import ControladorFamiliaPlantas


class ControladorPrincipal:

    def __init__(self):
        self.__repositorio = Repositorio()

        # Trainers Test Cases

        entrenador1 = Entrenador('98102632132', 'Elizabeth Perez Usbert', 'Eli', '26', 'F', date(1998, 6, 16), '5')
        entrenador2 = Entrenador('00041226321', 'Pedro Hernandez Gonzalez', 'Pepe', '24', 'M', date(2000, 4, 12), '1')
        entrenador3 = Entrenador('83021965987', 'Juan García Hernández', 'García', '38', 'M', date(1983, 2, 19), '10')
        entrenador4 = Entrenador('00032654214', 'Maria Benitez Marín', 'Marín', '24', 'M', date(2000, 3, 26), '1')
        entrenador5 = Entrenador('95041926321', 'Jesus Perez Mayo', 'Mayo', '29', 'M', date(1995, 4, 19), '8')

        self.__repositorio.lista_entrenadores.append(entrenador1)
        self.__repositorio.lista_entrenadores.append(entrenador2)
        self.__repositorio.lista_entrenadores.append(entrenador3)
        self.__repositorio.lista_entrenadores.append(entrenador4)
        self.__repositorio.lista_entrenadores.append(entrenador5)

        # Species Test Cases

        animal1 = AnimalAquatico(1, 'Millie', 'Delphinidae', 'delfines', 'Mar', 3, 'Mamíferos', 'Si', 'No', '', '')
        animal2 = AnimalAquatico(2, 'Bart', 'Otaria flavescens', 'lobos marinos', 'Mar', 3, 'Mamíferos', 'Si', 'Si',
                                 date(2006, 5, 28), 'Pedro Hernandez Gonzalez')
        animal3 = AnimalAquatico(7, 'Lili', 'Spheniscidae', 'otros', 'Mar', 1, 'Aves', 'Si', 'No', '', '')
        animal4 = AnimalAquatico(8, 'Bily', 'Spheniscidae', 'otros', 'Mar', 2, 'Aves', 'Si', 'No', '', '')
        animal5 = AnimalAquatico(9, 'Bob', 'Delphinidae', 'delfines', 'Mar', 10, 'Mamíferos', 'No', 'Si',
                                 date(2017, 1, 17), 'Juan García Hernández')
        animal6 = AnimalAquatico(10, 'Sparky', 'Delphinidae', 'delfines', 'Mar', 9, 'Mamíferos', 'No', 'Si',
                                 date(2017, 1, 17), 'Elizabeth Perez Usbert')
        animal7 = AnimalAquatico(11, 'May', 'Delphinidae', 'delfines', 'Mar', 11, 'Mamíferos', 'No', 'Si',
                                 date(2017, 1, 17), 'Juan García Hernández')
        animal8 = AnimalAquatico(12, 'Juno', 'Delphinidae', 'delfines', 'Mar', 9, 'Mamíferos', 'No', 'Si',
                                 date(2017, 1, 17), 'Jesus Perez Mayo')

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
        self.__repositorio.lista_especies.append(animal5)
        self.__repositorio.lista_especies.append(animal6)
        self.__repositorio.lista_especies.append(animal7)
        self.__repositorio.lista_especies.append(animal8)

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

    def reportes_animales_entrenador(self):
        pen = ControladorAnimalesEntrenador(self.__repositorio)
        pen.iniciar()

    def reportes_indice_aceptacion(self):
        pen = ControladorIndiceAceptacion(self.__repositorio)
        pen.iniciar()

    def reportes_aceptacion_familia_plantas(self):
        pen = ControladorFamiliaPlantas(self.__repositorio)
        pen.iniciar()
