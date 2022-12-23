total_people = input("How many people are in your dinner group? ")
total_people = int(total_people)

if total_people > 8:
    print("You'll have to wait for a table")
else:
    print("Your table is ready")