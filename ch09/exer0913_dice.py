import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        print(random.randint(1, self.sides))

print("Dado de 6 caras:")
dado_6 = Dice()
[dado_6.roll_die() for roll in range(10)]

print("\nDado de 10 caras:")
dado_10 = Dice(10)
[dado_10.roll_die() for roll in range(10)]

print("\nDado de 20 caras:")
dado_20 = Dice(20)
[dado_20.roll_die() for roll in range(10)]