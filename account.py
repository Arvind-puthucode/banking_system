class A:
    def __init__(self, ac, bal):
        self.ac = ac
        self.bal = bal

    def d(self, amt):
        self.bal += amt

    def w(self, amt):
        if amt <= self.bal:
            self.bal -= amt
        else:
            raise ValueError("Insufficient funds.")

    def db(self):
        print(f"Account {self.ac} balance: ${self.bal}")
