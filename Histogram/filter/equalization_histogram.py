import numpy as np
import matplotlib.pyplot as plt

# ======================
# 1. Data citra (soal)
# ======================
img = np.array([
    [1,3,4,5,6],
    [2,3,4,5,6],
    [2,4,6,7,8],
    [1,4,5,6,7],
    [1,5,6,4,3]
])

# ======================
# 2. Histogram awal
# ======================
hist, bins = np.histogram(img.flatten(), bins=9, range=(0,9))

# ======================
# 3. Hitung PDF & CDF
# ======================
pdf = hist / hist.sum()
cdf = np.cumsum(pdf)

# ======================
# 4. Histogram Equalization (0–8 → ×8)
# ======================
L = 9
new_values = np.round((L-1) * cdf).astype(int)

# mapping nilai lama ke baru
img_eq = np.zeros_like(img)
for i in range(len(hist)):
    img_eq[img == i] = new_values[i]

# ======================
# 5. Plot Histogram
# ======================
plt.figure(figsize=(10,4))

# Histogram asli
plt.subplot(1,2,1)
plt.bar(range(9), hist)
plt.title("Histogram Asli")
plt.xlabel("Intensitas")
plt.ylabel("Frekuensi")

# Histogram hasil equalization
hist_eq, _ = np.histogram(img_eq.flatten(), bins=9, range=(0,9))

plt.subplot(1,2,2)
plt.bar(range(9), hist_eq)
plt.title("Histogram Setelah Equalization")
plt.xlabel("Intensitas")
plt.ylabel("Frekuensi")

plt.tight_layout()
plt.show()

# ======================
# 6. Print hasil matriks
# ======================
print("Citra Asli:\n", img)
print("\nCitra Setelah Equalization:\n", img_eq)