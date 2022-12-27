class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"El restaurante {self.restaurant_name} es de cocina",
              f"{self.cuisine_type}.")

    def open_restaurant(self):
        print(f"El restaurante {self.restaurant_name} está abierto.")
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, number):
        self.number_served += number
    
    def clients_served(self):
        print(f"Clientes atendidos: {self.number_served}")

valverde = Restaurant('Valverde', 'popular')
valverde.clients_served()

valverde.number_served = 12
valverde.clients_served()

valverde.set_number_served(15)
valverde.clients_served()

valverde.increment_number_served(123)
valverde.clients_served()