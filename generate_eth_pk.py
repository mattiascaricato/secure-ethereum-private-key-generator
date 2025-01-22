import subprocess
import base64
from ecdsa.curves import SECP256k1

# Get the order of secp256k1 directly from the library
# 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
SECP256K1_ORDER = SECP256k1.order

def generate_random_32_bytes():
    """Generate 32 random bytes using AWS KMS."""
    result = subprocess.run(
        ["aws", "kms", "generate-random", "--number-of-bytes", "32", "--query", "Plaintext", "--output", "text"],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise Exception(f"Error generating random bytes: {result.stderr.strip()}")

    # Decode base64 output and convert to hex
    raw_bytes = base64.b64decode(result.stdout.strip())
    return raw_bytes.hex()

def is_valid_private_key(hex_key):
    """Check if the private key is within the valid Ethereum range."""
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
