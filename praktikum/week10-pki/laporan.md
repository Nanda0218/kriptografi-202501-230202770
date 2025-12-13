# Laporan Praktikum Kriptografi
Minggu ke-: 10  
Topik: [Public Key Infrastructure (PKI & Certificate Authority)]  
Nama: [Nanda Erdi Pratama]  
NIM: [230202770]  
Kelas: [5IKRB]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Membuat sertifikat digital sederhana.  
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.  
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).

---

## 2. Dasar Teori
Berikut ringkasan teori relevan tentang Public Key Infrastructure (PKI) dan Certificate Authority (CA):

Public Key Infrastructure (PKI) adalah sistem yang mendukung komunikasi aman di jaringan dengan menggunakan kriptografi kunci publik. PKI menyediakan kerangka untuk membuat, mendistribusikan, mengelola, dan mencabut sertifikat digital yang mengikat public key dengan identitas pemiliknya. Dengan PKI, pengguna dapat mengenkripsi pesan, memverifikasi tanda tangan digital, dan memastikan integritas serta autentikasi data dalam transaksi digital. PKI memanfaatkan konsep dasar kriptografi modern seperti RSA atau DSA, di mana pasangan kunci publik dan privat digunakan untuk enkripsi dan verifikasi tanda tangan digital.

Certificate Authority (CA) adalah pihak tepercaya yang berperan sebagai otoritas dalam PKI. CA bertanggung jawab memverifikasi identitas individu, organisasi, atau server sebelum menerbitkan sertifikat digital. Sertifikat ini mengikat identitas pemilik dengan public key mereka dan ditandatangani secara digital oleh CA. Dengan demikian, penerima pesan dapat memverifikasi keaslian public key pengirim menggunakan sertifikat CA, sehingga sistem tanda tangan digital menjadi aman dan dapat dipercaya.

PKI dan CA bekerja bersama untuk memastikan kerahasiaan, integritas, dan otentikasi komunikasi digital. Konsep ini sejalan dengan prinsip kriptografi klasik dan modern, termasuk penggunaan hash untuk memastikan integritas pesan dan operasi modular aritmetika dalam algoritma kunci publik seperti RSA. Dengan PKI, tanda tangan digital dan enkripsi kunci publik menjadi alat yang sah dan efektif untuk transaksi elektronik, komunikasi, dan keamanan data.
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
from cryptography import x509 # type: ignore
from cryptography.x509.oid import NameOID # type: ignore
from cryptography.hazmat.primitives import hashes, serialization # type: ignore
from cryptography.hazmat.primitives.asymmetric import rsa # type: ignore
from datetime import datetime, timedelta

# Generate key pair
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Buat subject & issuer (CA sederhana = self-signed)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

# Buat sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# Simpan sertifikat
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat: cert.pem")
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
- Pertanyaan 1: Fungsi utama Certificate Authority (CA) adalah bertindak sebagai pihak tepercaya yang memverifikasi identitas individu, organisasi, atau server sebelum mengeluarkan sertifikat digital. Sertifikat ini mengikat public key dengan identitas pemiliknya, sehingga penerima pesan atau pengguna layanan bisa yakin bahwa public key tersebut benar-benar milik pihak yang disebutkan.

Dengan kata lain, CA memastikan bahwa komunikasi dan transaksi digital menjadi aman, autentik, dan terpercaya, karena penerima dapat memverifikasi keaslian public key pengirim menggunakan sertifikat yang diterbitkan dan ditandatangani secara digital oleh CA.

Selain itu, CA juga membantu mendukung integritas, otentikasi, dan non-repudiation dalam sistem tanda tangan digital, sehingga pengirim tidak bisa menyangkal pesan yang telah ditandatangani dengan private key mereka.

- Pertanyaan 2: Self-signed certificate tidak cukup untuk sistem produksi karena beberapa alasan keamanan dan kepercayaan:

1. Tidak ada pihak tepercaya (trusted third party)
* Self-signed certificate dibuat dan ditandatangani sendiri oleh pemiliknya.
* Pihak penerima tidak bisa yakin** apakah public key benar-benar milik pengirim atau server, karena tidak diverifikasi oleh pihak tepercaya (CA).

2. Masalah kepercayaan browser atau sistem
* Browser, sistem operasi, atau aplikasi biasanya tidak mempercayai self-signed certificate secara default.
* Akibatnya, pengguna akan menerima peringatan keamanan (misal “Not Secure” di browser).
* Ini membuat self-signed certificate tidak cocok untuk layanan publik atau produksi.

3. Rentan terhadap serangan Man-in-the-Middle (MITM)
* Karena penerima tidak punya jaminan identitas yang sah, penyerang bisa menyisipkan certificate palsu dan berpura-pura sebagai server asli.
* Dengan CA, sertifikat diverifikasi sehingga serangan MITM menjadi jauh lebih sulit.

- Pertanyaan 3: PKI (Public Key Infrastructure) mencegah serangan Man-in-the-Middle (MITM) dalam komunikasi TLS/HTTPS melalui mekanisme sertifikat digital dan otentikasi pihak tepercaya. Berikut penjelasannya:

1. Verifikasi identitas server
* Server TLS/HTTPS memiliki sertifikat digital yang diterbitkan oleh Certificate Authority (CA) tepercaya.
* Sertifikat ini berisi public key server dan identitas server (misal domain).
* Saat klien (browser) terhubung ke server, klien memeriksa:
  1. Sertifikat valid dan belum kadaluarsa.
  2. Sertifikat ditandatangani oleh CA yang dipercaya.
  3. Nama domain pada sertifikat sesuai dengan server yang dikunjungi.
* Jika salah satu pemeriksaan gagal, klien menolak koneksi.

 2. Enkripsi kunci publik
* Setelah sertifikat diverifikasi, klien menggunakan public key server untuk menukar kunci sesi (session key) secara aman.
* Hanya server dengan private key yang sesuai dengan public key di sertifikat yang bisa mendekripsi kunci sesi.

3. Mencegah MITM
* Penyerang yang mencoba menyisipkan diri di tengah (MITM) tidak bisa:
  1. Memalsukan sertifikat yang valid dari CA tepercaya.
  2. Mendekripsi kunci sesi tanpa private key server asli.
* Karena itu, komunikasi tetap terenkripsi dan identitas server terjamin.
---

## 8. Kesimpulan
Berdasarkan percobaan pembuatan sertifikat digital self-signed, dapat disimpulkan bahwa PKI menyediakan kerangka kerja untuk mengikat public key dengan identitas pemiliknya melalui sertifikat digital, sehingga memungkinkan autentikasi dan enkripsi data. Certificate Authority (CA) berperan sebagai pihak tepercaya yang memverifikasi identitas sebelum sertifikat diterbitkan, memastikan komunikasi lebih aman. Self-signed certificate dapat digunakan untuk percobaan, tetapi untuk sistem produksi diperlukan sertifikat dari CA tepercaya agar integritas dan kepercayaan terjamin.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log

```
commit 71511175df6992d7bfb2a2b725def0a34b0f9fff (HEAD -> main, origin/main, origin/HEAD)
Author: Nanda0218 <nandaerdipratama29@gmail.com>
Date:   Wed Dec 10 14:56:50 2025 +0700

    week10-pki
```
