def city_function(city, country, population=''):
    if population:
        formatted_string = f"{city}, {country} - Population {population}"
    else:
        formatted_string = f"{city}, {country}"
    return formatted_string.title()