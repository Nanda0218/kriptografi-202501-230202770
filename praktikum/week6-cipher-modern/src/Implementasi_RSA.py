print("=== STARTING RSA TEST ===")

try:
    # Test import
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    print("✓ Imports successful")
    
    # Generate key pair
    print("Generating RSA keys...")
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()
    print("✓ RSA keys generated")
    
    # Enkripsi dengan public key
    print("Encrypting...")
    cipher_rsa = PKCS1_OAEP.new(public_key)
    plaintext = b"RSA Example"
    print(f"Plaintext: {plaintext}")
    
    ciphertext = cipher_rsa.encrypt(plaintext)
    print(f"✓ Encryption successful")
    print(f"Ciphertext (hex): {ciphertext.hex()}")
    print(f"Ciphertext (raw): {ciphertext}")
    
    # Dekripsi dengan private key
    print("Decrypting...")
    decipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted = decipher_rsa.decrypt(ciphertext)
    print(f"✓ Decryption successful")
    print(f"Decrypted bytes: {decrypted}")
    print(f"Decrypted string: {decrypted.decode()}")
    
    # Verifikasi
    print(f"✓ Verification: {decrypted == plaintext}")
    
except Exception as e:
    print(f"✗ Error: {e}")
    print(f"Error type: {type(e).__name__}")
    import traceback
    traceback.print_exc()

print("=== PROGRAM FINISHED ===")