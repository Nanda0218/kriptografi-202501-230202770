# Laporan Praktikum Kriptografi
Minggu ke-: 13
Topik: [TinyChain – Proof of Work (PoW)]  
Nama: [Nanda Erdi Pratama]  
NIM: [230202770]  
Kelas: [5IKRB]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menjelaskan peran **hash function** dalam blockchain.  
2. Melakukan simulasi sederhana **Proof of Work (PoW)**.  
3. Menganalisis keamanan cryptocurrency berbasis kriptografi.  
---

## 2. Dasar Teori
Proof of Work (PoW) merupakan mekanisme konsensus dalam teknologi blockchain yang digunakan untuk memverifikasi transaksi dan menambahkan blok baru ke dalam rantai blok. Pada PoW, penambang (miner) diwajibkan menyelesaikan permasalahan komputasi berupa pencarian nilai hash yang memenuhi kriteria tertentu, seperti jumlah awalan nol. Proses ini membutuhkan daya komputasi yang besar sehingga mencegah manipulasi data dan serangan double spending, karena perubahan satu blok akan memerlukan perhitungan ulang seluruh blok berikutnya.

TinyChain mengadopsi konsep PoW dalam skala sederhana sebagai media pembelajaran untuk memahami prinsip kerja blockchain. Dalam TinyChain, algoritma hash (misalnya SHA-256) digunakan untuk mengubah data blok menjadi nilai tetap dengan sifat satu arah (one-way function). Proses pencarian nonce hingga menghasilkan hash yang valid mencerminkan konsep dasar kriptografi modern, khususnya fungsi hash kriptografis yang bersifat deterministik, sulit dibalik, dan sensitif terhadap perubahan input.

Secara matematis, PoW berkaitan dengan konsep komputasi berulang dan aritmetika sederhana, di mana nilai nonce diuji secara bertahap hingga memenuhi kondisi yang ditetapkan. Mekanisme ini menekankan prinsip computational difficulty, yaitu mudah untuk diverifikasi namun sulit untuk ditemukan. Dengan demikian, TinyChain – PoW menjadi model yang efektif untuk menjelaskan dasar keamanan blockchain, integritas data, dan konsensus terdistribusi tanpa kompleksitas sistem blockchain berskala besar.

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
- Pertanyaan 1: Fungsi hash sangat penting karena berfungsi untuk menjaga integritas dan keamanan data dalam blockchain. Setiap blok memiliki nilai hash unik yang dihasilkan dari data transaksi dan hash blok sebelumnya. Jika terjadi perubahan sekecil apa pun pada data, maka nilai hash akan berubah secara signifikan, sehingga manipulasi data dapat langsung terdeteksi. Selain itu, fungsi hash bersifat satu arah (one-way), sehingga data asli tidak dapat dengan mudah direkonstruksi dari nilai hash.
- Pertanyaan 2: Proof of Work mencegah double spending dengan mewajibkan setiap transaksi diverifikasi melalui proses penambangan yang memerlukan usaha komputasi tinggi. Setelah transaksi dimasukkan ke dalam blok dan divalidasi, blok tersebut ditambahkan ke blockchain dan didistribusikan ke seluruh jaringan. Untuk mengubah transaksi yang sudah tercatat, pelaku harus mengulang proses PoW pada blok tersebut dan seluruh blok setelahnya, yang membutuhkan sumber daya komputasi sangat besar dan hampir tidak mungkin dilakukan.
- Pertanyaan 3: Kelemahan utama PoW adalah konsumsi energi yang sangat tinggi, karena proses penambangan mengharuskan banyak perangkat melakukan perhitungan hash secara terus-menerus. Kompetisi antar penambang untuk menemukan hash yang valid menyebabkan pemborosan energi, karena sebagian besar perhitungan tidak menghasilkan blok yang sah. Hal ini membuat PoW kurang efisien dan berdampak negatif terhadap lingkungan, terutama pada blockchain berskala besar.
)
---

## 8. Kesimpulan
Berdasarkan percobaan TinyChain dengan mekanisme Proof of Work, dapat disimpulkan bahwa fungsi hash dan pencarian *nonce* berperan penting dalam menjaga integritas dan keamanan data blockchain. Proses PoW terbukti mampu mencegah manipulasi transaksi karena membutuhkan usaha komputasi yang tinggi untuk setiap perubahan blok. Namun, percobaan ini juga menunjukkan bahwa PoW kurang efisien dari sisi energi dan waktu komputasi.

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
