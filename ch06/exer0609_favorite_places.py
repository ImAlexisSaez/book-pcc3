favorite_places = {
    'ana': ['Alicante', 'Castellón', 'Valencia'],
    'juan': ['Madrid', 'Barcelona', 'Valencia'],
    'marta': ['Sevilla', 'León'],
    'pepe': ['Valladolid'],
}

for name in favorite_places.keys():
    print(f"Para {name}, sus ciudades favoritas son:")
    print(f"\t{favorite_places[name]}\n")