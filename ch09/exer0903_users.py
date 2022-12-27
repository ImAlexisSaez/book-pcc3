class User:
    def __init__(self, first_name, last_name, age, location, nick):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.nick = nick
    
    def describe_user(self):
        print(
            f"El usuario cuyo nick es {self.nick}, se llama",
            f"{self.first_name} {self.last_name}, tiene {self.age}",
            f"años y vive en {self.location}.")
    
    def greet_user(self):
        print(f"¡Buenos días, {self.nick}!")

user_1 = User('Juan', 'Martínez', 19, 'Alcoy', 'Juancho')
user_1.describe_user()
user_1.greet_user()