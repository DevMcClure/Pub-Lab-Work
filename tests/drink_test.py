import unittest 
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Dark and Stormy", 4.50)
        self.drink2 = Drink("Zombie", 6.25)
    
    def test_drink_name(self):
        self.assertEqual("Zombie", self.drink2.name)
        