import unittest 
from src.pub import Pub

class TestPub(unittest.TestCase):
    

    def setUp(self):
        self.pub1 = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub1.name)   


    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub1.till)    

    # Arranged
    def test_increase_till(self):
        # Act
        self.pub1.increase_till(2.50)    
        # Asserting
        self.assertEqual(102.50, self.pub1.till)