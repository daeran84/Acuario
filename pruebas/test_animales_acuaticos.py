from unittest import TestCase
from datetime import date
from modelo.animal_acuatico import AnimalAquatico


class TestAnimalAcuatico(TestCase):
    def setUp(self):
        self.animal1 = AnimalAquatico(1, 'Millie', 'Delphinidae', 'delfines', 'Mar', 3, 'Mamíferos', 'Si', 'No', '', '')
        self.animal2 = AnimalAquatico(2, 'Bart', 'Otaria flavescens', 'lobos marinos', 'Mar', 3, 'Mamíferos', 'Si', 'Si', date(2006, 5, 28), 'Pedro Hernandez Gonzalez')
        self.animal3 = AnimalAquatico(7, 'Lili', 'Spheniscidae', 'otros', 'Mar', 1, 'Aves', 'Si', 'No', '', '')
        self.animal4 = AnimalAquatico(8, 'Bily', 'Spheniscidae', 'otros', 'Mar', 2, 'Aves', 'Si', 'No', '', '')

    def test_init(self):
        self.assertIsNotNone(self.animal1)
        self.assertIsNotNone(self.animal2)
        self.assertIsNotNone(self.animal3)
        self.assertIsNotNone(self.animal4)

    def test_property_nombre(self):
        self.assertEqual(self.animal1.nombre, 'Millie')
        self.assertEqual(self.animal2.nombre, 'Bart')
        self.assertEqual(self.animal3.nombre, 'Lili')
        self.assertEqual(self.animal4.nombre, 'Bily')

        self.animal2.nombre = 'Bill'
        self.assertEqual(self.animal2, 'Bill')
        self.animal4.nombre = 'Pip'
        self.assertEqual(self.animal2, 'Pip')

    def test_property_nombre_cientifico(self):
        self.assertEqual(self.animal1.nombre_cientifico, 'Delphinidae')
        self.assertEqual(self.animal2.nombre_cientifico, 'Otaria flavescens')
        self.assertEqual(self.animal3.nombre_cientifico, 'Spheniscidae')
        self.assertEqual(self.animal4.nombre_cientifico, 'Spheniscidae')

    def test_property_familia(self):
        self.assertEqual(self.animal1.familia, 'delfines')
        self.assertEqual(self.animal2.familia, 'lobos marinos')
        self.assertEqual(self.animal3.familia, 'otros')
        self.assertEqual(self.animal4.familia, 'otros')

    def test_property_habitat(self):
        self.assertEqual(self.animal1.habitat_natural, 'Mar')
        self.assertEqual(self.animal2.habitat_natural, 'Mar')
        self.assertEqual(self.animal3.habitat_natural, 'Mar')
        self.assertEqual(self.animal4.habitat_natural, 'Mar')

    def test_property_edad(self):
        self.assertEqual(self.animal1.edad, 3)
        self.assertEqual(self.animal2.edad, 3)
        self.assertEqual(self.animal3.edad, 1)
        self.assertEqual(self.animal4.edad, 2)

    def test_property_categoria(self):
        self.assertEqual(self.animal1.categoria, 'Mamíferos')
        self.assertEqual(self.animal2.categoria, 'Mamíferos')
        self.assertEqual(self.animal3.categoria, 'Aves')
        self.assertEqual(self.animal4.categoria, 'Aves')

    def test_property_rep_cautiverio(self):
        self.assertEqual(self.animal1.reproducido_en_cautiverio, 'Si')
        self.assertEqual(self.animal2.reproducido_en_cautiverio, 'Si')
        self.assertEqual(self.animal3.reproducido_en_cautiverio, 'Si')
        self.assertEqual(self.animal4.reproducido_en_cautiverio, 'Si')

    def test_property_espectaculo(self):
        self.assertEqual(self.animal1.espectaculo, 'No')
        self.assertEqual(self.animal2.espectaculo, 'Si')
        self.assertEqual(self.animal3.espectaculo, 'No')
        self.assertEqual(self.animal4.espectaculo, 'No')
