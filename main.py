import hashlib

def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

if __name__ == "__main__":
    password = input("Enter a password: ")
    hashed_password = hash_password(password)
    print(f"Hashed password: {hashed_password}")
