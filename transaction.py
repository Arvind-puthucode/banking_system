class Transaction:
    def __init__(self, account_number, amount):
        self.account_number = account_number
        self.amount = amount

    def duplicate_process(self, bank):
        # Duplicated code
        account = bank.get_account(self.account_number)
        account.deposit(self.amount)
        print(f"Transaction processed for account {self.account_number}. Amount: ${self.amount}")

    def process(self, bank):
        # Long method
        account = bank.get_account(self.account_number)
        account.deposit(self.amount)
        account.withdraw(self.amount)
        account.display_balance()
        self.duplicate_process(bank)


class DepositTransaction(Transaction):
    def process(self, bank):
        # Override the process method for DepositTransaction
        account = bank.get_account(self.account_number)
        account.deposit(self.amount)
        print(f"Deposit transaction processed for account {self.account_number}. Amount: ${self.amount}")


class WithdrawTransaction(Transaction):
    def process(self, bank):
        # Override the process method for WithdrawTransaction
        account = bank.get_account(self.account_number)
        try:
            account.withdraw(self.amount)
            print(f"Withdrawal transaction processed for account {self.account_number}. Amount: ${self.amount}")
        except ValueError as e:
            print(f"Withdrawal transaction failed for account {self.account_number}: {str(e)}")
