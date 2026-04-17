import cv2
import matplotlib.pyplot as plt

image = cv2.imread('/home/umark135/Kuliah Umark/image/jalan.jpg', 0)
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.title('Citra Grayscale')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title('Histogram Citra')
plt.plot(histogram)
plt.xlim([0,256])
plt.show()