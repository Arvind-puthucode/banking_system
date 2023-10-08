from bank import C
from atm import B
from savings_account import SA
from current_account import CA
from user import G
from transaction_manager import TM
from bank_interface import BI

if __name__ == "__main__":
    bnk = C("MyBank")
    bi = BI(bnk)

    bi.ca("SA1", 1000)
    bi.ca("CA1", 500)

    user1 = G("U1", "alice123", "password1")
    user2 = G("U2", "bob456", "password2")

    atm = B(bnk)
    tm = TM()

    dt = tm.cdt("SA1", 200)
    atm.p(dt)

    wt = tm.cwt("CA1", 700)
    atm.p(wt)

    bi.da()

    print("Authenticating users:")
    print(user1.a("password1"))  # Should print True
    print(user2.a("wrongpassword"))  # Should print False

    user1.di()
    user2.di()
