from account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def calculate_interest(self):
        self.balance += self.balance * 0.02  # Add 2% interest
        print(f"Interest calculated for Savings Account {self.account_number}. New balance: ${self.balance}")
