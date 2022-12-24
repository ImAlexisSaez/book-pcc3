prompt = "\n¿Cuántos años tienes? "
prompt += "\n(Escribe 'salir' para terminar el programa) "

while True:
    edad = input(prompt)

    if edad == 'salir':
        break
    else:
        edad = int(edad)

    if edad <= 3:
        precio = 0
    elif edad <= 12:
        precio = 10
    else:
        precio = 15
    
    print(f"El precio de la entrada es {precio} euros.")
