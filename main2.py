import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_symbols=True):
    
    characters = list(string.ascii_lowercase)

    if (use_uppercase):
        characters = characters + list(string.ascii_uppercase)
    if (use_numbers):
        characters = characters + list(string.digits)
    if (use_symbols):
        characters = characters + list(string.punctuation)

    if not characters:
        return "No character types selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print( "Password Generator")
try:
    length = int(input("Enter the password length: "))
    if length <= 0:
        print("Length must be positive.")
    
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    print(" Generated Password:", password)
except ValueError as e:
    print("Error:", e)

