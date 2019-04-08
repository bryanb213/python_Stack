class BankAccount:
    def __init__(self, interest_rate, balance=0 ):
        self.interest = interest_rate
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        self.account_balance  -= amount
        return self

    def dispay_account_info(self):
        print('Balance:', self.account_balance,'$')
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance = self.account_balance + (self.account_balance * self.interest)
        return self

class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(interest_rate=0.01, balance=0)
        

    def make_deposit(self, amount):
        self.account.account_balance += amount
        return self
        

    def make_withdrawl(self, amount):
        self.account.account_balance -= amount
        return self
    

    def display_user_balance(self):
        print(self.name, 'has', self.account.account_balance, 'dollars')
        return self


user_1 = User('Bob', 'skfg@msn.com')
user_2 = User('Bill', 'jf@msn.com')
user_3 = User('Moe', 'moe@msn.com')

user_1.make_deposit(100).make_deposit(100).make_withdrawl(50).display_user_balance()

user_2.make_deposit(100).make_deposit(100).make_withdrawl(50).make_withdrawl(50).display_user_balance()

user_3.make_deposit(200).make_withdrawl(50).make_withdrawl(50).make_withdrawl(50).display_user_balance()
