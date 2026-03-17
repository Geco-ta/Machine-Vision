import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/home/umark135/Kuliah Umark/image/otak.jpg')
rows, cols = img.shape[:2]

M = np.float32([[1,0,100],[0,1,50]])
translate = cv2.warpAffine(img,M,(cols,rows))

R = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
rotate = cv2.warpAffine(img,R,(cols,rows))

scale = cv2.resize(img,None,fx=1.5,fy=1.5)
flip = cv2.flip(img,1)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis('off')
plt.show()

plt.imshow(cv2.cvtColor(translate,cv2.COLOR_BGR2RGB))
plt.title("Translate")
plt.axis('off')
plt.show()

plt.imshow(cv2.cvtColor(rotate,cv2.COLOR_BGR2RGB))
plt.title("Rotate")
plt.axis('off')
plt.show()

plt.imshow(cv2.cvtColor(scale,cv2.COLOR_BGR2RGB))
plt.title("Scaling")
plt.axis('off')
plt.show()

plt.imshow(cv2.cvtColor(flip,cv2.COLOR_BGR2RGB))
plt.title("Flip")
plt.axis('off')
plt.show()