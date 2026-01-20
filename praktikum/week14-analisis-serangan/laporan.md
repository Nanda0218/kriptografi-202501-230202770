# Laporan Praktikum Kriptografi
Minggu ke-: 14
Topik: [Analisis Serangan Kriptografi]  
Nama: [Nanda Erdi Pratama]  
NIM: [230202770]  
Kelas: [5IKRB]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Mengidentifikasi jenis serangan pada sistem informasi nyata.  
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.  
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan. 

---

## 2. Dasar Teori
Kriptografi merupakan ilmu yang mempelajari teknik pengamanan informasi agar hanya pihak yang berwenang yang dapat mengaksesnya. Pada kriptografi klasik, pengamanan data dilakukan menggunakan cipher klasik seperti Caesar Cipher, Vigenère Cipher, dan Substitution Cipher, yang bekerja dengan cara mengganti atau menggeser huruf berdasarkan aturan tertentu. Kelemahan utama cipher klasik terletak pada ruang kunci yang kecil dan pola yang mudah dianalisis, sehingga rentan terhadap serangan seperti brute force dan frequency analysis. Hal ini mendorong berkembangnya kriptografi modern yang mengandalkan perhitungan matematis yang lebih kompleks.

Kriptografi modern banyak menggunakan konsep aritmetika modular, yaitu operasi matematika dengan sisa pembagian (modulo). Konsep ini menjadi dasar algoritma populer seperti RSA, Diffie–Hellman, dan ElGamal, di mana keamanan sistem bergantung pada kesulitan masalah matematika tertentu, seperti faktorisasi bilangan prima besar atau logaritma diskret. Serangan kriptografi modern umumnya berusaha mengeksploitasi kelemahan implementasi atau keterbatasan komputasi, bukan sekadar menebak kunci secara langsung.

Serangan kriptografi dapat diklasifikasikan menjadi beberapa jenis, antara lain ciphertext-only attack, known-plaintext attack, chosen-plaintext attack, dan brute force attack. Selain itu, terdapat pula serangan berbasis implementasi seperti side-channel attack yang memanfaatkan informasi fisik (waktu eksekusi, konsumsi daya). Oleh karena itu, sistem kriptografi yang aman tidak hanya membutuhkan algoritma yang kuat secara teori, tetapi juga implementasi yang benar dan pengelolaan kunci yang baik.
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
- Pertanyaan 1: Banyak sistem lama dirancang saat kemampuan komputasi masih terbatas, sehingga menggunakan panjang kunci yang pendek, algoritma hash lemah (misalnya MD5 atau SHA-1), serta tanpa mekanisme proteksi tambahan seperti salt dan rate limiting. Akibatnya, penyerang modern dengan perangkat keras cepat dan wordlist besar dapat dengan mudah melakukan brute force atau dictionary attack dalam waktu singkat.
- Pertanyaan 2: Kelemahan algoritma berasal dari desain matematis algoritma itu sendiri, misalnya algoritma yang sudah terbukti dapat dipecahkan secara kriptanalisis. Sementara itu, kelemahan implementasi muncul karena kesalahan penerapan, seperti manajemen kunci yang buruk, penggunaan mode enkripsi yang salah, atau kebocoran informasi melalui side-channel. Algoritma yang kuat tetap dapat menjadi tidak aman jika diimplementasikan secara keliru.
- Pertanyaan 3: Organisasi perlu menggunakan algoritma dan standar kriptografi terkini, melakukan pembaruan dan audit keamanan secara berkala, serta menerapkan manajemen kunci yang kuat. Selain itu, penting untuk mengikuti perkembangan ancaman terbaru, termasuk kesiapan terhadap kriptografi pasca-kuantum, agar sistem tetap aman dalam jangka panjang.
)
---

## 8. Kesimpulan
Berdasarkan hasil percobaan, dapat disimpulkan bahwa tingkat keamanan suatu algoritma kriptografi sangat bergantung pada kompleksitas algoritma dan panjang kunci yang digunakan. Percobaan menunjukkan bahwa cipher sederhana lebih mudah diserang dibandingkan algoritma kriptografi modern yang berbasis perhitungan matematis kompleks. Oleh karena itu, pemilihan algoritma dan implementasi yang tepat sangat penting untuk menjaga kerahasiaan dan keamanan data.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log

```
commit ff99d561a9db4989bd60c77b00044120f9e40ba8 
Author: Nanda0218 <nandaerdipratama29@gmail.com>
Date:   Tue Jan 20 14:35:50 2026 +0700

    week14-analisis-serangan
```
