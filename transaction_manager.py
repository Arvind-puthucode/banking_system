from transaction import DepositTransaction, WithdrawTransaction

class TransactionManager:
    @staticmethod
    def create_deposit_transaction(account_number, amount):
        return DepositTransaction(account_number, amount)

    @staticmethod
    def create_withdraw_transaction(account_number, amount):
        return WithdrawTransaction(account_number, amount)
