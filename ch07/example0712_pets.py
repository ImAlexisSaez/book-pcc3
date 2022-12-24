pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

pets_set = set(pets)
print(pets_set)

while 'cat' in pets:
    pets.remove('cat')

print(pets)