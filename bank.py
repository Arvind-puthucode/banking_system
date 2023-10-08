from account import A
from savings_account import SA
class C:
    def __init__(self, n):
        self.n = n
        self.acc = {}

    def ca(self, ac, ib):
        a = A(ac, ib)
        self.acc[ac] = a

    def ga(self, ac):
        return self.acc.get(ac)

    def da(self):
        print("Accounts:")
        for ac, a in self.acc.items():
            print(f"Account {ac}, Balance: ${a.bal}")

    def pmi(self):
        for ac, a in self.acc.items():
            if isinstance(a, SA):
                a.ci()
