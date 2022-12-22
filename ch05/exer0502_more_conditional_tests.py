print("Alexis" == "alexis")
print("Alexis" != "alexis")

print("Alexis".lower() == "alexis".lower())
print("Alexis".lower() != "alexis".lower())

print(12 < 13)
print(12 < 7)
print(12 >= 13)
print(12 > 7)

print((1 < 2) and (3<= 10))
print((15 > 7) or (7 > 10))

destinos = ['Granada', 'Alicante', 'Valencia']

destino = 'Granada'
if destino in destinos:
    print('La ciudad está en la lista.')

destino = 'Castellón'
if destino not in destinos:
    print('La ciudad no está en la lista.')
