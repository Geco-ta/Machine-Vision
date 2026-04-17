import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('/home/umark135/Kuliah Umark/image/jalan.jpg', 0)

dark = cv2.convertScaleAbs(image, alpha=0.5, beta=0)
bright = cv2.convertScaleAbs(image, alpha=1.5, beta=50)
low_contrast = cv2.normalize(image, None, alpha=100, beta=150, norm_type=cv2.NORM_MINMAX)
high_contrast = cv2.equalizeHist(image)

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.imshow(dark, cmap='gray')
plt.title('1. Citra Gelap (Under Exposed)')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(bright, cmap='gray')
plt.title('2. Citra Terang (Over Exposed)')
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(low_contrast, cmap='gray')
plt.title('3. Kontras Rendah (Low Contrast)')
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(high_contrast, cmap='gray')
plt.title('4. Kontras Tinggi (High Contrast)')
plt.axis('off')

plt.tight_layout()
plt.show()