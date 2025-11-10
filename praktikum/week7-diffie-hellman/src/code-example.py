import random

# Parameter publik yang disepakati
p = 23  # bilangan prima
g = 5   # generator modulo p

print("=== PROTOCOL DIFFIE-HELLMAN KEY EXCHANGE ===")
print(f"Parameter publik: p = {p}, g = {g}")
print()

# Generate private keys
a = random.randint(1, p-1)  # private key Alice
b = random.randint(1, p-1)  # private key Bob

print(f"Private Key Alice (a): {a}")
print(f"Private Key Bob (b): {b}")
print()

# Generate public keys
A = pow(g, a, p)  # public key Alice: g^a mod p
B = pow(g, b, p)  # public key Bob: g^b mod p

print(f"Public Key Alice (A): {A}")
print(f"Public Key Bob (B): {B}")
print()

# Pertukaran public key terjadi di sini
# Alice mengirim A ke Bob, Bob mengirim B ke Alice

# Hitung shared secret
shared_secret_Alice = pow(B, a, p)  # Alice hitung: B^a mod p
shared_secret_Bob = pow(A, b, p)    # Bob hitung: A^b mod p

print("=== HASIL SHARED SECRET ===")
print(f"Kunci bersama Alice: {shared_secret_Alice}")
print(f"Kunci bersama Bob: {shared_secret_Bob}")
print()

# Verifikasi
if shared_secret_Alice == shared_secret_Bob:
    print("✅ SUKSES: Kunci bersama sama!")
    print(f"Shared Secret: {shared_secret_Alice}")
else:
    print("❌ GAGAL: Kunci bersama berbeda!")