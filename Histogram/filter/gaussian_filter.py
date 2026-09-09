import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/home/umark135/Kuliah Umark/image/jalan.jpg', 0)

g1 = cv2.GaussianBlur(img, (3,3), 0.5)
g2 = cv2.GaussianBlur(img, (5,5), 1.0)
g3 = cv2.GaussianBlur(img, (9,9), 2.0)

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title('Asli')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(g1, cmap='gray')
plt.title('Sigma 0.5')
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(g2, cmap='gray')
plt.title('Sigma 1.0')
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(g3, cmap='gray')
plt.title('Sigma 2.0')
plt.axis('off')

plt.show()