# secure-ethereum-private-key-generator ![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)
Securely generate cryptographically strong Ethereum private keys using AWS KMS as a true source of randomness. Ensures secp256k1 elliptic curve compliance.

- Uses **AWS KMS** for cryptographic-grade randomness instead of predictable entropy or local randomness flaws.
- Filters out invalid keys exceeding **secp256k1** elliptic curve limits.
- Simple **script** or **one-liner CLI command**.
- No dependencies beyond **AWS CLI** and **Python**.

## Requirements
- AWS CLI
- AWS credentials configured
- Python 3

## Dependencies
```sh
pip3 install -r requirements.txt
```

## Usage
```sh
python3 generate_eth_pk.py
```

## One-liner-command
```sh
while true; do key=$(aws kms generate-random --number-of-bytes 32 --query "Plaintext" --output text | base64 --decode | xxd -p -c 32); python3 -c "import sys; from eth_keys import keys; k=int(sys.argv[1], 16); exit(0 if 1 <= k < 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141 else 1)" "$key" && echo "Private Key: $key" && echo "Wallet Address: $(python3 -c "from eth_keys import keys; pk = keys.PrivateKey(bytes.fromhex('$key')); print(pk.public_key.to_checksum_address())")" && break; done
```

## License
[MIT](https://github.com/mattiascaricato/secure-ethereum-private-key-generator/blob/main/LICENSE)
