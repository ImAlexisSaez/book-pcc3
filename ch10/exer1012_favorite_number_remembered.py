from pathlib import Path
import json


def get_favorite_number(path):    
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        return favorite_number
    else:
        return None


def ask_favorite_number(path):    
    favorite_number = input("What is your favorite number? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    return favorite_number


def favorite_number():    
    path = Path('ch10/favorite_number.json')

    favorite_number = get_favorite_number(path)

    if favorite_number:
        print(f"Your favorite number is {favorite_number}!")
    else:
        favorite_number = ask_favorite_number(path)
        print(f"Your favorite number is {favorite_number}!")


favorite_number()
