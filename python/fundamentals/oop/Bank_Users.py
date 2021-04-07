
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


class User:
    def __init__(self, name, email, interest, startingFund):
        self.name = name 
        self.email = email
        g = interest
        h = startingFund
        self.account = BankAccount(name = "account 1", int_rate = g, balance = h)
        self.account2 = BankAccount(name = "account 2", int_rate = 0.02, balance = 0)
    def make_deposit(self, amount):
        i = input("which account would you like to deposit, 1 or 2?")
        if i == 1:
            self.account.deposit(amount)
        elif i == 2:
            self.account2.deposit(amount)
        return self

    def make_withdraw(self, amount):
        i = input("which account would you like to withdraw, 1 or 2?")
        if i == "1":
            self.account.withdraw(amount)
        elif i == "2":
            self.account2.withdraw(amount)
        return self


    def display_user_balance(self):
        i = input("which account would you like to view? 1 or 2?")
        if i == "1":
            print(self.account.balance)
        elif i == "2":
            print(self.account2.balance)
        return self

    def transfer_money(self,target,amount):
        self.make_withdraw(amount)
        target.make_deposit(amount)
        print(f"your balance is now {self.account_balance}")
        print(f"their balance is now {target.account_balance}")

# keith = User("Keith", "KJ@dojo.com")

# keith.make_deposit(50)
# keith.make_withdraw(25)
# keith.display_user_balance()

def makeAccount():
    accountUser = input("let's make an account. Whats your name?")
    accountEmail = input("what's your email?")
    accountInterest = input("what % interest rate do you want? Don't include the symbol because youll break it")
    accountInterest = int(accountInterest) * .01
    userBalance = input("how much money would you like to open the account with?")
    userBalance = int(userBalance)

    user1 = User(f"{accountUser}", f"{accountEmail}", f"{accountInterest}", f"{userBalance}")

    print("What would you like to do?")
    p = ""
    while p != 4:
        p = input("1 -- Deposit, 2 -- Withdraw, 3 -- View Balance, 4 -- Exit")
        p = int(p)
        if p == 1:
            money = input("how much would you like to deposit?")
            money = int(money)
            user1.make_deposit(money)
        elif p == 2:
            money = input("how much would you like to withdraw?")
            money = int(money)
            user1.make_withdraw(money)
        elif p == 3:
            user1.display_user_balance()

        elif p == 4:
            print("thank you, have a nice day")
            break
        else:
            continue
makeAccount()



        