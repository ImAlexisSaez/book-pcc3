# Inicializo los datos como strings
dato_1 = ''
dato_2 = ''
opcion = ''
opciones = ['A', 'B', 'C', 'D']

# Mientras dato_1 no sea natural:
while not dato_1.isnumeric():
    dato_1 = input("\nIntroduce el primer número natural: ")

# Mientras dato_2 no sea natural:
while not dato_2.isnumeric():
    dato_2 = input("\nIntroduce el segundo número natural: ")

# Mientras no selecciones una opción de las indicadas:
while opcion not in opciones:
    print('''\nLas operaciones aritméricas disponibles son:
            \t A: Suma
            \t B: Resta
            \t C: Multiplicación
            \t D: División''')
    opcion = input("¿Qué operación aritmética deseas realizar? ")

if opcion=='A':
    suma = int(dato_1) + int(dato_2)
    print(f'El resultado de la suma es {suma}.')
elif opcion=='B':
    resta = int(dato_1) - int(dato_2)
    print(f'El resultado de la resta es {resta}.')
elif opcion=='C':
    prod = int(dato_1) * int(dato_2)
    print(f'El resultado de la multiplicación es {prod}.')
else:
    cociente = int(dato_1) / int(dato_2)
    print(f'El resultado de la división es {cociente}.')
