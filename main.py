from bank import Bank
from atm import ATM
from savings_account import SavingsAccount
from current_account import CurrentAccount
from user import User
from transaction_manager import TransactionManager
from bank_interface import BankInterface

if __name__ == "__main__":
    bank = Bank("MyBank")
    bank_interface = BankInterface(bank)

    # Create different types of accounts
    bank_interface.create_account("SA1", 1000)
    bank_interface.create_account("CA1", 500)

    # Create users
    user1 = User("U1", "alice123", "password1")
    user2 = User("U2", "bob456", "password2")

    # Perform transactions
    atm = ATM(bank)
    transaction_manager = TransactionManager()

    deposit_transaction = transaction_manager.create_deposit_transaction("SA1", 200)
    atm.perform_transaction(deposit_transaction)

    withdraw_transaction = transaction_manager.create_withdraw_transaction("CA1", 700)
    atm.perform_transaction(withdraw_transaction)

    # Display account information
    bank_interface.display_accounts()

    # Authenticate users
    print("Authenticating users:")
    print(user1.authenticate("password1"))  # Should print True
    print(user2.authenticate("wrongpassword"))  # Should print False

    # Display user information
    user1.display_info()
    user2.display_info()
