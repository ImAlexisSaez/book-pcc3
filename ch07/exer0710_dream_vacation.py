respuestas = {}

flag_encuesta = True

while flag_encuesta:
    nombre = input("\n¿Cómo te llamas? ")
    destino = input("\n¿Dónde te gustaría ir de vacaciones? ")

    respuestas[nombre] = destino

    continua = input("\n¿Hay más personas a quien preguntar? (S / N) ")
    if continua == 'N':
        flag_encuesta = False

print("\n--- Resultados de la encuesta ---")
for nombre, destino in respuestas.items():
    print(f"A {nombre.title()} le gustaría ir de vacaciones a {destino.title()}.")