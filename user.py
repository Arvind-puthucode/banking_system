class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

    def authenticate(self, entered_password):
        return self.password == entered_password

    def display_info(self):
        print(f"User ID: {self.user_id}, Username: {self.username}")
