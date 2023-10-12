class Customer:
    def __init(self, email, password):
        self.email = email
        self.password = password
        self.cart = []

    def add_to_cart(self, product, quantity=1):
        self.cart.append((product, quantity))
        print(f"{quantity} {product.name}(s) added to your cart.")

    def remove_from_cart(self, product, quantity=1):
    # Iterate through items in the cart.
        for item in self.cart:
            # Check if the current item's product matches the one to remove.
            if item[0] == product:
                # If the item's quantity in the cart is greater than or equal to the desired quantity.
                if item[1] >= quantity:
                    # Reduce the item's quantity by the desired quantity.
                    item[1] -= quantity
                    print(f"{quantity} {product.name}(s) removed from your cart.")
                    # If the item's quantity becomes 0, remove the item from the cart.
                    if item[1] == 0:
                        self.cart.remove(item)
                else:
                    # If there's insufficient quantity of the product in the cart.
                    print(f"Insufficient quantity of {product.name} in your cart.")
                return
        # If the product is not found in the cart.
        print(f"{product.name} is not in your cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for product, quantity in self.cart:
                print(f"{quantity} x {product.name}")

    def place_order(self, stock):
        if not self.cart:
            print("Your cart is empty. Add products to your cart before placing an order.")
            return

        order_successful = True
        for product, quantity in self.cart:
            if product not in stock or stock[product] < quantity:
                print(f"{product.name} is out of stock. Order not placed.")
                order_successful = False
                continue
            stock[product] -= quantity

        if order_successful:
            total_price = sum(product.price * quantity for product, quantity in self.cart)
            print(f"Order placed! Total price: ${total_price:.2f}")
            self.cart.clear()

    def __str__(self):
        return f"Customer with email: {self.email}"
# Create sellers
# seller1 = Seller("seller1@example.com", "sellerpass1")
# seller2 = Seller("seller2@example.com", "sellerpass2")

# Create customers
customer1 = Customer("customer1@example.com", "customerpass1")
customer2 = Customer("customer2@example.com", "customerpass2")

# Sellers add products to sell
product1 = seller1.create_product("Product A", 25.99, stock=10)
product2 = seller1.create_product("Product B", 15.49, stock=5)
product3 = seller2.create_product("Product C", 30.00, stock=3)

# Customers view all available products
print("Available Products:")
for seller in [seller1, seller2]:
    for product, stock in seller.list_products().items():
        if stock > 0:
            print(product)

# Customers add products to their carts
customer1.add_to_cart(product1, 2)
customer1.add_to_cart(product2, 1)
customer2.add_to_cart(product3, 2)

# Customers view their carts
print(f"{customer1}'s cart:")
customer1.view_cart()

# Customers place orders
customer1.place_order(seller1.list_products())
customer2.place_order(seller2.list_products())

# View updated stock
print("Updated Stock:")
for seller in [seller1, seller2]:
    for product, stock in seller.list_products().items():
        print(product)

# Customers view their carts after ordering
print(f"{customer1}'s updated cart:")
customer1.view_cart()