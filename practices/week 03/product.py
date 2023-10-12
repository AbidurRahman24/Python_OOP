class Customer:
    def __init__(self,name,email,password) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.cart = []

    def add_to_cart(self,product):
        self.cart.append(product)
    
    def remove_from_cart(self, product):
        if product in self.cart:
            self.cart.remove(product)
            print(f"{product} removed from your cart.")
        else:
            print(f"{product} is not in your cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for item in self.cart:
                print(item)

    def __str__(self):
        return f"Customer with email: {self.email} {self.name}"

class Seller:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.products = []

    def create_product(self, product_name, price):
        product = Product(product_name, price)
        self.products.append(product)
        return product

    def list_products(self):
        return self.products

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product Name: {self.name}, Price: ${self.price:.2f}"
# Example usage
customer1 = Customer("NIloy","customer1@example.com", "password123")
customer2 = Customer("Sumon","customer2@example.com", "pass456")

# # Adding products to the cart
# customer1.add_to_cart("Product A")
# customer1.add_to_cart("Product B")
# customer2.add_to_cart("Product C")

# # Viewing the cart
# print(f"{customer1}'s cart:")
# customer1.view_cart()

# # Removing a product from the cart
# customer1.remove_from_cart("Product A")

# # Viewing the updated cart
# print(f"{customer1}'s updated cart:")
# customer1.view_cart()
