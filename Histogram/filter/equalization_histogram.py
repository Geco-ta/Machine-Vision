import cv2
import matplotlib.pyplot as plt

# membaca gambar grayscale
img = cv2.imread('/home/umark135/Kuliah Umark/image/jalan.jpg', 0)

# histogram equalization
eq = cv2.equalizeHist(img)

# membuat figure
plt.figure(figsize=(12,6))

# ======================
# CITRA ASLI
# ======================
plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title('Citra Asli')
plt.axis('off')

# histogram asli
plt.subplot(2,2,2)
plt.hist(img.ravel(), 256, [0,256])
plt.title('Histogram Asli')

# ======================
# HASIL EQUALIZATION
# ======================
plt.subplot(2,2,3)
plt.imshow(eq, cmap='gray')
plt.title('Histogram Equalization')
plt.axis('off')

# histogram equalization
plt.subplot(2,2,4)
plt.hist(eq.ravel(), 256, [0,256])
plt.title('Histogram Equalization')

# tampilkan hasil
plt.tight_layout()
plt.show()