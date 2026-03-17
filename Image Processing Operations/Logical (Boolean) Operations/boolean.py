import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('/home/umark135/Kuliah Umark/image/otak.jpg',0)
img2 = cv2.imread('/home/umark135/Kuliah Umark/image/jalan.jpg',0)

img2 = cv2.resize(img2,(img1.shape[1], img1.shape[0]))

_, img1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
_, img2 = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)

AND = cv2.bitwise_and(img1,img2)
OR = cv2.bitwise_or(img1,img2)
XOR = cv2.bitwise_xor(img1,img2)
NOT = cv2.bitwise_not(img1)

plt.imshow(img1,cmap='gray')
plt.title("Binary 1")
plt.axis('off')
plt.show()

plt.imshow(img2,cmap='gray')
plt.title("Binary 2")
plt.axis('off')
plt.show()

plt.imshow(AND,cmap='gray')
plt.title("AND")
plt.axis('off')
plt.show()

plt.imshow(OR,cmap='gray')
plt.title("OR")
plt.axis('off')
plt.show()

plt.imshow(XOR,cmap='gray')
plt.title("XOR")
plt.axis('off')
plt.show()

plt.imshow(NOT,cmap='gray')
plt.title("NOT")
plt.axis('off')
plt.show()