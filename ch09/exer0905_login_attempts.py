class User:
    def __init__(self, first_name, last_name, age, location, nick):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.nick = nick
        self.login_attempts = 0

    def describe_user(self):
        print(
            f"El usuario cuyo nick es {self.nick}, se llama",
            f"{self.first_name} {self.last_name}, tiene {self.age}",
            f"años y vive en {self.location}.")

    def greet_user(self):
        print(f"¡Buenos días, {self.nick}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    
    def print_login_attempts(self):
        print(
            f"Número de intentos de acceso del usuario {self.nick}:", 
            f"{self.login_attempts}.")


user_1 = User('Juan', 'Martínez', 19, 'Alcoy', 'Juancho')

for i in range(30):
    user_1.increment_login_attempts()

user_1.print_login_attempts()

user_1.reset_login_attempts()
user_1.print_login_attempts()