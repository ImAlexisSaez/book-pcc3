print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Una de las respuestas instroducidas no era un valor numérico.")
    else:
        print(answer)
