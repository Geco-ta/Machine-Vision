import cv2
import matplotlib.pyplot as plt
import pandas as pd

img = cv2.imread("/home/umark135/Kuliah Umark/image/otak.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# simpan gambar
cv2.imwrite("/home/umark135/Kuliah Umark/gambar_original.png", img)

# simpan matriks RGB ke excel
with pd.ExcelWriter("/home/umark135/Kuliah Umark/matrix_original.xlsx") as writer:
    pd.DataFrame(img_rgb[:,:,0]).to_excel(writer, sheet_name="Red", index=False)
    pd.DataFrame(img_rgb[:,:,1]).to_excel(writer, sheet_name="Green", index=False)
    pd.DataFrame(img_rgb[:,:,2]).to_excel(writer, sheet_name="Blue", index=False)

print("Gambar dan matriks original berhasil disimpan")

plt.imshow(img_rgb)
plt.title("Gambar Asli")
plt.axis("off")
plt.show()
