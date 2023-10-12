class Food:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        self.cooking_time = 15

class Burger(Food):
    def __init__(self, name, price, meat, ingredients) -> None:
        super().__init__(name, price)
        self.meat = meat
        self.ingredients = ingredients


class Pizza(Food):
    def __init__(self, name, price, size, toppings) -> None:
        super().__init__(name, price)
        self.size = size
        self.toppings = toppings

class Drinks(Food):
    def __init__(self, name, price, isCold = True) -> None:
        super().__init__(name, price)
        self.isCold = isCold

# composition
class Menu:
    def __init__(self) -> None:
        self.pizzas = []
        self.burgers = []
        self.drinks = []
    
    def add_menu_items(self,item_type,item):
        if item_type == 'pizza':
            self.pizzas.append(item)
        elif item_type == 'burger':
            self.burgers.append(item)
        elif item_type == 'drinks':
            self.drinks.append(item)

    def remove_pizza(self, pizza,burger,drink):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)
        elif drink in self.drinks:
            self.drinks.remove(drink)
        elif burger in self.burgers:
            self.burgers.remove(burger)

    def show_menu(self):
        