class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"El restaurante {self.restaurant_name} es de cocina",
              f"{self.cuisine_type}.")

    def open_restaurant(self):
        print(f"El restaurante {self.restaurant_name} está abierto.")

valverde = Restaurant('Valverde', 'popular')

print(f"Restaurante: {valverde.restaurant_name}.")
print(f"Tipo de cocina: {valverde.cuisine_type}.")

valverde.describe_restaurant()
valverde.open_restaurant()
