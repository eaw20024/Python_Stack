class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate 
        self.balance = balance 
        
    def deposit(self, amount):
        self.balance += amount 
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount 
        else:
            self.balance -= 5 
            print("Insufficient Funds: Charging a $5 fee")
        return self

    def display_account_info(self, name):
        print(f"Name: {name}, Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info(self.name)
        return self
    
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount) 
        self.make_withdrawal(amount) 
        return self

eaw = User("Eric Washington", "eric.washington.me@gmail.com").make_deposit(100).make_withdrawal(50).display_user_balance()
