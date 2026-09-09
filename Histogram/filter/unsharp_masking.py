import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/home/umark135/Kuliah Umark/image/jalan.jpg', 0)

blur = cv2.GaussianBlur(img, (5,5), 1.0)

mask = cv2.subtract(img, blur)

sharp1 = cv2.add(img, (0.5 * mask).astype(np.uint8))
sharp2 = cv2.add(img, (1.0 * mask).astype(np.uint8))
sharp3 = cv2.add(img, (1.5 * mask).astype(np.uint8))

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(sharp1, cmap='gray')
plt.title('k = 0.5')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(sharp2, cmap='gray')
plt.title('k = 1.0')
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(sharp3, cmap='gray')
plt.title('k = 1.5')
plt.axis('off')

plt.show()