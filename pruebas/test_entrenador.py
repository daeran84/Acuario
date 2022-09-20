from unittest import TestCase
from datetime import date
from modelo.entrenador import Entrenador


class TestAnimalAcuatico(TestCase):
    def setUp(self):
        self.entrenador1 = Entrenador('98102632132', 'Elizabeth Perez Usbert', 'Eli', '26', 'F', date(1998, 6, 16), '5')
        self.entrenador2 = Entrenador('00041226321', 'Pedro Hernandez Gonzalez', 'Pepe', '24', 'M', date(2000, 4, 12), '1')
        self.entrenador3 = Entrenador('83021965987', 'Juan García Hernández', 'García', '38', 'M', date(1983, 2, 19), '10')
        self.entrenador4 = Entrenador('00032654214', 'Maria Benitez Marín', 'Marín', '24', 'M', date(2000, 3, 26), '1')

    def test_init(self):
        self.assertIsNotNone(self.entrenador1)
        self.assertIsNotNone(self.entrenador2)
        self.assertIsNotNone(self.entrenador3)
        self.assertIsNotNone(self.entrenador4)

    def test_property_ci(self):
        self.assertEqual(self.entrenador1.ci, '98102632132')
        self.assertEqual(self.entrenador2.ci, '00041226321')
        self.assertEqual(self.entrenador3.ci, '83021965987')
        self.assertEqual(self.entrenador4.ci, '00032654214')

    def test_property_nombre_apellidos(self):
        self.assertEqual(self.entrenador1.nombre_apellidos, 'Elizabeth Perez Usbert')
        self.assertEqual(self.entrenador2.nombre_apellidos, 'Pedro Hernandez Gonzalez')
        self.assertEqual(self.entrenador3.nombre_apellidos, 'Juan García Hernández')
        self.assertEqual(self.entrenador4.nombre_apellidos, 'Maria Benitez Marín')

    def test_property_nombre_artistico(self):
        self.assertEqual(self.entrenador1.nombre_artistico, 'Eli')
        self.assertEqual(self.entrenador2.nombre_artistico, 'Pepe')
        self.assertEqual(self.entrenador3.nombre_artistico, 'García')
        self.assertEqual(self.entrenador4.nombre_artistico, 'Marín')

    def test_property_edad(self):
        self.assertEqual(self.entrenador1.edad, '26')
        self.assertEqual(self.entrenador2.edad, '24')
        self.assertEqual(self.entrenador3.edad, '38')
        self.assertEqual(self.entrenador4.edad, '24')

    def test_property_sexo(self):
        self.assertEqual(self.entrenador1.sexo, 'F')
        self.assertEqual(self.entrenador2.sexo, 'M')
        self.assertEqual(self.entrenador3.sexo, 'M')
        self.assertEqual(self.entrenador4.sexo, 'M')

    def test_property_anios_experiencia(self):
        self.assertEqual(self.entrenador1.anios_experiencia, '5')
        self.assertEqual(self.entrenador2.anios_experiencia, '1')
        self.assertEqual(self.entrenador3.anios_experiencia, '10')
        self.assertEqual(self.entrenador4.anios_experiencia, '1')
