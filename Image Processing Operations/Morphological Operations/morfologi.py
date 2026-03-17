import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/home/umark135/Kuliah Umark/image/otak.jpg',0)

_, binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(binary,kernel,iterations=1)
dilation = cv2.dilate(binary,kernel,iterations=1)
opening = cv2.morphologyEx(binary,cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(binary,cv2.MORPH_CLOSE,kernel)

plt.imshow(binary,cmap='gray')
plt.title("Binary")
plt.axis('off')
plt.show()

plt.imshow(erosion,cmap='gray')
plt.title("Erosion")
plt.axis('off')
plt.show()

plt.imshow(dilation,cmap='gray')
plt.title("Dilation")
plt.axis('off')
plt.show()

plt.imshow(opening,cmap='gray')
plt.title("Opening")
plt.axis('off')
plt.show()

plt.imshow(closing,cmap='gray')
plt.title("Closing")
plt.axis('off')
plt.show()