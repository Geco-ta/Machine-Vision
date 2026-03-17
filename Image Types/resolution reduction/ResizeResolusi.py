import cv2
import matplotlib.pyplot as plt
import pandas as pd

img = cv2.imread("/home/umark135/Kuliah Umark/image/otak.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

resize_img = cv2.resize(img_rgb,(256,256))

# simpan gambar
cv2.imwrite("/home/umark135/Kuliah Umark/gambar_resize.png", cv2.cvtColor(resize_img, cv2.COLOR_RGB2BGR))

# simpan matriks
pd.DataFrame(resize_img[:,:,0]).to_excel("/home/umark135/Kuliah Umark/matrix_resize.xlsx", index=False)

print("Resize dan matriks berhasil disimpan")

plt.imshow(resize_img)
plt.title("Resize 256x256")
plt.axis("off")
plt.show()
