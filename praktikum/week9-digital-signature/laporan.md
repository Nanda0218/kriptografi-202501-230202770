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

Sementara itu, DSA (Digital Signature Algorithm) mengandalkan kesulitan masalah logaritma diskret dalam aritmetika modular. DSA menghasilkan tanda tangan berupa dua nilai unik yang bergantung pada kunci privat dan hash pesan. Algoritma ini dirancang khusus oleh NIST dan banyak digunakan dalam standar keamanan seperti SSH. Baik RSA maupun DSA bertujuan memberikan autentikasi dan integritas, hanya berbeda pada dasar matematis dan cara menghasilkan tanda tangan.Berikut **ringkasan teori digital signature (RSA/DSA) tanpa rumus**, 2–3 paragraf sesuai permintaan:

---

**Digital signature** adalah teknik kriptografi yang digunakan untuk memastikan bahwa pesan atau dokumen digital benar-benar dibuat oleh pengirim yang sah dan tidak mengalami perubahan. Sistem ini menggunakan pasangan kunci asimetris: **private key** untuk menandatangani, dan **public key** untuk memverifikasi tanda tangan tersebut. Prosesnya selalu melibatkan fungsi **hash** yang mengubah pesan menjadi jejak digital unik, sehingga verifikasi dapat dilakukan dengan cepat dan aman.

Pada **RSA**, keamanan digital signature bergantung pada kesulitan memecahkan masalah faktorisasi bilangan besar. Private key pemilik digunakan untuk membuat tanda tangan digital, sementara public key dapat digunakan siapa saja untuk memeriksa keasliannya. RSA dikenal sederhana dalam konsep dan umum digunakan karena kompatibel dengan banyak sistem keamanan modern.

Sementara itu, **DSA (Digital Signature Algorithm)** mengandalkan kesulitan masalah logaritma diskret dalam aritmetika modular. DSA menghasilkan tanda tangan berupa dua nilai unik yang bergantung pada kunci privat dan hash pesan. Algoritma ini dirancang khusus oleh NIST dan banyak digunakan dalam standar keamanan seperti SSH. Baik RSA maupun DSA bertujuan memberikan autentikasi dan integritas, hanya berbeda pada dasar matematis dan cara menghasilkan tanda tangan.

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
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
