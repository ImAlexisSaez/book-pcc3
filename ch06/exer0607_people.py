person_1 = {
    'first_name': 'Alexis',
    'last_name': 'Sáez',
    'age': 42,
    'city': 'Elche'
}

person_2 = {
    'first_name': 'Ana',
    'last_name': 'Martínez',
    'age': 39,
    'city': 'Elche'
}

person_3 = {
    'first_name': 'Juana',
    'last_name': 'Arco',
    'age': 35,
    'city': 'Elda'
}

people = [person_1, person_2, person_3]

for person in people:
    print(f"Nombre: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"\tEdad: {person['age']}")
    print(f"\tUbicación: {person['city'].title()}")


