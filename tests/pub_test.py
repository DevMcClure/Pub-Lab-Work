import unittest 
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    

    def setUp(self):
        self.pub1 = Pub("Bob and Dev's", 300.00)
        self.drink1 = Drink("Dark and Stormy", 4.50)
        self.drink2 = Drink("Zombie", 6.25)

    def test_pub_has_name(self):
        self.assertEqual("Bob and Dev's", self.pub1.name)   

    def test_pub_has_till(self):
        self.assertEqual(300.00,self.pub1.till)    

    def test_pub_can_sell(self):
        self.pub1.sell_drink(self.drink1)
        self.assertEqual(304.50, self.pub1.till)

    def test_pub_has_drinks(self):
        self.pub1.add_drinks(self.drink1)
        self.pub1.add_drinks(self.drink2)
        self.assertEqual(2, len(self.pub1.drinks))  
