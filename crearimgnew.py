from utiles import img_letra
import matplotlib.pyplot as plt

lt='j'
img=img_letra(lt)

plt.figure(figsize=(5,5))
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.axis('off')
plt.show()
