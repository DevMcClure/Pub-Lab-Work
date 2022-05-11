import unittest 
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("Bob", 20.00)
        self.customer2 = Customer("Dev", 15.00)


    def test_customer_name(self):
        self.assertEqual("Bob", self.customer1.name)   