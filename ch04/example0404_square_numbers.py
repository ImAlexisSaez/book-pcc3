squares = []

for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

# Mismo código sin vairable temporal
squares = []

for value in range(1,11):
    squares.append(value**2)

print(squares)

digits = list(range(10))
print(digits)

print(min(digits))
print(max(digits))
print(sum(digits))

# Usando list comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)