def describe_city(city, country='españa'):
    """Describe dónde está una ciudad."""
    print(f"{city.title()} está en {country.title()}")

describe_city('Barcelona')
describe_city(city='madrid')
describe_city('paris')