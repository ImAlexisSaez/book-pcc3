favorite_numbers = {
    'Alexis': [5, 6, 7],
    'Ana': [7, 10, 13],
    'Carmen': [13, 15, 21],
    'Juan': [15, 35, 53], 
    'Pepe': [21, 25, 35, 112],
}

for name, numbers in favorite_numbers.items():
    print(f"Los números favoritos de {name} son:")
    for number in numbers:
        print(f"\t{number}")