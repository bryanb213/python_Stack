class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
        

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
        

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    

    def display_user_balance(self):
        print(self.name, 'has', self.account_balance, 'dollars')
        return self
        

user_1 = User('Bob', 'skfg@msn.com')
user_2 = User('Bill', 'jf@msn.com')
user_3 = User('Moe', 'moe@msn.com')

user_1.make_deposit(100).make_deposit(100).make_withdrawl(50).display_user_balance()

user_2.make_deposit(100).make_deposit(100).make_withdrawl(50).make_withdrawl(50).display_user_balance()

user_3.make_deposit(200).make_withdrawl(50).make_withdrawl(50).make_withdrawl(50).display_user_balance()

