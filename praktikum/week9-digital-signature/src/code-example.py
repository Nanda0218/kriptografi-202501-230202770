from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# =========================
# GENERATE RSA KEY PAIR
# =========================
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# =========================
# MESSAGE TO BE SIGNED
# =========================
message = b"Hello, ini pesan penting."
hash_message = SHA256.new(message)

# =========================
# CREATE DIGITAL SIGNATURE
# =========================
signature = pkcs1_15.new(private_key).sign(hash_message)

print("=" * 50)
print("DIGITAL SIGNATURE (HEX)")
print(signature.hex())
print("=" * 50)

# =========================
# VERIFY ORIGINAL MESSAGE
# =========================
try:
    pkcs1_15.new(public_key).verify(hash_message, signature)
    print("✔ Verifikasi berhasil: tanda tangan VALID")
except (ValueError, TypeError):
    print("✖ Verifikasi gagal: tanda tangan TIDAK VALID")

# =========================
# MODIFY MESSAGE (ATTACK SIMULATION)
# =========================
fake_message = b"Hello, ini pesan palsu."
hash_fake = SHA256.new(fake_message)

# =========================
# VERIFY FAKE MESSAGE
# =========================
try:
    pkcs1_15.new(public_key).verify(hash_fake, signature)
    print("✖ Verifikasi berhasil (INI SALAH)")
except (ValueError, TypeError):
    print("✔ Verifikasi gagal: tanda tangan tidak cocok dengan pesan")
