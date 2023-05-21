import hashlib

from settings.settings import ALGORITM, ITERATIONS, SALT


def hash_token(token_: bytes) -> str:
    return hashlib.pbkdf2_hmac(ALGORITM, token_, SALT, ITERATIONS).hex()
