class BI:
    def __init__(self, bnk):
        self.bnk = bnk

    def ca(self, ac, ib):
        self.bnk.ca(ac, ib)

    def pmi(self):
        self.bnk.pmi()

    def da(self):
        self.bnk.da()
