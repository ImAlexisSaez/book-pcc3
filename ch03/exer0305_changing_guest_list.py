guests = ['Alexis', 'Ana', 'Rubén', 'Bea']

print("La lista de invitados inicial era:\n")
print(guests)
print(f"\nPero finalmente, {guests[2].title()} no puede asistir.")

guests[2] = 'Marco'

print(f"\nSe invitará a {guests[2].title()} en su lugar. De manera que:")

print(f"\t - {guests[0].title()}, ¡te esperamos el próximo miércoles para cenar!")
print(f"\t - {guests[1].title()}, ¡te esperamos el próximo miércoles para cenar!")
print(f"\t - {guests[2].title()}, ¡te esperamos el próximo miércoles para cenar!")
print(f"\t - {guests[3].title()}, ¡te esperamos el próximo miércoles para cenar!")