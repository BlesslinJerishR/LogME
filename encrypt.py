from cryptography.fernet import Fernet


def write_key():
    """Generates a key and save it in a file"""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """Loads the key from current directory """
    return open("key.key", "rb").read()


def encrypt(file, key):
    f = Fernet(key)
    with open(file, "rb") as file_content:
        file_data = file_content.read()
    encrypted_data = f.encrypt(file_data)
    with open(file, "wb") as file_content:
        file_content.write(encrypted_data)


def decrypt(file, key):
    f = Fernet(key)
    with open(file, "rb") as file_content:
        # reading encrypted
        encrypted_data = file_content.read()
        # decrypt data
        decrypted_data = f.decrypt(encrypted_data)
        str_decrypted_data = decrypted_data.decode('UTF-8')
        return str_decrypted_data
    # return original
    # with open(file, "r") as file_content:
        # file_content.write(decrypted_data)

