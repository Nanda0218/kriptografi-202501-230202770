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