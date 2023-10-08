from transaction import E, F

class TM:
    @staticmethod
    def cdt(ac, amt):
        return E(ac, amt)

    @staticmethod
    def cwt(ac, amt):
        return F(ac, amt)
