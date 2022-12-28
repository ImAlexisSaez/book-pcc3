from pathlib import Path

cats = Path('ch10/cats.txt')
dogs = Path('ch10/dogs.txt')

try:
    cats_contents = cats.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"El archivo {cats} no existe.")
else:
    print(cats_contents)

try:
    dogs_contents = dogs.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"El archivo {dogs} no existe.")
else:
    print(dogs_contents)

