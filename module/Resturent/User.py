from abc import ABC,abstractmethod

class User:
    def __init__(self,name,phone,email,address) -> None:
        self.name = name
        self.phone = phone
        self.email =email 
        self.address = address
    
class Customer(User):
    def __init__(self, name, phone, email, address,money) -> None:
        super().__init__(name, phone, email, address)
        self.wallet = money
        self.__order = None
        self.due = 0

    @property
    def order(self):
        self.__order
    
    @order.setter
    def order(self, order):
        self.__order = order
    
    def place_order(self,order):
        self.order = order
        self.due_amount += order.bill
        print(f'{self.name} placed an order with bill {order.bill}')
    
    def eat_food(self, order):
        print(f'{self.name} item food {order.items}')
    
    def pay_for_order(self, amount):
        # TODO: submit the money to the manager
        pass

    def give_tips(self, tips_amount):
        pass

    def write_review(self, stars):
        pass

class Employee(User):
    def __init__(self, name, phone, email, address,salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.due = salary
        self.starting_date = starting_date
        self.department = department

    def receive_selary(self):
        self.due = 0
    
class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department,cooking_item) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        self.cooking_time = cooking_item
class server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        self.tips_earning = 0
    
    def take_order(self, order):
        pass

    def transfer_order(self, order):
        pass

    def serve_food(self, order):
        pass

    def receive_tips(self,amount):
        self.tips_earning += amount

class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)