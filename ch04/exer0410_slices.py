destinos = ['Barcelona', 'Sevilla', 'Valencia', 'Madrid', 'Alicante']
destinos.append('Castellón')
destinos.append('Valencia')
destinos.append('Toledo')
destinos.append('Cuenca')

print(destinos)

print('Los tres primeros destinos son:')
for destino in destinos[:3]:
    print(f'\t{destino}')

print('Los tres destinos intermedios son:')
for destino in destinos[3:7]:
    print(f'\t{destino}')

print('Los últimos tres destinos son:')
for destino in destinos[-3:]:
    print(f'\t{destino}')