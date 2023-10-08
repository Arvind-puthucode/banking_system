from account import A

class SA(A):
    def __init__(self, ac, bal):
        super().__init__(ac, bal)

    def ci(self):
        self.bal += self.bal * 0.02
        print(f"Interest calculated for Savings Account {self.ac}. New balance: ${self.bal}")
