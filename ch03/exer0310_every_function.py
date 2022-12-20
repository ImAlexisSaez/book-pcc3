lenguajes = ['español', 'francés', 'inglés', 'valenciano', 'gallego']

print(lenguajes)
print(lenguajes[0])
print(lenguajes[-2])
print(lenguajes[1].title())

lenguajes[2] = 'alemán'
print(lenguajes)

lenguajes.append('inglés')
print(lenguajes)

lenguajes.insert(1, 'holandés')
print(lenguajes)

del lenguajes[0]
print(lenguajes)

lenguajes.pop()
print(lenguajes)

lenguajes.sort()
print(lenguajes)

lenguajes.sort(reverse=True)
print(lenguajes)