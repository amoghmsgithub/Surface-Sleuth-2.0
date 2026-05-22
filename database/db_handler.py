import os
import pickle
from security.pqc_crypto import encrypt_data, decrypt_data

DB_FILE = "fingerprint_db.enc"


def save_db(data, key):
    """
    Encrypt and save the fingerprint database
    """
    try:
        # Serialize data
        raw_data = pickle.dumps(data)

        # Encrypt data
        nonce, encrypted_data = encrypt_data(key, raw_data)

        # Save to file
        with open(DB_FILE, "wb") as f:
            pickle.dump((nonce, encrypted_data), f)

        print("✅ Database encrypted and saved successfully")

    except Exception as e:
        print(f"❌ Error saving DB: {e}")


def load_db(key):
    """
    Load and decrypt the fingerprint database
    """
    try:
        if not os.path.exists(DB_FILE):
            print("⚠️ No database found, returning empty DB")
            return {}

        # Load encrypted data
        with open(DB_FILE, "rb") as f:
            nonce, encrypted_data = pickle.load(f)

        # Decrypt
        decrypted_data = decrypt_data(key, nonce, encrypted_data)

        # Deserialize
        db = pickle.loads(decrypted_data)

        print("✅ Database decrypted successfully")
        return db

    except Exception as e:
        print(f"❌ Error loading DB: {e}")
        return {}