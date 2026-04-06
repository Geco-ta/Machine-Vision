import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar
image = cv2.imread("/home/umark135/Kuliah Umark/image/jalan.jpg")

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ======================
# 1. Binerisasi
# ======================
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Tampilkan hasil biner
plt.figure()
plt.imshow(binary, cmap='gray')
plt.title("Citra Biner")
plt.axis('off')
plt.show()

# ======================
# 2. Perhitungan Statistik
# ======================
mean = np.mean(binary)
var = np.var(binary)
std = np.std(binary)

print("Mean       :", mean)
print("Varian     :", var)
print("Std Deviasi:", std)