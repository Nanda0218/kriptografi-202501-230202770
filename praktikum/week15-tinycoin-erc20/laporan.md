# Laporan Praktikum Kriptografi
Minggu ke-: 15
Topik: [TinyCoin ERC20]  
Nama: [Nanda Erdi Pratama]  
NIM: [230202770]  
Kelas: [5IKRB]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Mengembangkan proyek sederhana berbasis algoritma kriptografi.  
2. Mendokumentasikan proses implementasi proyek ke dalam repository Git.  
3. Menyusun laporan teknis hasil proyek akhir.  

---

## 2. Dasar Teori
ERC20 merupakan standar token pada blockchain Ethereum yang mendefinisikan sekumpulan fungsi dan event wajib seperti transfer, balanceOf, approve, dan transferFrom. Standar ini memastikan token dapat berinteraksi secara kompatibel dengan berbagai dompet digital, decentralized exchange (DEX), dan smart contract lain. TinyCoin ERC20 adalah implementasi sederhana dari token ERC20 yang biasanya digunakan untuk pembelajaran, simulasi, atau proyek kecil guna memahami mekanisme dasar aset digital di jaringan Ethereum.

Keamanan dan keandalan TinyCoin ERC20 bergantung pada prinsip kriptografi kunci publik dan fungsi hash yang digunakan oleh Ethereum. Setiap transaksi token divalidasi melalui tanda tangan digital berbasis ECDSA, di mana pemilik alamat Ethereum menandatangani transaksi menggunakan kunci privatnya. Selain itu, Ethereum menggunakan hash Keccak-256 untuk menjamin integritas data transaksi dan smart contract, sehingga perubahan data dapat terdeteksi oleh jaringan.

Dalam implementasinya, TinyCoin ERC20 dijalankan di atas Ethereum Virtual Machine (EVM) yang bersifat deterministik, artinya setiap node akan menghasilkan hasil yang sama untuk eksekusi smart contract. Konsep seperti gas fee digunakan untuk mencegah penyalahgunaan sumber daya dan serangan spam. Dengan memahami standar ERC20 dan mekanisme kriptografi yang mendasarinya, pengembang dapat membangun token yang aman, interoperabel, dan sesuai dengan ekosistem blockchain Ethereum.

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
- Pertanyaan 1:   
- Pertanyaan 2: 
- Pertanyaan 3: 
)
---

## 8. Kesimpulan
Berdasarkan hasil percobaan pembuatan dan pengujian TinyCoin ERC20, dapat disimpulkan bahwa standar ERC20 memudahkan pengembangan token yang kompatibel dengan berbagai layanan di ekosistem Ethereum. Percobaan menunjukkan bahwa mekanisme tanda tangan digital dan validasi transaksi pada EVM mampu menjaga keamanan serta integritas transfer token. Dengan demikian, TinyCoin ERC20 efektif digunakan sebagai media pembelajaran untuk memahami smart contract dan teknologi blockchain.

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
