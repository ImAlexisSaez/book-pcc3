import random

def sorteo(bombo, extracciones):
    premio = []
    for extraccion in range(extracciones):
        bola = random.choice(bombo)
        premio.append(bola)
        bombo.remove(bola)
    return premio

bombo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D"]
ticket = [1, 4, "C", 10]
sorteos = 0
gana_sorteo = False

while not gana_sorteo:
    resultado = sorteo(bombo[:], 4)
    sorteos += 1
    if set(resultado) == set(ticket):
        gana_sorteo = True

print(f"Hemos necesitado {sorteos} sorteos.")