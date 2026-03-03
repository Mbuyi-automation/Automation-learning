import json


class User:
    def __init__(self, username, password):
        if not username or not password:
            raise ValueError("Username and password cannot be empty")
        self.username = username
        self.password = password

    def login(self):
        if self.username == "admin" and self.password == "1234":
            return "Login successful"
        else:
            return "Login failed"


if __name__ == "__main__":
    try:
        with open("users.json") as file:
            data = json.load(file)

        username = data["valid_user"]["username"]
        password = data["valid_user"]["password"]

        user = User(username, password)
        print(user.login())

    except ValueError as e:
        print("Error:", e)