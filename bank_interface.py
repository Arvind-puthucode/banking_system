class BankInterface:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, account_number, initial_balance):
        self.bank.create_account(account_number, initial_balance)

    def process_monthly_interest(self):
        self.bank.process_monthly_interest()

    def display_accounts(self):
        self.bank.display_accounts()
