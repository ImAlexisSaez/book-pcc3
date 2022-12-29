from city_function import city_function

def test_city_country():
    formatted_string = city_function('santiago', 'chile')
    assert formatted_string == "Santiago, Chile"

def test_city_country_population():
    formatted_string = city_function('santiago', 'chile', 5000000)
    assert formatted_string == "Santiago, Chile - Population 5000000"