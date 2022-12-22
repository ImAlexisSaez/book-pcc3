current_users = ['juan', 'marta', 'paloma', 'pepe', 'admin']
current_users_copy = current_users[:]

new_users = ['josé', 'juana', 'Marta', 'Pepe', 'tomás']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"¡Lo sentimos! El nombre {new_user} ya está en uso.")
    else:
        print(f"¡Felicidades! El nombre {new_user} está disponible.")

