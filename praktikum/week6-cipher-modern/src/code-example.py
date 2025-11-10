print("=== LANGKAH 1 — IMPLEMENTASI DES ===")
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)  # kunci 64 bit (8 byte)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"ABCDEFGH"
print("Plaintext:", plaintext)

ciphertext = cipher.encrypt(plaintext)
print("Ciphertext (hex):", ciphertext.hex())

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)
print()

print("=== LANGKAH 2 — IMPLEMENTASI AES-128 ===")
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 128 bit key
cipher = AES.new(key, AES.MODE_EAX)

plaintext = b"Modern Cipher AES Example"
print("Plaintext:", plaintext)

ciphertext, tag = cipher.encrypt_and_digest(plaintext)
print("Ciphertext (hex):", ciphertext.hex())

# Dekripsi - PERBAIKAN: gunakan decrypt_and_verify
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt_and_verify(ciphertext, tag)  # ← INI PERBAIKANNYA
print("Decrypted:", decrypted.decode())
print()

print("=== LANGKAH 3 — IMPLEMENTASI RSA ===")
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Enkripsi dengan public key
cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"RSA Example"
print("Plaintext:", plaintext)

ciphertext = cipher_rsa.encrypt(plaintext)
print("Ciphertext (hex):", ciphertext.hex())

# Dekripsi dengan private key
decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())