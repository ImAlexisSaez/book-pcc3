rivers = {
    'nile': 'egypt',
    'sena': 'france',
    'tajo': 'spain',
}

for river in rivers.keys():
    print(f"The {river.title()} runs through {rivers[river].title()}.")

print("Rivers mentioned:")
for river in rivers.keys():
    print(f"\t{river.title()}")

print("Countries mentioned:")
for country in rivers.values():
    print(f"\t{country.title()}")