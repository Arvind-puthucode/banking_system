from account import A

class CA(A):
    def __init__(self, ac, bal):
        super().__init__(ac, bal)

    def w(self, amt):
        self.bal -= amt
        print(f"Withdrawal from Current Account {self.ac}. New balance: ${self.bal}")
