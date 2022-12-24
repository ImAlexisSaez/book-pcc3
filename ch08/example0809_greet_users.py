def greet_users(names):
    """Print a simple greeting to each usar in the list."""
    for name in names:
        msg = f"\nHello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)