import random

bombo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D"]
premio = []

for i in range(4):
    bola = random.choice(bombo)
    premio.append(bola)
    bombo.remove(bola)

print(f"El boleto con la combinación {premio} es el ganador.")
