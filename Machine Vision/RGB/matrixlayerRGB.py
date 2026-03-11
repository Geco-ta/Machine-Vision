import cv2
import matplotlib.pyplot as plt
import pandas as pd

img = cv2.imread("/home/umark135/Kuliah Umark/image/otak.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

R = img_rgb[:,:,0]
G = img_rgb[:,:,1]
B = img_rgb[:,:,2]

# membuat layer
red_layer = img_rgb.copy()
red_layer[:,:,1] = 0
red_layer[:,:,2] = 0

green_layer = img_rgb.copy()
green_layer[:,:,0] = 0
green_layer[:,:,2] = 0

blue_layer = img_rgb.copy()
blue_layer[:,:,0] = 0
blue_layer[:,:,1] = 0

# simpan gambar
cv2.imwrite("/home/umark135/Kuliah Umark/gambar_red.png", cv2.cvtColor(red_layer, cv2.COLOR_RGB2BGR))
cv2.imwrite("/home/umark135/Kuliah Umark/gambar_green.png", cv2.cvtColor(green_layer, cv2.COLOR_RGB2BGR))
cv2.imwrite("/home/umark135/Kuliah Umark/gambar_blue.png", cv2.cvtColor(blue_layer, cv2.COLOR_RGB2BGR))

# simpan matriks
pd.DataFrame(R).to_excel("/home/umark135/Kuliah Umark/matrix_red.xlsx", index=False)
pd.DataFrame(G).to_excel("/home/umark135/Kuliah Umark/matrix_green.xlsx", index=False)
pd.DataFrame(B).to_excel("/home/umark135/Kuliah Umark/matrix_blue.xlsx", index=False)

print("Layer RGB dan matriks berhasil disimpan")

plt.imshow(red_layer)
plt.title("Red Layer")
plt.axis("off")
plt.show()

plt.imshow(green_layer)
plt.title("Green Layer")
plt.axis("off")
plt.show()

plt.imshow(blue_layer)
plt.title("Blue Layer")
plt.axis("off")
plt.show()

