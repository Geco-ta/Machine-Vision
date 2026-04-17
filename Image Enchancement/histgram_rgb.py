import cv2
import matplotlib.pyplot as plt
image = cv2.imread('/home/umark135/Kuliah Umark/image/jalan.jpg')
colors = ('b','g','r')

for i, col in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [256], [0,256])
    plt.plot(hist, color=col)

plt.title('Histogram RGB')
plt.xlim([0,256])
plt.show()