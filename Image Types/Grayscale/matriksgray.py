import cv2
import matplotlib.pyplot as plt
import pandas as pd

img = cv2.imread("/home/umark135/Kuliah Umark/image/otak.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# simpan gambar
cv2.imwrite("/home/umark135/Kuliah Umark/gambar_grayscale.png", gray)

# simpan matriks
pd.DataFrame(gray).to_excel("/home/umark135/Kuliah Umark/matrix_grayscale.xlsx", index=False)

print("Grayscale dan matriks berhasil disimpan")

plt.imshow(gray, cmap='gray')
plt.title("Grayscale 0-255")
plt.axis("off")
plt.show()
