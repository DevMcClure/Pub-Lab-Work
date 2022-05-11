import unittest 
from src.pub import Pub

class TestPub(unittest.TestCase):
    

    def setUp(self):
        self.pub1 = Pub("Bob and Dev's", 300.00)

    def test_pub_has_name(self):
        self.assertEqual("Bob and Dev's", self.pub1.name)   

    def test_pub_has_till(self):
        self.assertEqual(300.00,self.pub1.till)    
