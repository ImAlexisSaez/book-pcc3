pizzas = ['Carbonara', 'Hawaiana', 'Americana']
friend_pizzas = pizzas[:]

pizzas.append('Cuatro quesos')
friend_pizzas.append('Jamón')

print('Mis pizzas favoritas son:')
for pizza in pizzas:
    print(f'\t{pizza}')

print('Las pizzas favorias de mi amigo son:')
for pizza in friend_pizzas:
    print(f'\t{pizza}')