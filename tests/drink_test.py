import unittest 
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Dark and Stormy", 4.50, 1)
        self.drink2 = Drink("Zombie", 6.25, 2)
    
    def test_drink_name(self):
        self.assertEqual("Zombie", self.drink2.name)

    def test_drink_price(self):
        self.assertEqual(4.50, self.drink1.price)

    def test_drink_alcohol_level(self):
        self.assertEqual(1, self.drink1.alcohol_level)    
        