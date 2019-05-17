class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0 
        
    def deposit(self, amount):
        self.account_balance += amount
        return self
    
    def withdraw(self, amount):
        self.account_balance -= amount
        return self
    
    def transfer_money(self, other_user, amount):
        other_user.deposit(amount)
        self.withdraw(amount)
        return self
    
    def display_user_information(self):
        print("User: {}, Email-Address: {}, Account-Balance: ${}".format(self.name, self.email, self.account_balance))
        
eaw = User("Eric Washington", "eric.washington.me@gmail.com").deposit(100).deposit(900).withdraw(999).display_user_information()
