# Laporan Praktikum Kriptografi
Minggu ke-: 5
Topik: [Cipher Klasik (Caesar, Vigenère, Transposisi)]  
Nama: [Nanda Erdi Pratama]  
NIM: [230202770]  
Kelas: [5IKRB]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
Mengimplementasikan algoritma transposisi sederhana.
Menjelaskan kelemahan algoritma kriptografi klasik.

---

## 2. Dasar Teori
Teori Cipher Klasik

Cipher klasik adalah sistem kriptografi tradisional yang bekerja pada karakter individual (biasa huruf alfabet) menggunakan transformasi sederhana tanpa memerlukan komputasi kompleks. Dua kategori utamanya adalah cipher substitusi (mengganti setiap huruf plaintext dengan huruf ciphertext) dan cipher transposisi (mengubah urutan huruf plaintext tanpa mengubah identitas hurufnya). Cipher-cipher ini umumnya bersifat simetris, menggunakan kunci yang sama untuk proses enkripsi dan dekripsi. Caesar cipher merupakan cipher substitusi paling sederhana yang menggunakan konsep modular aritmetika. Setiap huruf plaintext digeser sejumlah posisi tetap dalam alfabet (misal: geser 3, A→D, B→E). Operasi modular (mod 26) memastikan pergeseran tetap dalam rentang alfabet. Sementara Vigenère cipher memperluas konsep ini menggunakan kunci berbasis kata/frasa yang menciptakan multiple shift values, sehingga menghasilkan polyalphabetic substitution yang lebih kuat daripada Caesar cipher. Cipher transposisi mengacak plaintext dengan menyusunnya dalam matriks atau pola tertentu berdasarkan kunci, kemudian membaca ulang sesuai aturan transposisi. Contohnya columnar transposition yang menulis plaintext per kolom kemudian membaca per baris. Keamanan cipher klasik secara umum telah terpecahkan dengan teknik analisis frekuensi dan metode kriptanalisis modern, namun tetap menjadi fondasi penting dalam memahami prinsip-prinsip kriptografi.

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
