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
