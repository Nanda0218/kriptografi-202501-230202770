# Laporan Praktikum Kriptografi
Minggu ke-: 4
Topik: [Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)]  
Nama: [Nanda Erdi Pratama]  
NIM: [230202770]  
Kelas: [5IKRB]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menyelesaikan perhitungan sederhana terkait entropi kunci.  
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.  
3. Menghitung **unicity distance** untuk ciphertext tertentu.  
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.  
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

---

## 2. Dasar Teori
Teori Dasar

Entropi kunci mengukur tingkat keacakan dan ketidakpastian suatu kunci kriptografi. Kunci yang memiliki entropi tinggi berarti sangat sulit ditebak karena terdapat banyak kemungkinan kandidat kunci yang sama-sama mungkin. Sebaliknya, entropi rendah menunjukkan pola atau kelemahan dalam pembuatan kunci, membuatnya rentan terhadap serangan bahkan sebelum penyerangan dimulai. Konsep ini membantu mengevaluasi kekuatan dasar suatu sistem kriptografi. Unicity distance adalah jumlah minimum cipherteks yang dibutuhkan agar secara teori hanya ada satu kunci yang dapat menghasilkan plainteks yang bermakna. Setelah melewati jarak unik ini, penyerang dapat menentukan kunci yang benar dengan pasti. Konsep ini menggambarkan batas praktis dimana sistem kriptografi mulai kehilangan keamanannya ketika cukup banyak data terenkripsi yang berhasil dikumpulkan.

Contoh Cipher Klasik dan Aritmetika Modular

Cipher klasik seperti Caesar Cipher bekerja dengan menggeser setiap huruf plainteks berdasarkan nilai kunci. Aritmetika modular digunakan untuk memastikan pergeseran tetap berada dalam rentang huruf alfabet. Misalnya, dengan kunci 3, huruf A digeser menjadi D, B menjadi E, dan seterusnya. Ketika mencapai Z, perhitungan akan kembali ke awal alfabet. Pada Caesar Cipher yang hanya memiliki 26 kemungkinan kunci, sistem ini sangat lemah. Dengan menganalisis beberapa karakter cipherteks saja, penyerang sudah dapat menentukan kunci yang digunakan. Hal ini terjadi karena unicity distance-nya sangat pendek, menunjukkan bahwa cipher sederhana seperti ini mudah dipecahkan dengan analisis frekuensi karakter.

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
