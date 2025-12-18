nama = input("Masukkan nama lengkap: ")
telepon = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

valid = True

if not nama.replace(" ", "").isalpha():
    print("Error: Nama harus hanya berisi huruf.")
    valid = False

if not telepon.isdigit():
    print("Error: Nomor telepon harus hanya berisi angka.")
    valid = False

if "@" not in email or "." not in email:
    print("Error: Email tidak valid.")
    valid = False

if valid:
    print("Data pendaftaran valid")