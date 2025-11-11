# Laporan Praktikum Kriptografi
Minggu ke-: 7 
Topik: [Diffie-Hellman Key Exchange]
Nama: [Nanda Erdi Pratama]
NIM: [230202770]
Kelas: [5IKRB]

---

## 1. Tujuan
Tujuan Pembelajaran
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Melakukan simulasi protokol **Diffie-Hellman** untuk pertukaran kunci publik.  
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.  
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan **Man-in-the-Middle / MITM**).  


---

## 2. Dasar Teori
Teori Pertukaran Kunci Diffie-Hellman

Diffie-Hellman adalah sebuah protokol yang memungkinkan dua pihak yang belum saling kenal untuk menciptakan sebuah kunci rahasia bersama melalui saluran komunikasi yang mungkin sedang disadap. Keajaiban dari metode ini terletak pada kemampuannya untuk membuat kunci rahasia tanpa harus mengirimkan kunci tersebut secara langsung. Sebelum penemuan ini, kedua pihak harus memiliki kunci rahasia yang sama terlebih dahulu, yang sulit dilakukan jika mereka tidak pernah bertemu.

Inti dari keamanan Diffie-Hellman terletak pada sebuah konsep matematika yang mirip dengan fungsi "jalan satu arah". Bayangkan sebuah proses dimana sangat mudah untuk melakukan perhitungan ke depan, tetapi hampir mustahil untuk membaliknya. Sebagai analogi, mencampur cat warna sangatlah mudah, tetapi mencoba untuk memisahkan campuran cat tersebut kembali menjadi warna aslinya adalah hal yang mustahil. Dalam Diffie-Hellman, kedua pihak secara independen mencampur "warna rahasia" mereka dengan "warna publik" yang disepakati, lalu saling bertukar hasil campuran ini.

Di akhir proses, kedua pihak akan mencampur hasil yang mereka terima dari pihak lain dengan "warna rahasia" mereka sendiri. Ajaibnya, kedua pihak akan menghasilkan "warna" akhir yang sama persis, yang menjadi kunci rahasia bersama. Bagi pihak ketiga yang menyadari pertukaran, mereka hanya melihat "warna-warna campuran" yang sudah dipertukarkan. Tanpa mengetahui "warna rahasia" asli dari salah satu pihak, hampir tidak mungkin bagi mereka untuk mengetahui "warna" akhir dari kunci rahasia tersebut.

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
import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)

