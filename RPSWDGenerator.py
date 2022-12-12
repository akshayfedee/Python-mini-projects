import string
import secrets

def generate_password(length: int) -> str:
    """Generate a random password with the given length, containing
    lowercase letters, uppercase letters, digits, and punctuation symbols.
    """
    # Get the sets of lowercase and uppercase letters, digits, and punctuation symbols
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Create a list of all possible characters
    chars = list(letters + digits + symbols)

    # Use the secrets module to generate a password of the specified length
    password = ''.join(secrets.choices(chars, k=length))
    return password

# Generate a password of 8 characters
password = generate_password(8)
print(password)
