from pathlib import Path
import json

favorite_number = input("¿Cuál es tu número favorito? ")

path = Path('ch10/favorite_number.json')
contents = json.dumps(favorite_number)
path.write_text(contents)