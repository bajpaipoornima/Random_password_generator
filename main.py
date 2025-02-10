import random
import string

def generate_password(length=12):
    # Define the character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password includes at least one character from each set
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password with random choices from all characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

# Example usage
password = generate_password()
print("Generated Password:", password)