import os
from cryptography.fernet import Fernet

KEY_FILENAME = 'secret.key'
KEY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', KEY_FILENAME)

def load_key():
    """
    Load the symmetric encryption key from file.
    Generates a new key if file does not exist or is invalid.
    """
    if not os.path.exists(KEY_PATH):
        key = Fernet.generate_key()
        try:
            with open(KEY_PATH, 'wb') as key_file:
                key_file.write(key)
        except IOError as e:
            raise Exception(f"Failed to write encryption key: {e}")
    else:
        try:
            with open(KEY_PATH, 'rb') as key_file:
                key = key_file.read()
            # Validate key by creating a Fernet instance
            Fernet(key)
        except Exception:
            # Key invalid, regenerate
            print("⚠️ Invalid key detected. Regenerating...")
            key = Fernet.generate_key()
            try:
                with open(KEY_PATH, 'wb') as key_file:
                    key_file.write(key)
            except IOError as e:
                raise Exception(f"Failed to write new encryption key: {e}")

    return key

fernet = Fernet(load_key())

def encrypt_file(data: bytes) -> bytes:
    """
    Encrypt bytes using Fernet symmetric encryption.
    """
    return fernet.encrypt(data)

def decrypt_file(data: bytes) -> bytes:
    """
    Decrypt bytes using Fernet symmetric encryption.
    """
    return fernet.decrypt(data)
