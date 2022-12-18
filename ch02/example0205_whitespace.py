print("Python")

# Con \t insertamos el espaciado de un tabulador
print("\tPython")

# Con \n insertamos nueva lína
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = ' python '
print(favorite_language)
print(favorite_language.lstrip())
print(favorite_language.rstrip())
print(favorite_language.strip())

nostarch_url = 'https://nostarch.com'
print(nostarch_url)
nostarch_url = nostarch_url.removeprefix('https://')
print(nostarch_url)