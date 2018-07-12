import unittest
import sys
sys.path.append('../')
from animal import Animal 
from animal import Dog


class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bob = Dog("Bob")
    
    def test_animal_creation(self):
        # One off instance of a created animal
        murph = Dog("Murph")

        self.assertIsInstance(murph, Dog)
        self.assertIsInstance(murph, Animal)

    def test_animal_can_set_legs(self):
        self.bob.set_legs(6)
        self.assertEqual(self.bob.legs, 6)

    def test_animal_can_set_species(self):
        self.bob.set_species(Dog("Bob"))
        self.assertIsInstance(self.bob.species, Dog)

    def test_animal_can_get_name(self):
        name = self.bob.get_name
        self.assertIsNotNone(name)

    def test_animal_speed(self):
        speed = self.bob.speed
        self.assertIsNotNone(speed)

    def test_animal_walk(self):
       self.bob.set_legs(1)
       self.bob.walk()
       self.assertEqual(self.bob.speed, 0.2)

if __name__ == '__main__':
    unittest.main()