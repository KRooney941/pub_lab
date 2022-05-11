import unittest
from src.customer import Customer
from src.drink import Drink


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("Barry", 500, 42)
        self.customer2 = Customer("Grant", 5, 16)

    def test_customer_name(self):
        self.assertEqual("Barry", self.customer1.name)

    def test_customer_wallet(self):
        self.assertEqual(500, self.customer1.wallet)

    def test_remove_money(self):
        self.customer1.remove_money(3.50)
        self.assertEqual(496.50, self.customer1.wallet)

    def test_give_drink_to_customer(self):
        drink1 = Drink("vodka coke", 3.00, 10)
        self.customer1.add_drink(drink1)
        self.assertEqual(drink1, self.customer1.drink)
