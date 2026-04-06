import cv2
import matplotlib.pyplot as plt

# Baca gambar
image = cv2.imread("/home/umark135/Kuliah Umark/image/jalan.jpg")

# Ubah ke grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ======================
# 1. Tampilkan Grayscale
# ======================
plt.figure()
plt.imshow(gray, cmap='gray')
plt.title("Citra Grayscale")
plt.axis('off')
plt.show()

# ======================
# 2. Histogram Grayscale
# ======================
plt.figure()
plt.hist(gray.flatten(), bins=256)
plt.title("Histogram Grayscale")
plt.xlabel("Intensitas Piksel")
plt.ylabel("Jumlah Piksel")
plt.show()