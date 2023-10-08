class ATM:
    def __init__(self, bank):
        self.bank = bank

    def perform_transaction(self, transaction):
        transaction.process(self.bank)
