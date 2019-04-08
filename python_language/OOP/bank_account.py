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

user1 = BankAccount( 0.05, 0)
user2 = BankAccount( 0.08, 0)

user1.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().dispay_account_info()
user2.deposit(300).deposit(200).withdraw(50).withdraw(50).deposit(50).deposit(50).yield_interest().dispay_account_info()