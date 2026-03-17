import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/home/umark135/Kuliah Umark/image/otak.jpg', cv2.IMREAD_GRAYSCALE)

bright = cv2.add(img, 50)
contrast = cv2.convertScaleAbs(img, alpha=1.5, beta=0)
negative = 255 - img

plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')
plt.show()

plt.imshow(bright, cmap='gray')
plt.title("Brightness")
plt.axis('off')
plt.show()

plt.imshow(contrast, cmap='gray')
plt.title("Contrast")
plt.axis('off')
plt.show()

plt.imshow(negative, cmap='gray')
plt.title("Negative")
plt.axis('off')
plt.show()