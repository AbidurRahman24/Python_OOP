class Customer:
  def __init__(self, email, password, first_name, last_name):
    self.email = email
    self.password = password
    self.first_name = first_name
    self.last_name = last_name

  def create_account(self):
    pass

class EShoppingApp:
  def __init__(self):
    self.customers = []
    self.products = []

  def add_customer(self, customer):
    self.customers.append(customer)

  def create_new_account(self, email, password, first_name, last_name):
    customer = Customer(email, password, first_name, last_name)
    customer.create_account()
    self.add_customer(customer)

  def login(self, email, password):
    for customer in self.customers:
      if customer.email == email and customer.password == password:
        return customer

  def browse_products(self):
    return self.products

  def add_product_to_cart(self, product):
    pass

  def checkout(self):
    pass

# Create a new EShoppingApp object
eshopping_app = EShoppingApp()

# Create a new customer account
eshopping_app.create_new_account("customer@example.com", "password", "John", "Doe")

# Login as the customer
customer = eshopping_app.login("customer@example.com", "password")

# Browse the products
products = eshopping_app.browse_products()

# Add a product to the customer's shopping cart
eshopping_app.add_product_to_cart(products[0])

# Checkout
eshopping_app.checkout()
