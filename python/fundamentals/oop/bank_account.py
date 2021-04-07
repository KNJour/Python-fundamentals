class  BankAccount:
    def __init__(self, name, int_rate, balance):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient Funds, you have been charged $5")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        self.int_yield = self.balance * self.int_rate
        self.balance += self.int_yield
        return self
        


keith = BankAccount("Keith",.01,100)
bob = BankAccount("Bob",.03, 100 )
keith.deposit(50).deposit(50).deposit(50).withdraw(50).yield_interest().display_account_info()
bob.deposit(100).deposit(50).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()
