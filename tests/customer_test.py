import unittest 
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("Bob", 20.00)
        self.customer2 = Customer("Dev", 15.00)
        self.pub1 = Pub("Bob and Dev's", 300.00)
        self.drink1 = Drink("Dark and Stormy", 4.50)
        self.drink2 = Drink("Zombie", 6.25)
        self.pub1.add_drinks(self.drink1)
        self.pub1.add_drinks(self.drink2)


    def test_customer_name(self):
        self.assertEqual("Bob", self.customer1.name)   


    def test_customer_wallet(self):
        self.assertEqual(15.00, self.customer2.wallet)


    def test_customer_can_buy(self):
        self.customer1.buy_drink(self.pub1.drinks[0])
        self.assertEqual(15.50, self.customer1.wallet)

       

              