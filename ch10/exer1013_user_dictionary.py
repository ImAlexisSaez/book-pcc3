from pathlib import Path
import json


def get_stored_user(path):    
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None


def get_new_user(path):
    user = {}
    username = input("What is your username? ")
    nick = input("What's your nick? ")
    age = input("What's your age?")
    user['username'] = username
    user['nick'] = nick
    user['age'] = age
    contents = json.dumps(user)
    path.write_text(contents)
    return user


def greet_user():
    """Greet the user by name."""
    path = Path('ch10/username_exer.json')

    user = get_stored_user(path)

    if user:
        current_user = input(f"Are you {user['nick']}? (y / n) ")
        if current_user == 'y':
            print(
                f"Welcome back, {user['nick']}! Your username is {user['username']}",
                f"and your age is {user['age']}."
            )
        else:
            user = get_new_user(path)
            print(f"We'll remember you when you come back, {user['nick']}!")
    else:
        user = get_new_user(path)
        print(f"We'll remember you when you come back, {user['nick']}!")


greet_user()
