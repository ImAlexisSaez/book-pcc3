prompt = "\nEnter a number, and I'll tell you if it's even or odd: "
prompt += "\n(Enter 'quit' to end the program) "

number = input(prompt)

while number != 'quit':
    number = int(number)

    if number % 2 == 0:
        print(f"\nThe number {number} is even.")
    else:
        print(f"\nThe number {number} is odd.")
    
    number = input(prompt)


