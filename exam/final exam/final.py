import random
from abc import ABC, abstractmethod

class Bank(ABC):
    accounts=[]
    def __init__(self,name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type

        self.balance = 0
        self.account_number = self.random_ac_number()
        self.transaction_history = []
        Bank.accounts.append(self)

    def random_ac_number(self):
        Bank.ac += 1
        return Bank.ac
    def deposit (self,amount):
        if amount >= 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            print(f"\n--> Deposited {amount}. New balance: ${self.balance}")
        else:
            print("\n--> Invalid deposit amount")
    
    def withdraw(self, amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            print(f"\nWithdrew ${amount}. New balance: ${self.balance}")
        else:
            print("\nWithdrawal amount exceeded")

    @abstractmethod
    def checkBalance(self):
        pass

    def view_transaction_history(self):
        return self.transaction_history
    
