import secrets
import string

PASSWORD_LENGTH = 10


def generate_random_password() -> str:
    chars = string.ascii_letters + string.digits
    generated_password = "".join(secrets.choice(chars) for _ in range(PASSWORD_LENGTH))
    return generated_password
