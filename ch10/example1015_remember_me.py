from pathlib import Path
import json

username = input("What's your name? ")

path = Path('ch10/username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"We'll remember you when you come back, {username}!")