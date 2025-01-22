import base64
import boto3
from ecdsa.curves import SECP256k1

# Get the order of secp256k1
# 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
SECP256K1_ORDER = SECP256k1.order

# Initialize AWS KMS client
kms_client = boto3.client("kms")

def generate_random_32_bytes():
    """Generate 32 random bytes using AWS KMS with boto3."""
    response = kms_client.generate_random(NumberOfBytes=32)
    raw_bytes = response["Plaintext"]
    return raw_bytes.hex()

def is_valid_private_key(hex_key):
    """Checks if the private key is within the valid SECP256K1 range: 1 ≤ key < curve order (prevents invalid keys)."""
    key_int = int(hex_key, 16)
    return 1 <= key_int < SECP256K1_ORDER

def main():
    while True:
        private_key = generate_random_32_bytes()
        if is_valid_private_key(private_key):
            print(f"Private Key: 0x{private_key}")
            break

if __name__ == "__main__":
    main()

