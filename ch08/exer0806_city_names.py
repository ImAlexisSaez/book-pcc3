def city_country(city, country):
    """Devuelve una cadena de texto con la ciudad y el país."""
    return f'"{city.title()}, {country.title()}"'

print(city_country('Barcelona', 'españa'))
print(city_country('madrid', 'españa'))
print(city_country('paris', 'francia'))