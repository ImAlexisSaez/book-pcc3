from pathlib import Path

prompt = "¿Cómo te llamas? "

guest = input(prompt)

path = Path('ch10/guest.txt')
path.write_text(guest, encoding='utf-8')