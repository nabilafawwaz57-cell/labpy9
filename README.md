# 📘 LAPORAN LATIHAN PRATIKUM 9
Nama : Nabila Fawwaz Nurliah

NIM : 312510255

Kelas : TI.25.A.2

Pratikum : 9

MATKUL : Pengantar Pemograman

Dosen : Agung Nugroho, S.Kom., M.Kom.

# 🧩 Validasi Form Input Menggunakan Python
# 📝 1. Pendahuluan

* Perkembangan teknologi informasi 💻 mendorong penggunaan sistem pendaftaran secara online.

* Untuk meminimalisir kesalahan data yang dimasukkan oleh pengguna, diperlukan proses validasi input sebelum data diproses lebih lanjut.

* Program ini dibuat menggunakan bahasa pemrograman Python sebagai solusi sederhana dalam melakukan validasi data pendaftaran.

# 🎯 2. Tujuan Program

Tujuan dari pembuatan program ini adalah:

1. ✅ Memvalidasi nama lengkap agar hanya berisi huruf.

2. 📞 Memvalidasi nomor telepon agar hanya berisi angka.

3. 📧 Memvalidasi email agar memiliki format dasar yang benar.

4. ⚠️ Menampilkan pesan kesalahan jika data tidak sesuai.

5. 🎉 Menampilkan pesan Data pendaftaran valid jika semua input benar.

# 📋 3. Ketentuan Validasi
```
| 🔍 Data Input    | 📌 Aturan Validasi              |
| ---------------- |-------------------------------   |
| 👤 Nama Lengkap  | Hanya huruf dan spasi           |
| 📞 Nomor Telepon | Hanya angka                     |
| 📧 Email         | Mengandung karakter `@` dan `.` |
```

# 🛠️ 4. Alat & Bahasa Pemrograman
* 🐍 Bahasa Pemrograman : Python
* 🧠 Konsep yang Digunakan :
  * String
  * Percabangan (if)
  * Boolean
  * Input & Output

# 💻 5. Source Code Program
```
nama = input("Masukkan nama lengkap: ")
telepon = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

valid = True

if not nama.replace(" ", "").isalpha():
    print("❌ Error: Nama harus hanya berisi huruf.")
    valid = False

if not telepon.isdigit():
    print("❌ Error: Nomor telepon harus hanya berisi angka.")
    valid = False

if "@" not in email or "." not in email:
    print("❌ Error: Email tidak valid.")
    valid = False

if valid:
    print("✅ Data pendaftaran valid")
```

# 🧪 6. Contoh Pengujian Program
  # ✍️ Input
  ```
Masukkan nama lengkap: John Doe
Masukkan nomor telepon: 08123456789
Masukkan email: john@gmail.com
```

# 📤 Output
```
✅ Data pendaftaran valid
```

# 📊 7. Hasil dan Pembahasan
Berdasarkan hasil pengujian, program mampu:
* 🔎 Mendeteksi kesalahan input pada nama, nomor telepon, dan email.
* ⚠️ Menampilkan pesan error sesuai jenis kesalahan.
* 🎯 Menampilkan pesan keberhasilan apabila seluruh data valid.

# 🧾 8. Kesimpulan
Program validasi form input ini berhasil dibuat dan berjalan dengan baik sesuai tujuan yang diharapkan.
Program ini dapat dijadikan dasar untuk pengembangan sistem pendaftaran online yang lebih kompleks di masa mendatang 🚀.
