import unittest
from src.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        # self.drink_list = [Drink("vodka coke", 3.00), Drink(
        #     "Tennents", 3.50), Drink("Gin and Tonic", 4.00), Drink("Venom", 5.00)]

        # def test_get_drink_by_name(self, name):
        #     drink1 = get_drink_by_name("Tennents")
        #     self.assertEqual("Tennents", drink1.name)

        self.drink1 = Drink("vodka coke", 3.00, 10)

    def test_drink_has_name(self):
        self.assertEqual("vodka coke", self.drink1.name)

    def test_price(self):
        self.assertEqual(3.00, self.drink1.price)

    def test_alcohol_level(self):
        self.assertEqual(10, self.drink1.alcohol_level)
