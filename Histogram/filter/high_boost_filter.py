import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/home/umark135/Kuliah Umark/image/jalan.jpg', 0)

blur = cv2.GaussianBlur(img, (5,5), 1.0)

A1 = 1.2
A2 = 1.5
A3 = 2.0

hb1 = cv2.addWeighted(img, A1, blur, -0.2, 0)
hb2 = cv2.addWeighted(img, A2, blur, -0.5, 0)
hb3 = cv2.addWeighted(img, A3, blur, -1.0, 0)

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(hb1, cmap='gray')
plt.title('A = 1.2')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(hb2, cmap='gray')
plt.title('A = 1.5')
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(hb3, cmap='gray')
plt.title('A = 2.0')
plt.axis('off')

plt.show()