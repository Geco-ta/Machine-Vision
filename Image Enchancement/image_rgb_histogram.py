import cv2
import matplotlib.pyplot as plt

image = cv2.imread('/home/umark135/Kuliah Umark/image/jalan.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title('Citra Berwarna (RGB)')
plt.axis('off')

plt.subplot(1,2,2)
colors = ('r', 'g', 'b')
channels = (0, 1, 2)

for i, color in zip(channels, colors):
    hist = cv2.calcHist([image_rgb], [i], None, [256], [0,256])
    plt.plot(hist, color=color, label=f'Kanal {color.upper()}')

plt.title('Histogram RGB')
plt.xlabel('Intensitas Pixel')
plt.ylabel('Jumlah Pixel')
plt.legend()
plt.xlim([0,256])

plt.tight_layout()
plt.show()