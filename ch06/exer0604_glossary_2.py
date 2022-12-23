glossary = {
    'bucle': 'Herramienta para repetir.',
    'condicional': 'Herramienta para decidir.',
    'IDE': 'Herramienta para escribir código y compilar.',
    'print()': 'Función para imprimir mensajes en la terminal.',
    'f-string': 'Cadena de texto con posibilidad de incluir variables.',
}

print('Glosario de términos:')
for word in glossary.keys():
    print(f"\t{word}: {glossary[word]}")