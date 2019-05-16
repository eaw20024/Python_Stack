class BankAccount:
    def __init__(self, int_rate=0, account_balance=0):
        self.int_rate = int_rate
        self.account_balance = account_balance
        
    def deposit(self, amount):
        self.account_balance += amount
        return self
    
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            self.account_balance -= 5
            print("There is not enough money in the account. A $5 fee will be charged to the account")
        return self
    
    def display_account_info(self):
        print("Balance: ${}".format(self.account_balance))
        
    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance = self.account_balance + self.account_balance * self.int_rate
        return self
     

