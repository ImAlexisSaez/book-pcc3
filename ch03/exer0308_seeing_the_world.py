destinos = ['valencia', 'barcelona', 'madrid', 'castellón', 'zamora', 'sevilla']

print("\nLista original:")
print(f'\t{destinos}')

print("\nLista ordenada sin afectar la original:")
print(f'\t{sorted(destinos)}')

print("\nLista original:")
print(f'\t{destinos}')

print('\nLista ordenada de manera inversa:')
print(f'\t{sorted(destinos, reverse=True)}')

print("\nLista original:")
print(f'\t{destinos}')

destinos.reverse()
print('\nLista escrita de manera inversa:')
print(f'\t{destinos}')

destinos.reverse()
print("\nLista original:")
print(f'\t{destinos}')

destinos.sort()
print("\nLista ordenada variando la original:")
print(f'\t{destinos}')

destinos.sort(reverse=True)
print('\nLista ordenada de manera inversa, variando la original:')
print(f'\t{destinos}')