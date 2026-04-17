import cv2
import matplotlib.pyplot as plt

image = cv2.imread('/home/umark135/Kuliah Umark/image/jalan.jpg', 0)
histogram = cv2.calcHist([image], [0], None, [256], [0,256])

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.imshow(image, cmap='gray')
plt.title('Citra Grayscale')
plt.axis('off')

plt.subplot(1,2,2)
plt.plot(histogram, color='black')
plt.title('Histogram Grayscale')
plt.xlabel('Intensitas Pixel')
plt.ylabel('Jumlah Pixel')
plt.xlim([0,256])

plt.tight_layout()
plt.show()