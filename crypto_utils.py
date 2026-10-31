import hashlib
import base64
from cryptography.fernet import Fernet

def generate_hash(text):
    """SHA-256 Hash üretir."""
    return hashlib.sha256(text.encode()).hexdigest()

def encrypt_message(message, secret_key):
    """AES tabanlı Fernet ile metin şifreler."""
    key = base64.urlsafe_b64encode(hashlib.sha256(secret_key.encode()).digest())
    f = Fernet(key)
    return f.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message, secret_key):
    """Şifreli metni çözer."""
    try:
        key = base64.urlsafe_b64encode(hashlib.sha256(secret_key.encode()).digest())
        f = Fernet(key)
        return f.decrypt(encrypted_message.encode()).decode()
    except Exception:
        return "HATA: Geçersiz anahtar veya bozuk şifreli metin!"