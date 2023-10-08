from account import Account
from savings_account import SavingsAccount
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        account = Account(account_number, initial_balance)
        self.accounts[account_number] = account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def display_accounts(self):
        print("Accounts:")
        for account_number, account in self.accounts.items():
            print(f"Account {account_number}, Balance: ${account.balance}")

    def process_monthly_interest(self):
        for account_number, account in self.accounts.items():
            if isinstance(account, SavingsAccount):
                account.calculate_interest()

    def process_transactions(self):
        # Large class and Long method
        for account_number, account in self.accounts.items():
            account.deposit(100)
            account.withdraw(50)
            account.display_balance()
            account.deposit(200)
            account.withdraw(100)
            account.display_balance()
