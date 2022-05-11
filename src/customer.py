from src.drink import Drink


class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drink = []
        self.drunkenness_level = 0

    def remove_money(self, amount):
        self.wallet -= amount

    def add_drink(self, drink):
        self.drink = drink
