cities = {
    'madrid': {
        'country': 'Spain',
        'population': 6000000,
        'fact': "it's the capital"
    },
    'barcelona': {
        'country': 'Spain',
        'population': 4500000,
        'fact': "it's also known as Warcelona"
    },
    'alicante': {
        'country': 'Spain',
        'population': 500000,
        'fact': "it's where I live"
    }
}

for city, data in cities.items():
    print(f"{city.title()} is a city in {data['country'].title()}.")
    print(f"Its population is {data['population']} and {data['fact']}.\n")