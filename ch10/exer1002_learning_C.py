from pathlib import Path

path = Path('ch10/learning_python.txt')  # Añado la carpeta a la ruta.
contents = path.read_text(encoding='utf-8')  # Ojo al encoding.

for line in contents.splitlines():    
    print(line.replace('Python', 'C'))
