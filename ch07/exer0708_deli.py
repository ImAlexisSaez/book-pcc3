sandwich_orders = ['atún', 'jamón', 'carne', 'queso', 'nocilla']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I made your {sandwich} sandwich!")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(sandwich)