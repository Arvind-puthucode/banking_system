from abc import ABC, abstractmethod

class D(ABC):
    def __init__(self, ac, amt):
        self.ac = ac
        self.amt = amt

    def dp(self, bnk):
        a = bnk.ga(self.ac)
        a.d(self.amt)
        print(f"Transaction processed for account {self.ac}. Amount: ${self.amt}")

    def p(self, bnk):
        a = bnk.ga(self.ac)
        a.d(self.amt)
        a.w(self.amt)
        a.db()
        self.dp(bnk)


class E(D):
    def p(self, bnk):
        a = bnk.ga(self.ac)
        a.d(self.amt)
        print(f"Deposit transaction processed for account {self.ac}. Amount: ${self.amt}")


class F(D):
    def p(self, bnk):
        a = bnk.ga(self.ac)
        try:
            a.w(self.amt)
            print(f"Withdrawal transaction processed for account {self.ac}. Amount: ${self.amt}")
        except ValueError as e:
            print(f"Withdrawal transaction failed for account {self.ac}: {str(e)}")
