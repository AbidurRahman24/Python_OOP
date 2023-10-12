import random

class Customer:
    def __init__(self, email, password):
        self.customer_id = random.randint(1000, 9999)
        self.email = email
        self.password = password
        self.cart = []

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.cart.append({"product": product, "quantity": quantity})
            product.reduce_stock(quantity)
            print(f"{quantity} {product.name}(s) added to your cart.")
        else:
            print(f"Sorry, {product.name} is out of stock.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for item in self.cart:
                product = item["product"]
                quantity = item["quantity"]
                print(f"{product.name} - ${product.price} x {quantity}")

    def checkout(self):
        if not self.cart:
            print("Your cart is empty. Add items to your cart before checking out.")
        else:
            total_price = sum(item["product"].price * item["quantity"] for item in self.cart)
            print(f"Total price: ${total_price}")
            print("Checkout successful. Thank you for shopping with us!")
            self.cart = []  # Empty the cart after checkout


class Seller:
    def __init__(self, email, password):
        self.seller_id = random.randint(1000, 9999)
        self.email = email
        self.password = password
        self.products = []

    def publish_product(self, name, price, stock):
        product = Product(name, price, stock)
        self.products.append(product)
        print(f"{name} has been published for sale.")

    def view_products(self):
        if not self.products:
            print("No products available for sale.")
        else:
            print("Available products:")
            for product in self.products:
                if product.stock > 0:
                    print(f"{product.name} - ${product.price} (In Stock: {product.stock})")


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        self.stock -= quantity


# Sample sellers and products
seller1 = Seller("seller1@example.com", "sellerpassword")
seller2 = Seller("seller2@example.com", "sellerpassword")

seller1.publish_product("Smartphone", 699.99, 10)
seller1.publish_product("Laptop", 1199.99, 5)
seller2.publish_product("Headphones", 99.99, 8)

# Main program
if __name__ == "__main__":
    print("Welcome to the e-shopping app!")

    while True:
        print("\nMenu:")
        print("1. Customer Login")
        print("2. Seller Login")
        print("3. Exit")
        choice = input("Please select an option: ")

        if choice == "1":
            # Customer login
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            customer = Customer(email, password)
            print(f"Customer account created with ID: {customer.customer_id}")

            while True:
                print("\nCustomer Menu:")
                print("1. Add a product to the cart")
                print("2. View the cart")
                print("3. Checkout")
                print("4. Logout")
                customer_choice = input("Select an option: ")

                if customer_choice == "1":
                    seller1.view_products()
                    seller2.view_products()
                    product_name = input("Enter the name of the product to add to the cart: ")
                    quantity = int(input("Enter the quantity: "))
                    for seller in [seller1, seller2]:
                        for product in seller.products:
                            if product.name == product_name:
                                customer.add_to_cart(product, quantity)
                elif customer_choice == "2":
                    customer.view_cart()
                elif customer_choice == "3":
                    customer.checkout()
                elif customer_choice == "4":
                    print("Logging out.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "2":
            # Seller login
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            for seller in [seller1, seller2]:
                if seller.email == email and seller.password == password:
                    print(f"Seller account created with ID: {seller.seller_id}")

                    while True:
                        print("\nSeller Menu:")
                        print("1. Publish a product for sale")
                        print("2. View published products")
                        print("3. Logout")
                        seller_choice = input("Select an option: ")

                        if seller_choice == "1":
                            name = input("Enter product name: ")
                            price = float(input("Enter product price: "))
                            stock = int(input("Enter initial stock: "))
                            seller.publish_product(name, price, stock)
                        elif seller_choice == "2":
                            seller.view_products()
                        elif seller_choice == "3":
                            print("Logging out.")
                            break
                        else:
                            print("Invalid choice. Please try again.")
                    break
            else:
                print("Seller not found. Please try again.")
        elif choice == "3":
            print("Thank you for using the e-shopping app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
