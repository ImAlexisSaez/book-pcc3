comidas = ('tortilla', 'sopa', 'filete', 'bocadillo', 'pizza')

for comida in comidas:
    print(comida.title())

#comidas[0] = 'ensalada' # TypeError

comidas = ('tortilla', 'sopa', 'filete', 'ensalada', 'ensaladilla')
for comida in comidas:
    print(comida.title())