import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/home/umark135/Kuliah Umark/image/jalan.jpg', 0)

mean3 = cv2.blur(img, (3,3))
mean5 = cv2.blur(img, (5,5))
mean7 = cv2.blur(img, (7,7))

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title('Asli')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(mean3, cmap='gray')
plt.title('Mean 3x3')
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(mean5, cmap='gray')
plt.title('Mean 5x5')
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(mean7, cmap='gray')
plt.title('Mean 7x7')
plt.axis('off')

plt.show()