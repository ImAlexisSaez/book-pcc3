cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# Con sorted() no modificamos la lista original
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nLista original:")
print(cars)

print("\nLista ordenada:")
print(sorted(cars))

print("\nLista original:")
print(cars)

# .reverse() da la vuelta a la lista. Cuidado, no ordena en sentido inverso.
cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse()
print("\nLista invertida:")
print(cars)

print("\nLista original:")
cars.reverse()
print(cars)

# len() permite calcular la longitud de una lista:
print(len(cars))