class Customer:
  def __init__(self, email, password, first_name, last_name):
    self.email = email
    self.password = password
    self.first_name = first_name
    self.last_name = last_name

  def create_account(self):
    pass

class Seller:
  def __init__(self, email, password, first_name, last_name):
    self.email = email
    self.password = password
    self.first_name = first_name
    self.last_name = last_name
    self.products = []

  def create_account(self):
    pass

  def publish_product(self, product):
    self.products.append(product)

class Product:
  def __init__(self, name, description, price, quantity_in_stock):
    self.name = name
    self.description = description
    self.price = price
    self.quantity_in_stock = quantity_in_stock

class EShoppingApp:
  def __init__(self):
    self.customers = []
    self.sellers = []
    self.products = []

  def add_customer(self, customer):
    self.customers.append(customer)

