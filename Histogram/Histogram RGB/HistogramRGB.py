import cv2
import matplotlib.pyplot as plt

# Baca gambar
image = cv2.imread("/home/umark135/Kuliah Umark/image/jalan.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Split channel
r = image_rgb[:, :, 0]
g = image_rgb[:, :, 1]
b = image_rgb[:, :, 2]

# ======================
# 1. Tampilkan Citra RGB
# ======================
plt.figure()
plt.imshow(image_rgb)
plt.title("Citra RGB (Asli)")
plt.axis('off')
plt.show()

# ======================
# 2. Histogram RGB
# ======================
plt.figure()
plt.hist(r.flatten(), bins=256, alpha=0.5, label='Red')
plt.hist(g.flatten(), bins=256, alpha=0.5, label='Green')
plt.hist(b.flatten(), bins=256, alpha=0.5, label='Blue')

plt.title("Histogram RGB")
plt.xlabel("Intensitas Piksel")
plt.ylabel("Jumlah Piksel")
plt.legend()
plt.show()