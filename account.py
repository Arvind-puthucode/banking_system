class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds.")

    def display_balance(self):
        # Duplicated code
        print(f"Account {self.account_number} balance: ${self.balance}")
        print(f"Account {self.account_number} balance: ${self.balance}")
