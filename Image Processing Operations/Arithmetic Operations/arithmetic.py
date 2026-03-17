import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('/home/umark135/Kuliah Umark/image/otak.jpg')
img2 = cv2.imread('/home/umark135/Kuliah Umark/image/jalan.jpg')

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

add = cv2.add(img1, img2)
sub = cv2.subtract(img1, img2)

plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("Image 1")
plt.axis('off')
plt.show()

plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("Image 2")
plt.axis('off')
plt.show()

plt.imshow(cv2.cvtColor(add, cv2.COLOR_BGR2RGB))
plt.title("Addition")
plt.axis('off')
plt.show()

plt.imshow(cv2.cvtColor(sub, cv2.COLOR_BGR2RGB))
plt.title("Subtraction")
plt.axis('off')
plt.show()