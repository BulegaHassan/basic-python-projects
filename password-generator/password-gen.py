import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    # Base character set (lowercase letters)
    characters = string.ascii_lowercase
    
    # Add other character sets as requested
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User settings
password_length = int(input("Enter password length: "))
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_special = input("Include special characters? (y/n): ").lower() == 'y'

# Generate and display the password
password = generate_password(password_length, include_uppercase, include_numbers, include_special)
print("Generated password:", password)
