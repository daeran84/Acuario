from unittest import TestCase
from datetime import date
from modelo.animal_acuatico import AnimalAquatico


class TestAnimalAcuatico(TestCase):
    def setUp(self):
        self.animal1 = AnimalAquatico(1, 'Millie', 'Delphinidae', 'delfines', 'Mar', 3, 'Mamíferos', 'Si', 'No', '', '')
        self.animal2 = AnimalAquatico(2, 'Bart', 'Otaria flavescens', 'lobos marinos', 'Mar', 3, 'Mamíferos', 'Si', 'Si', date(2006, 5, 28), 'Pedro Hernandez Gonzalez')
        self.animal3 = AnimalAquatico(7, 'Lili', 'Spheniscidae', 'otros', 'Mar', 1, 'Aves', 'Si', 'No', '', '')
        self.animal4 = AnimalAquatico(8, 'Bily', 'Spheniscidae', 'otros', 'Mar', 2, 'Aves', 'Si', 'No', '', '')
        self.animal5 = AnimalAquatico(9, 'Bob', 'Delphinidae', 'delfines', 'Mar', 10, 'Mamíferos', 'No', 'Si', date(2017, 1, 17), 'Juan García Hernández')
        self.animal6 = AnimalAquatico(10, 'Sparky', 'Delphinidae', 'delfines', 'Mar', 9, 'Mamíferos', 'No', 'Si', date(2017, 1, 17), 'Elizabeth Perez Usbert')
        self.animal7 = AnimalAquatico(11, 'May', 'Delphinidae', 'delfines', 'Mar', 11, 'Mamíferos', 'No', 'Si', date(2017, 1, 17), 'Juan García Hernández')
        self.animal8 = AnimalAquatico(12, 'Juno', 'Delphinidae', 'delfines', 'Mar', 9, 'Mamíferos', 'No', 'Si', date(2017, 1, 17), 'Jesus Perez Mayo')

    def test_properties(self):
        self.assertEqual(self.animal1.nombre, 'Millie')
        self.assertEqual(self.animal1.)