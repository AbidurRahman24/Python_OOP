class Bank:
    def __init__(self,balance) -> None:
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount> 0: self.balance += amount

    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print(f"you can't withdraw {self.min_withdraw}")
        elif amount > self.max_withdraw:
            print(f"Bank not allow {self.max_withdraw}")
        else:
            self.balance -= amount
            print(f'Your money {amount}')
            print(f'After withdraw : {self.get_balance()}')


DBBL = Bank(50000)
DBBL.deposit(4323)
DBBL.deposit(4343)
DBBL.withdraw(432)
print(DBBL.get_balance())

