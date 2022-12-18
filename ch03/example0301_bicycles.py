# Las listas conviene nombrarlas en plural, pues suelen tener varios elementos.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Primer elemento:
print(bicycles[0])

print(bicycles[0].title())

print(bicycles[1].upper())
print(bicycles[3].strip())

# Accediendo por el final
print(bicycles[-1].title())

# Escribiendo mensajes:
mensaje = f"Mi primera bicicleta fue de la marca {bicycles[1].title()}."
print(mensaje)