```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](Screenshots/Hasil_Eksekusi.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Diffie-Hellman memungkinkan pertukaran kunci di saluran publik karena menggunakan konsep "jalan satu arah" (one-way function) dalam matematika.

Berikut penjelasan singkatnya:

1. Pertukaran Hanya Informasi "Publik":
   Yang ditransmisikan melalui saluran publik hanyalah hasil perhitungan tertentu (nilai publik), bukan kunci rahasia itu sendiri. Kunci rahasia masing-masing pihak tidak pernah dikirim.

2. Fungsi Matematika yang Tidak Simetris:
   Proses perhitungannya dirancang agar:
   - Mudah bagi kedua pihak untuk menghasilkan kunci bersama dari kombinasi nilai publik dan rahasia mereka.
   - Sangat Sulit bagi penyadap untuk menurunkan kunci rahasia hanya dari nilai-nilai publik yang dilihatnya. Kesulitan ini dikenal sebagai masalah *Logaritma Diskrit*.

3. Analoginya:
   Bayangkan dua orang mencampur cat. Mereka setuju pada satu warna dasar (publik). Masing-masing menambahkan warna rahasia mereka sendiri, lalu bertukar hasil campuran. Mereka lalu menambahkan lagi warna rahasia mereka ke campuran yang diterima. Hasil akhirnya, kedua orang mendapatkan warna yang sama, tetapi bagi orang yang mengamati pertukaran campuran tadi, sangatlah sulit untuk mengetahui warna rahasia asli atau warna akhirnya.

Kesimpulan:
Diffie-Hellman aman dilakukan di saluran publik karena penyadap hanya melihat "bahan mentah" (nilai publik) yang tidak cukup untuk merekonstruksi kunci rahasia akhir, berkat kompleksitas matematika yang melandasinya.
- Pertanyaan 2: Kelemahan Utama Protokol Diffie-Hellman Murni

Kelemahan paling kritis dari protokol Diffie-Hellman murni (tanpa otentikasi) adalah kerentanan terhadap serangan Man-in-the-Middle (MITM).

Berikut penjelasannya:

1. Ketiadaan Otentikasi:
   Protokol dasar ini hanya menjamin bahwa sebuah kunci rahasia bersama dapat dibuat. Namun, ia tidak memverifikasi identitas pihak yang sedang diajak berkomunikasi. Seorang penyerang (Mallory) dapat dengan mudah menyusup di antara kedua pihak (Alice dan Bob).

2. Mekanisme Serangan Man-in-the-Middle:
   - Penyerang menyela komunikasi antara Alice dan Bob.
   - Terhadap Alice, penyerang berpura-pura menjadi Bob, dan melakukan pertukaran Diffie-Hellman terpisah untuk membuat kunci rahasia bersama dengan Alice.
   - Terhadap Bob, penyerang berpura-pura menjadi Alice, dan melakukan pertukaran Diffie-Hellman terpisah lainnya untuk membuat kunci rahasia bersama dengan Bob.
   - Hasilnya, Alice dan Bob *merasa* telah berkomunikasi langsung dan memiliki kunci rahasia bersama, padahal kenyataannya:
     - Alice memiliki kunci bersama dengan penyerang.
     - Bob memiliki kunci bersama dengan penyerang.
   - Semua komunikasi yang kemudian dienkripsi dengan kunci tersebut akan diteruskan oleh penyerang, yang dapat menyadap, membaca, bahkan mengubah isi pesan sebelum meneruskannya ke tujuan asli.

Analogi:
Bayangkan Anda (Alice) ingin membuat rahasia dengan Bob. Seorang penipu (Mallory) berdiri di tengah. Anda membisikkan rahasia Anda kepada Mallory, mengira dialah Bob. Mallory lalu pergi ke Bob dan membisikkan rahasia yang berbeda, mengatasnamakan Anda. Baik Anda maupun Bob tidak menyadari bahwa rahasia yang Anda bagikan sebenarnya adalah dengan si penipu, bukan satu sama lain.

Kesimpulan:
Diffie-Hellman murni tidak aman untuk digunakan sendiri karena rentan terhadap penyusupan. Oleh karena itu, dalam praktiknya, protokol ini harus dikombinasikan dengan metode otentikasi, seperti tanda tangan digital (seperti dalam Authenticated Diffie-Hellman) atau sertifikat digital (seperti yang digunakan dalam TLS/SSL), untuk memastikan bahwa Anda sedang bertukar kunci dengan pihak yang benar, bukan dengan penyerang.
- Pertanyaan 3: Cara Mencegah Serangan MITM pada Protokol Diffie-Hellman

Untuk mencegah serangan Man-in-the-Middle, kunci utamanya adalah memverifikasi identitas kedua pihak yang berkomunikasi. Berikut adalah metode-metode yang dapat digunakan:

1. Sertifikat Digital (Public Key Infrastructure)
Metode ini menggunakan pihak ketiga tepercaya yang disebut Otoritas Sertifikat. Setiap pihak memiliki sertifikat digital yang berisi identitas dan kunci publiknya yang telah diverifikasi dan ditandatangani oleh otoritas tersebut. Saat pertukaran kunci berlangsung, sertifikat ini ditampilkan sebagai bukti identitas yang sah, sehingga mencegah penyerang berpura-pura menjadi salah satu pihak.

2. Tanda Tangan Digital
Setiap pesan dalam proses pertukaran kunci ditandatangani secara digital menggunakan kunci privat pengirim. Penerima dapat memverifikasi tanda tangan ini dengan kunci publik yang sah dari pengirim. Karena penyerang tidak memiliki kunci privat yang benar, mereka tidak dapat memalsukan tanda tangan yang valid.

3. Kunci Pra-Bagi (Pre-Shared Keys)
Kedua pihak telah berbagi rahasia bersama sebelumnya melalui saluran yang aman. Rahasia ini kemudian digunakan untuk membuktikan identitas selama proses pertukaran kunci, biasanya dengan menghasilkan kode otentikasi untuk setiap pesan yang dikirim.

Intinya, Diffie-Hellman perlu dikombinasikan dengan sistem pembuktian identitas yang kuat. Tanpa otentikasi, protokol ini hanya membuat terowongan rahasia tanpa bisa memastikan dengan siapa kita berbagi terowongan tersebut.
)
---

## 8. Kesimpulan
Berdasarkan percobaan, dapat disimpulkan bahwa Protokol Diffie-Hellman memungkinkan dua pihak menghasilkan kunci rahasia yang sama tanpa pernah mengirimkan kunci tersebut secara langsung. Keamanan proses ini bergantung pada kesulitan matematis untuk membalikkan perhitungan pertukaran, meskipun semua informasi lainnya diketahui publik. Dengan demikian, metode ini efektif untuk membangun keamanan komunikasi di saluran yang tidak terpercaya.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
commit ff796d14b8731b80a735a9333f5f7dcdf19209f9 (HEAD -> main, origin/main, origin/HEAD)
Author: Nanda0218 <nandaerdipratama29@gmail.com>
Date:   Tue Nov 11 13:06:45 2025 +0700

    week7-diffie-hellman
```
