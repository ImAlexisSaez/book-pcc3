yuki = {
    'name': 'yuki',
    'kind': 'dog',
    'owner_name': 'Ana',
}

linda = {
    'name': 'linda',
    'kind': 'dog',
    'owner_name': 'Alexis',
}

mushu = {
    'name': 'mushu',
    'kind': 'cat',
    'owner_name': 'Bea',
}

pets = [yuki, linda, mushu]

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['kind']}, and its owner is",
          f"{pet['owner_name']}.")