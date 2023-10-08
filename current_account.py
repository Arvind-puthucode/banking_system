from account import Account

class CurrentAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawal from Current Account {self.account_number}. New balance: ${self.balance}")
