import unittest 
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("Bob", 20.00)
        self.customer2 = Customer("Dev", 15.00)


    def test_customer_name(self):
        self.assertEqual("Bob", self.customer1.name)   


    def test_customer_wallet(self):
        self.assertEqual(15.00, self.customer2.wallet)


    def test_customer_can_buy(self):
        self.customer1.buy_drink(4.50)        