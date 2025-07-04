from passlib.context import CryptContext

pwdd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return pwdd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against a hashed password."""
    return pwdd_context.verify(plain_password, hashed_password)