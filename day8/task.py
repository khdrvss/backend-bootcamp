class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def show_info(self):
        print(f"Your username is {self.username} and your email is {self.email}")

s1 = User("maymun", "said@gmail.com")

s2 = User("chort", "azik@gmail.com")


s1.show_info()
s2.show_info()
