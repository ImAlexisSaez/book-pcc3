from pathlib import Path

path = Path('ch10/pi_million_digits.txt')  # Añado la carpeta a la ruta.
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''

for line in lines:
    pi_string += line.lstrip()

prompt = "¿Cuándo es tu cumpleaños?"
prompt += "\nIntroduce la fecha en la forma ddmmyy: "

birthday = input(prompt)

if birthday in pi_string:
    print("Tu cumpleaños aparece en el primer millón de dígitos de pi.")
else:
    print("Tu cumpleaños no aparece en el primer millón de digitos de pi.")
