"""
    Bcrypt Password Functions
"""

import bcrypt  # pylint: disable=import-self


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
        Verify Password
    """
    password_byte_enc = plain_password.encode('utf-8')
    hashed_password_byte = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password=password_byte_enc, hashed_password=hashed_password_byte) # pylint: disable=no-member


def hash_password(password: str) -> str:
    """
        Password Hashing
    """
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()  # pylint: disable=no-member
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)  # pylint: disable=no-member
    return hashed_password.decode()
