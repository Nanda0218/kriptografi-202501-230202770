# Laporan Praktikum Kriptografi
Minggu ke-: 9 
Topik: [Digital Signature (RSA/DSA)]  
Nama: [Nanda Erdi Pratama]  
NIM: [230202770]  
Kelas: [5IKRB]  

---

## 1. Tujuan
Tujuan Pembelajaran
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.  
2. Memverifikasi keaslian tanda tangan digital.  
3. Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.

---

## 2. Dasar Teori

Digital signature adalah teknik kriptografi yang digunakan untuk memastikan bahwa pesan atau dokumen digital benar-benar dibuat oleh pengirim yang sah dan tidak mengalami perubahan. Sistem ini menggunakan pasangan kunci asimetris: private key untuk menandatangani, dan public key untuk memverifikasi tanda tangan tersebut. Prosesnya selalu melibatkan fungsi hash yang mengubah pesan menjadi jejak digital unik, sehingga verifikasi dapat dilakukan dengan cepat dan aman.

Pada RSA, keamanan digital signature bergantung pada kesulitan memecahkan masalah faktorisasi bilangan besar. Private key pemilik digunakan untuk membuat tanda tangan digital, sementara public key dapat digunakan siapa saja untuk memeriksa keasliannya. RSA dikenal sederhana dalam konsep dan umum digunakan karena kompatibel dengan banyak sistem keamanan modern. 

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
from Crypto.PublicKey import RSA # type: ignore
from Crypto.Signature import pkcs1_15 # type: ignore
from Crypto.Hash import SHA256 # type: ignore

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Buat tanda tangan dengan private key
signature = pkcs1_15.new(private_key).sign(h)

print("="*50)
print("SIGNATURE (HEX):")
print(signature.hex())
print("="*50)

# Verifikasi tanda tangan asli
try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")

# Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

# Coba verifikasi dengan pesan palsu
try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](Screenshots/Eksekusi.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan  
- Pertanyaan 1: Perbedaan utama terletak pada tujuan dan penggunaan kunci. Pada enkripsi RSA, pengirim mengenkripsi pesan menggunakan kunci publik penerima untuk menjaga kerahasiaan, dan hanya penerima yang dapat mendekripsi pesan dengan kunci privatnya. Sebaliknya, pada tanda tangan digital RSA, pengirim membuat tanda tangan dengan kunci privat miliknya, dan siapa pun dapat memverifikasi keaslian tanda tangan tersebut menggunakan kunci publik pengirim.
- Pertanyaan 2: Tanda tangan digital menjamin integritas karena tanda tangan dibuat dari hasil hash pesan; perubahan sekecil apa pun pada pesan akan menyebabkan verifikasi gagal. Selain itu, tanda tangan digital menjamin otentikasi karena hanya pemilik kunci privat yang sah yang dapat menghasilkan tanda tangan tersebut, sehingga identitas pengirim dapat dipastikan.
- Pertanyaan 3: Certificate Authority (CA) berperan sebagai pihak tepercaya yang memverifikasi identitas pemilik kunci publik dan menerbitkan sertifikat digital. Sertifikat ini mengaitkan identitas dengan kunci publik secara resmi, sehingga penerima pesan dapat mempercayai bahwa kunci publik yang digunakan untuk verifikasi tanda tangan digital benar-benar milik pengirim yang sah.

## 8. Kesimpulan
Berdasarkan percobaan dengan tanda tangan digital menggunakan RSA/DSA, dapat disimpulkan bahwa tanda tangan digital berhasil memastikan integritas dan otentikasi pesan, karena verifikasi berhasil untuk pesan asli dan gagal untuk pesan yang diubah. Selain itu, tanda tangan yang dibuat dengan private key hanya bisa diverifikasi menggunakan public key yang sesuai, sehingga membuktikan identitas pengirim.


---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log

```
commit cf11f0387e2c48ecb1bd91ca288565ecb0d3caa4 (HEAD -> main, origin/main, origin/HEAD)
Author: Nanda0218 <nandaerdipratama29@gmail.com>
Date:   Wed Dec 10 14:29:04 2025 +0700

    week9-digital-signature
```
