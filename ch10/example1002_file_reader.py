from pathlib import Path

path = Path('ch10/pi_digits.txt')  # Añado la carpeta a la ruta.
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line.strip())