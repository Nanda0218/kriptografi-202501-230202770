from secretsharing import SecretSharer
import hashlib
import base64

def contoh_secret_sharing():
    # Rahasia yang ingin dibagi
    secret = "KriptografiUPB2025"
    print(f"Rahasia asli: {secret}")
    print(f"Panjang rahasia: {len(secret)} karakter")
    
    # Bagi menjadi 5 shares, ambang batas 3 (minimal 3 shares untuk rekonstruksi)
    shares = SecretSharer.split_secret(secret, 3, 5)
    print("\nShares yang dihasilkan:")
    for i, share in enumerate(shares, 1):
        print(f"  Share {i}: {share}")
    
    # Rekonstruksi rahasia dari 3 shares
    recovered = SecretSharer.recover_secret(shares[:3])
    print(f"\nRahasia direkonstruksi dari 3 shares pertama: {recovered}")
    
    # Verifikasi
    if secret == recovered:
        print("✓ Rekonstruksi berhasil! Rahasia sama dengan aslinya.")
    else:
        print("✗ Rekonstruksi gagal!")
    
    return shares

def contoh_dengan_share_berbeda():
    print("\n" + "="*50)
    print("Contoh dengan kombinasi shares berbeda:")
    
    secret = "KriptografiUPB2025"
    shares = SecretSharer.split_secret(secret, 3, 5)
    
    # Coba berbagai kombinasi 3 shares
    kombinasi = [
        [0, 1, 2],  # shares 1-3
        [0, 2, 4],  # shares 1,3,5
        [1, 3, 4],  # shares 2,4,5
        [0, 1, 4],  # shares 1,2,5
    ]
    
    for i, kombo in enumerate(kombinasi, 1):
        selected_shares = [shares[idx] for idx in kombo]
        recovered = SecretSharer.recover_secret(selected_shares)
        print(f"Kombinasi {i} (shares {[idx+1 for idx in kombo]}): {recovered}")
    
    # Coba dengan hanya 2 shares (seharusnya gagal)
    print("\nMencoba dengan hanya 2 shares (seharusnya gagal):")
    try:
        recovered = SecretSharer.recover_secret(shares[:2])
        print(f"Hasil: {recovered}")
    except Exception as e:
        print(f"Error (sesuai harapan): {type(e).__name__}")

def contoh_data_biner():
    print("\n" + "="*50)
    print("Contoh dengan data biner/byte:")
    
    # Untuk data biner, kita perlu encode dulu
    data_biner = b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A"
    secret_hex = data_biner.hex()
    
    print(f"Data biner asli: {data_biner}")
    print(f"Dalam format hex: {secret_hex}")
    
    # Bagi secret
    shares = SecretSharer.split_secret(secret_hex, 2, 4)
    
    print("\nShares untuk data biner:")
    for i, share in enumerate(shares, 1):
        print(f"  Share {i}: {share}")
    
    # Rekonstruksi
    recovered_hex = SecretSharer.recover_secret(shares[:2])
    recovered_biner = bytes.fromhex(recovered_hex)
    
    print(f"\nData biner direkonstruksi: {recovered_biner}")
    
    if data_biner == recovered_biner:
        print("✓ Rekonstruksi data biner berhasil!")
    else:
        print("✗ Rekonstruksi data biner gagal!")

def contoh_dengan_hash():
    print("\n" + "="*50)
    print("Contoh dengan verifikasi hash:")
    
    # Data sensitif
    data_sensitif = "PasswordRahasia2025#"
    
    # Tambahkan hash untuk verifikasi
    hash_obj = hashlib.sha256(data_sensitif.encode()).hexdigest()
    secret_with_hash = f"{data_sensitif}:{hash_obj}"
    
    print(f"Data asli: {data_sensitif}")
    print(f"Hash SHA256: {hash_obj[:16]}...")
    
    # Bagi secret
    shares = SecretSharer.split_secret(secret_with_hash, 3, 6)
    
    # Simulasikan kehilangan beberapa shares
    print(f"\nTotal shares dibuat: {len(shares)}")
    print("Misalkan share 2 dan 5 hilang...")
    
    # Hanya memiliki shares 1, 3, 4, 6
    available_shares = [shares[0], shares[2], shares[3], shares[5]]
    
    # Rekonstruksi dengan 3 shares dari yang tersedia
    recovered_with_hash = SecretSharer.recover_secret(available_shares[:3])
    
    # Pisahkan data dan hash
    recovered_data, recovered_hash = recovered_with_hash.split(":", 1)
    
    print(f"\nData direkonstruksi: {recovered_data}")
    
    # Verifikasi hash
    new_hash = hashlib.sha256(recovered_data.encode()).hexdigest()
    
    if new_hash == recovered_hash:
        print("✓ Hash valid! Data tidak dimodifikasi.")
    else:
        print("✗ Hash tidak valid! Data mungkin dimodifikasi.")

def main():
    print("DEMO IMPLEMENTASI SECRET SHARING")
    print("="*50)
    
    # Contoh 1: Basic usage
    shares = contoh_secret_sharing()
    
    # Contoh 2: Kombinasi berbeda
    contoh_dengan_share_berbeda()
    
    # Contoh 3: Data biner
    contoh_data_biner()
    
    # Contoh 4: Dengan verifikasi hash
    contoh_dengan_hash()
    
    print("\n" + "="*50)
    print("Ringkasan:")
    print("- Secret sharing membagi rahasia menjadi beberapa bagian (shares)")
    print("- Minimal diperlukan threshold shares untuk rekonstruksi")
    print("- Setiap share tunggal tidak mengungkapkan informasi tentang rahasia")
    print("- Cocok untuk backup kunci kriptografi dan data sensitif")

if __name__ == "__main__":
    main()