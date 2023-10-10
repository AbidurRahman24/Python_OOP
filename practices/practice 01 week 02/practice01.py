class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Shop:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_product(self, name, price, quantity):
        # Create an instance of the Product class and add it to the cart
        product = Product(name, price, quantity)
        self.cart.append(product)

    def buy_product(self, item, quantity=1):
        for product in self.cart:
            if product.name == item:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    return f"Congratulations! You bought {quantity} {item}(s)."
                else:
                    return f"Sorry, {item} is not available in the required quantity."
        return f"Sorry, {item} is not available in our shop."

# Example usage:
my_shop = Shop('My Shop')
my_shop.add_product('Widget', 10.99, 5)

# Buy products
print(my_shop.buy_product('Widget', 2))  # Successful purchase
print(my_shop.buy_product('Widget', 6))  # Not enough quantity available
print(my_shop.buy_product('Gadget', 1))   # Product not available
