prompt = "\nIntroduce un ingrediente para la pizza: "
prompt += "\n(Escribe 'salir' para terminar) "

active = True

while active:
    ingrediente = input(prompt)

    if ingrediente == 'salir':
        active = False
    else:
        print(f"¡Añadiendo {ingrediente.lower()} a la pizza!")

print(f"Pedido finalizado.")