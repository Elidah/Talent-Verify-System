from cryptography.fernet import Fernet

# Generate this once and store securely (e.g., in environment variable)
key = b'KUreRivHHKE0QUvIrM0rMDQALaaUdrRkd7znIUOaXkE='  # Replace with your real key
cipher = Fernet(key)

def encrypt(data):
    return cipher.encrypt(data.encode()).decode()

def decrypt(data):
    return cipher.decrypt(data.encode()).decode()
