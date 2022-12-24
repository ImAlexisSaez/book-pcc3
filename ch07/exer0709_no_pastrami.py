sandwich_orders = ['pastrami', 'atún', 'pastrami', 'jamón', 'carne', 'queso', 'nocilla']
sandwich_orders.append('pastrami')
sandwich_orders.insert(3, 'pastrami')
sandwich_orders.insert(6, 'pastrami')

print("\nPedidos iniciales:")
print(sandwich_orders)

print("\n¡Lo sentimos, no queda pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\nNuevos pedidos (sin pastrami):")
print(sandwich_orders)