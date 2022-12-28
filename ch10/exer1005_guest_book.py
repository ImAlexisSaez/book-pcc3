from pathlib import Path

names = []

prompt = "¿Cómo te llamas?"
prompt += "\n(Pulsa 'q' para terminar) "

while True:
    name = input(prompt)
    if name == 'q':
        break
    names.append(name)

contents = "Lista de invitados\n"
for name in names:
    contents += f"\t{name}\n"

path = Path('ch10/guest_book.txt')
path.write_text(contents, encoding='utf-8')