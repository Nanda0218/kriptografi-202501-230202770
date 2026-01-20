# Laporan Praktikum Kriptografi
Minggu ke-: 11 
Topik: [Secret Sharing (Shamir’s Secret Sharing)]  
Nama: [Nanda Erdi Pratama]  
NIM: [230202770]  
Kelas: [5IKRB]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menjelaskan konsep Shamir Secret Sharing (SSS).  
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.  
3. Menganalisis keamanan skema distribusi rahasia.  


---

## 2. Dasar Teori
Teori Relevan Secret Sharing (Shamir’s Secret Sharing)

Secret Sharing adalah teknik kriptografi untuk membagi sebuah rahasia (seperti kata sandi atau kunci enkripsi) menjadi beberapa bagian, yang kemudian dibagikan ke beberapa pihak. Rahasia asli hanya bisa dikembalikan jika sejumlah pihak tertentu bersedia menggabungkan bagian mereka. Shamir's Secret Sharing, yang dirancang oleh Adi Shamir, menggunakan prinsip dasar dari matematika: melalui dua titik dapat ditarik satu garis lurus, melalui tiga titik dapat dibuat satu parabola, dan seterusnya.

Konsep intinya adalah rahasia dianggap sebagai sebuah titik tersembunyi dalam sebuah grafik polinomial. Setiap pihak yang mendapat bagian rahasia sebenarnya mendapatkan satu titik unik dalam grafik tersebut. Jika cukup banyak pihak berkumpul dan menggabungkan titik-titik mereka, mereka dapat menemukan bentuk grafik aslinya dan dengan demikian menemukan rahasia yang tersembunyi di dalamnya. Jika pihak yang berkumpul kurang dari jumlah yang ditentukan, mereka tidak akan memperoleh informasi apa pun tentang rahasia tersebut—bahkan sedikit pun. Sifat ini membuat skema ini sangat aman.

Untuk memastikan perhitungan matematisnya bersih dan akurat, metode ini menggunakan sistem bilangan bulat dalam aritmetika modular (seperti sistem jam yang berputar). Mirip dengan cipher klasik sederhana seperti Caesar cipher yang menggeser huruf dalam alfabet (di mana huruf Z kembali ke A), aritmetika modular memastikan perhitungan tetap berada dalam batasan angka tertentu, mencegah hasil yang tidak terhingga dan menjaga kerahasiaan sempurna dari sistem bagi rahasia ini.

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
from secretsharing import SecretSharer

# Rahasia yang ingin dibagi
secret = "KriptografiUPB2025"

# Bagi menjadi 5 shares, ambang batas 3 (minimal 3 shares untuk rekonstruksi)
shares = SecretSharer.split_secret(secret, 3, 5)
print("Shares:", shares)

# Rekonstruksi rahasia dari 3 shares
recovered = SecretSharer.recover_secret(shares[:3])
print("Recovered secret:", recovered)
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](Screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Keuntungan utama Shamir Secret Sharing (SSS) adalah tidak ada satu pihak pun yang memegang kunci lengkap. Kunci dibagi menjadi beberapa share yang secara individual tidak memiliki makna dan tidak dapat digunakan untuk membuka rahasia. Berbeda dengan membagikan salinan kunci secara langsung, SSS mengurangi risiko kebocoran karena kompromi satu atau beberapa pihak tidak langsung menyebabkan rahasia terbongkar.
- Pertanyaan 2: Threshold (k) menentukan jumlah minimum share yang harus dikumpulkan untuk merekonstruksi rahasia. Nilai ini berfungsi sebagai keseimbangan antara keamanan dan ketersediaan: semakin besar nilai k, semakin sulit bagi penyerang untuk mendapatkan cukup share, namun semakin rendah toleransi terhadap kehilangan share. Dengan demikian, threshold menjadi parameter utama dalam mengontrol tingkat keamanan sistem secret sharing.
- Pertanyaan 3: Salah satu contoh nyata penggunaan SSS adalah pengamanan kunci privat dompet kripto perusahaan. Kunci privat dibagi kepada beberapa eksekutif atau sistem berbeda, dan hanya dapat digunakan jika minimal k pihak menyetujui dan menggabungkan share mereka. Pendekatan ini mencegah penyalahgunaan kunci oleh satu individu dan meningkatkan keamanan aset digital secara signifikan.
)
---

## 8. Kesimpulan
Berdasarkan percobaan, Shamir's Secret Sharing terbukti efektif membagi dan menyembunyikan sebuah rahasia. Rahasia asli hanya berhasil ditemukan kembali ketika cukup banyak pihak menggabungkan bagian mereka, sesuai dengan ketentuan awal. Jika bagian yang dikumpulkan kurang, tidak ada informasi yang bisa diduga tentang rahasia tersebut, sama sekali.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log

```
commit b3bd6bcf949fde5be0c641c67e66f71187af14d6 (HEAD -> main, origin/main, origin/HEAD)
Author: Nanda0218 <nandaerdipratama29@gmail.com>
Date:   Mon Dec 29 21:22:16 2025 +0700

    week11-secret-sharing

```
