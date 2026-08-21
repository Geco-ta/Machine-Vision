import cv2
import numpy as np

# Lokasi gambar
input_file = r"C:\Users\Lenovo\Pictures\Screenshots\ttdDPL.png"

# Lokasi hasil
output_file = r"C:\Users\Lenovo\Pictures\Screenshots\hasilttdDPL.png"

print("=== PENGOLAHAN CITRA GRAYSCALE ===")
print()

# Input dari CMD
batas = int(input("Masukkan batas mentok (0-255): "))
perubahan = int(input("Masukkan nilai tambah/kurang (contoh -80 atau 50): "))

# Validasi batas
if batas < 0 or batas > 255:
    print("ERROR: Batas harus antara 0 sampai 255.")
    input("Tekan ENTER untuk keluar...")
    exit()

# Baca gambar grayscale
img = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("ERROR: Gambar tidak ditemukan!")
    print(input_file)
    input("Tekan ENTER untuk keluar...")
    exit()

# Ubah ke int16 supaya aman saat tambah/kurang
hasil = img.astype(np.int16)

# ============================
# PROSES
# ============================

# Nilai >= batas dibuat 255
hasil[img >= batas] = 255

# Nilai < batas ditambah/dikurangi
hasil[img < batas] = hasil[img < batas] + perubahan

# Jaga supaya tetap pada rentang 0-255
hasil = np.clip(hasil, 0, 255)

# Kembalikan ke uint8
hasil = hasil.astype(np.uint8)

# Simpan gambar
berhasil = cv2.imwrite(output_file, hasil)

print()
print("==============================")

if berhasil:
    print("BERHASIL!")
    print()
    print(f"Nilai >= {batas} -> 255")

    if perubahan < 0:
        print(f"Nilai <  {batas} -> dikurangi {abs(perubahan)}")
    elif perubahan > 0:
        print(f"Nilai <  {batas} -> ditambah {perubahan}")
    else:
        print(f"Nilai <  {batas} -> tidak diubah")

    print()
    print("Hasil disimpan di:")
    print(output_file)
else:
    print("Gagal menyimpan gambar.")

print("==============================")

input("\nTekan ENTER untuk keluar...")
