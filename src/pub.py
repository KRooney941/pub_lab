from src.customer import Customer
from src.drink import Drink


class Pub:
    def __init__(self, name, till, drink):
        self.name = name
        self.till = till
        self.drink = drink

    def add_money(self, amount):
        self.till += amount

    def find_drink(self, name):
        for drink in self.drink:
            if drink.name == name:
                return drink

    def give_customer_drink(self, customer, drink):
        self.customer.drink.append(drink)

    def sell_drink(self, customer, drink):
        if customer.age > 17:
            customer.remove_money(drink.price)
            self.add_money(drink.price)
            customer.add_drink(drink)
        return
