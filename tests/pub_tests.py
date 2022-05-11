import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink


class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub1 = Pub(
            "The Dog and Duck",
            100.00, [Drink("vodka coke", 3.00, 10), Drink(
                "Tennents", 3.50, 5), Drink("Gin and Tonic", 4.00, 7), Drink("Venom", 5.00, 15)]
        )
        self.customer2 = Customer("John", 100, 22)
        self.customer3 = Customer("Craig", 5, 15)

    def test_pub_has_name(self):
        self.assertEqual("The Dog and Duck", self.pub1.name)

    def test_return_till(self):
        self.assertEqual(100.00, self.pub1.till)

    def test_increase_till(self):
        self.pub1.add_money(3.50)
        self.assertEqual(103.50, self.pub1.till)

    def find_drink_by_name(self):
        drink1 = self.find_drink("vodka coke")
        self.assertEqual("vodka coke", self.drink1.name)

    def test_sell_drink(self):
        drink1 = self.pub1.find_drink("vodka coke")
        self.pub1.sell_drink(self.customer2, drink1)
        self.assertEqual(97.00, self.customer2.wallet)
        self.assertEqual(103.00, self.pub1.till)
        self.assertEqual(drink1, self.customer2.drink)

    def test_sell_drink(self):
        drink1 = self.pub1.find_drink("vodka coke")
        self.pub1.sell_drink(self.customer3, drink1)
        self.assertEqual(5, self.customer3.wallet)
        self.assertEqual(100.00, self.pub1.till)
        self.assertEqual([], self.customer3.drink)
