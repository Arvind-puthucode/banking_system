from bank import Bank
from atm import ATM
from savings_account import SavingsAccount
from current_account import CurrentAccount
from user import User
from transaction import DepositTransaction, WithdrawTransaction

if __name__ == "__main__":
    bank = Bank("MyBank")

    # Create different types of accounts
    bank.create_account("SA1", 1000)
    bank.create_account("CA1", 500)

    # Create users
    user1 = User("U1", "alice123", "password1")
    user2 = User("U2", "bob456", "password2")

    # Perform transactions
    atm = ATM(bank)
    atm.perform_transaction(DepositTransaction("SA1", 200))
    atm.perform_transaction(WithdrawTransaction("CA1", 700))

    # Display account information
    bank.display_accounts()

    # Authenticate users
    print("Authenticating users:")
    print(user1.authenticate("password1"))  # Should print True
    print(user2.authenticate("wrongpassword"))  # Should print False

    # Display user information
    user1.display_info()
    user2.display_info()
