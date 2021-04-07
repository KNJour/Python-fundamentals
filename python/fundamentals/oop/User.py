
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

guido = User("guido", "gg@code.com")
keith = User("Keith", "KN@gmail.com")
bob = User("Bob", "Bob@bob.bob")

guido.make_deposit(100)
print(guido.account_balance)

guido.make_withdrawal(50)
print(guido.account_balance)

guido.dispay_user_balance(guido)