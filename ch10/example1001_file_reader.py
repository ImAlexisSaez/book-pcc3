from pathlib import Path

path = Path('ch10/pi_digits.txt') # Añado la carpeta a la ruta.
contents = path.read_text()
contents = contents.rstrip()
print(contents)