class User:
    """A class to model users."""

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        self.full_name = f"{self.first_name} {self.last_name}"
        print(f"\n{self.full_name.title()} is {self.age} years old and lives in {self.location.title()}.")

    def greet_user(self):
        print(f"Hello, {self.full_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def show_login_attempts(self):
        print(f"\nYou have been logged in for {self.login_attempts} times.")