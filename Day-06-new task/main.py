import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


length = int(input("Enter password length: "))

if length < 4:
    print("Password length should be at least 4.")
else:
    password = generate_password(length)
    print("Generated Password:", password)