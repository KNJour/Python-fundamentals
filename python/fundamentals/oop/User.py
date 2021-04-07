
class User:
    def __init__(self, name, email):
        self.name = name 
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.account_balance)

    def transfer_money(self,target,amount):
        self.make_withdrawal(amount)
        target.make_deposit(amount)
        print(f"your balance is now {self.account_balance}")
        print(f"their balance is now {target.account_balance}")

guido = User("guido", "gg@code.com")
keith = User("Keith", "KN@gmail.com")
bob = User("Bob", "Bob@bob.bob")

guido.make_deposit(100)
guido.make_deposit(50)
guido.make_deposit(250)
guido.make_withdrawal(50)
guido.display_user_balance()

keith.make_deposit(100)
keith.make_deposit(300)
keith.make_withdrawal(200)
keith.make_withdrawal(150)
keith.display_user_balance()

bob.make_deposit(100)
bob.make_withdrawal(300)
bob.make_withdrawal(200)
bob.make_withdrawal(150)
bob.display_user_balance()

guido.transfer_money(keith, 100)