def send_messages(messages, messages_sent):
    """Imprime mensajes de una lista y los mueve a otra."""
    while messages:
        msg = messages.pop()
        print(msg)
        messages_sent.append(msg)

messages = ['Hola', 'Adiós', '¡Hasta pronto!', 'Saludos']
messages_sent = []

send_messages(messages[:], messages_sent)

print("\nLista de mensajes por enviar: ")
print(messages)

print("\nLista de mensajes enviados: ")
print(messages_sent)