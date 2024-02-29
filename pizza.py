class Pizza:
    "класс пицца"
    pass
class PepperoniPizza:
    "класс пицца маргарита"
    def __init__(name, dough, sauce, toppings, price):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings
        self.price = price
class BBQPizza:
    "класс пицца BBQ"
    def __init__(name, dough, sauce, toppings, price, ingridients):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings
        self.price = price
        self.ingridients = ingridients
class SeafoodPizza:
    "класс пицца с морепродуктами"
    def __init__(name, dough, sauce, toppings, price):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings
        self.price = price

class Order:
    "список пицц и работа с ними"
    def __init__(self) -> None:
        self.pizzaz: list[Pizza] = []

        def add_pizza(self, pizza: Pizza) -> None:
            self.pizzas.append(pizza)

        def calculate_total(self) -> int:
            return sum(pizza.price for pizza in self.pizzas)


class Terminal:
    """класс для взаимодействия меню и заказами"""

    def __init__(self) -> None:
        self.menu: dict[int, Pizza] = {
            1: PepperoniPizza(),
            2: BBQPizza(),
            3: SeafoodPizza(),
        }
        self.order: Order | None = None

    def display_menu(self) -> None:
        print("Name", "=" + 80, sep="\n")
        for key, pizza in self.menu.items():
            print(f"key, (pizza.name) - (pizza.price) тенге")

        
    def take_order(self) -> None:
        """заказ от пользователя"""
        self.order = Order()
        while True:
            self.display_menu()
            choice = input(
                "=" * 80
                + "\nвведите номер пиццы (0 для завершения): \n"
                + "=" * 80
                + "\n"
            )
            if choice == "0":
                break
            if choice == "2":
                topping = self.menu[int(choice)].ask_topping()
                self.menu[int(choice)].add_topping(topping)
            if int(choice) in self.menu:
                self.order.add_pizza(self.menu[int(choice)])
                print(f"{self.menu[int(choice)].name}")
            else:
                print("неверный выбор, выберите пиццу из меню")
                continue

    def confirm_order(self) -> bool:
        """пот=дтверждение заказа"""
        if self.order:
            print(f"итого к оплате: {self.order.calculate_total()} тенге")
            if confirmation.lower() == "да":
                print("заказ подтвержден")
                return True
            else:
                print("заказ отменен")
                self.order = None
                return False
        else:
            print("нет заказа для подтверждения")
            return False

    def take_payment(self) -> None:
        """оплата"""
        if self.order:
            print("оплата принята. ваш заказ готовится")
            for pizza in self.order.pizzas:
                pizza.prepare()
                pizza.bake()
                pizza.cut()
                pizza.box()
            print("спасибо за заказ")















        
