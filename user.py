class G:
    def __init__(self, uid, un, pwd):
        self.ui = uid
        self.un = un
        self.p = pwd

    def a(self, ep):
        return self.p == ep

    def di(self):
        print(f"User ID: {self.ui}, Username: {self.un}")
