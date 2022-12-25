def make_sandwich(*ingredients):
    """Imprime los ingredientes del sandwich."""
    print("\nEl sandwich contiene:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich('atún')
make_sandwich('atún', 'mayonesa')
make_sandwich('tomate', 'jamón', 'aceite')