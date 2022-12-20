dato_1, dato_2, opcion = '', '', ''
dato_1_flag, dato_2_flag = True, True
opciones = ['A', 'B', 'C', 'D']

while dato_1_flag:
    dato_1 = input("Introduce el primer número decimal: ")
    try:
        dato_1 = float(dato_1)
        dato_1_flag = False
    except ValueError:
        print("¡El número introducido no es un número decimal!")

while dato_2_flag:
    dato_2 = input("Introduce el segundo número decimal: ")
    try:
        dato_2 = float(dato_2)
        dato_2_flag = False
    except ValueError:
        print("¡El número introducido no es un número decimal!")

while opcion not in opciones:
    print('''\nLas operaciones aritméricas disponibles son:
            \t A: Suma
            \t B: Resta
            \t C: Multiplicación
            \t D: División''')
    opcion = input("¿Qué operación aritmética deseas realizar? ")

if opcion=='A':
    suma = dato_1 + dato_2
    print(f'El resultado de la suma es {suma}.')
elif opcion=='B':
    resta = dato_1 - dato_2
    print(f'El resultado de la resta es {resta}.')
elif opcion=='C':
    prod = dato_1 * dato_2
    print(f'El resultado de la multiplicación es {prod}.')
else:
    cociente = dato_1 / dato_2
    print(f'El resultado de la división es {cociente}.')
