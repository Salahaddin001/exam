class Pizza:
    class PepperoniPizza:
        def __init__(name, dough, sauce, toppings, price):
            self.name = name
            self.dough = dough
            self.sauce = sauce
            self.toppings = toppings
            self.price = price
    class BBQPizza:
        def __init__(name, dough, sauce, toppings, price, ingridients):
            self.name = name
            self.dough = dough
            self.sauce = sauce
            self.toppings = toppings
            self.price = price
            self.ingridients = ingridients
    class SeafoodPizza:
        def __init__(name, dough, sauce, toppings, price):
            self.name = name
            self.dough = dough
            self.sauce = sauce
            self.toppings = toppings
            self.price = price

class Order:
    