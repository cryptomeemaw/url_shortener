import secrets
import string

ALPHABET = string.ascii_letters + string.digits

def generate_code(length: int) -> str:
    characters = []
    for _ in range(length):
        characters.append(secrets.choice(ALPHABET))
    return "".join(characters)