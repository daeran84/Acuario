from unittest import TestCase
from modelo.planta_aquatica import PlantaAquatica


class TestPlantaAcuatica(TestCase):
    def setUp(self):
        self.planta1 = PlantaAquatica(3, 'Nymphaea odorata alba blanca', 'Nympháceas', 'Rio', 26, 'No')
        self.planta2 = PlantaAquatica(4, 'Nymphaea odorata alba blanca', 'Hidrocaritáceas', 'Rio', 7, 'No')
        self.planta3 = PlantaAquatica(5, 'Azolla filiculoides', 'Salviniáceas', 'Rio', 13, 'No')
        self.planta4 = PlantaAquatica(6, 'Spirodela intermedia', 'Lemnáceas', 'Rio', 21, 'No')

    def test_init(self):
        self.assertIsNotNone(self.planta1)
        self.assertIsNotNone(self.planta2)
        self.assertIsNotNone(self.planta3)
        self.assertIsNotNone(self.planta4)

    def test_property_nombre(self):
        self.assertEqual(self.planta1.nombre_cientifico, 'Nymphaea odorata alba blanca')
        self.assertEqual(self.planta2.nombre_cientifico, 'Nymphaea odorata alba blanca')
        self.assertEqual(self.planta3.nombre_cientifico, 'Azolla filiculoides')
        self.assertEqual(self.planta4.nombre_cientifico, 'Spirodela intermedia')

    def test_property_familia(self):
        self.assertEqual(self.planta1.familia, 'Nympháceas')
        self.assertEqual(self.planta2.familia, 'Hidrocaritáceas')
        self.assertEqual(self.planta3.familia, 'Salviniáceas')
        self.assertEqual(self.planta4.familia, 'Lemnáceas')

    def test_property_habitat(self):
        self.assertEqual(self.planta1.habitat_natural, 'Rio')
        self.assertEqual(self.planta2.habitat_natural, 'Rio')
        self.assertEqual(self.planta3.habitat_natural, 'Rio')
        self.assertEqual(self.planta4.habitat_natural, 'Rio')

    def test_property_edad(self):
        self.assertEqual(self.planta1.num_ejemplares, 26)
        self.assertEqual(self.planta2.num_ejemplares, 7)
        self.assertEqual(self.planta3.num_ejemplares, 13)
        self.assertEqual(self.planta4.num_ejemplares, 21)

    def test_property_categoria(self):
        self.assertEqual(self.planta1.aguas_profundas, 'No')
        self.assertEqual(self.planta2.aguas_profundas, 'No')
        self.assertEqual(self.planta3.aguas_profundas, 'No')
        self.assertEqual(self.planta4.aguas_profundas, 'No')
