# Lista original de invitados:
guests = ['Alexis', 'Ana', 'Rubén', 'Bea']

# Se añaden invitados:
guests.insert(0, 'Marco')
guests.insert(3, 'Juana')
guests.append('Lucas')

# Empiezan las cancelaciones:
print("Únicamente dos personas pueden acudir a la cena.")

print(f"Lo siento, {guests.pop()}. No puedes acudir a la cena.")
print(f"Lo siento, {guests.pop()}. No puedes acudir a la cena.")
print(f"Lo siento, {guests.pop()}. No puedes acudir a la cena.")
print(f"Lo siento, {guests.pop()}. No puedes acudir a la cena.")
print(f"Lo siento, {guests.pop()}. No puedes acudir a la cena.")

print(f"{guests[0]} todavía estás invitado a la cena.")
print(f"{guests[1]} todavía estás invitado a la cena.")

del guests[1]
del guests[0]

print(guests)
