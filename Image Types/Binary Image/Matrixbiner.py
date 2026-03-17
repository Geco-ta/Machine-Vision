import cv2
import matplotlib.pyplot as plt
import pandas as pd

img = cv2.imread("/home/umark135/Kuliah Umark/image/otak.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)

# simpan gambar
cv2.imwrite("/home/umark135/Kuliah Umark/gambar_binary.png", binary)

# simpan matriks
pd.DataFrame(binary).to_excel("/home/umark135/Kuliah Umark/matrix_binary.xlsx", index=False)

print("Citra binary dan matriks berhasil disimpan")

plt.imshow(binary, cmap='gray')
plt.title("Citra Biner")
plt.axis("off")
plt.show()
