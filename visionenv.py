import numpy as np
import matplotlib.pyplot as plt

print('paquete numpy importado correctamente')

a=np.array([[255, 0, 255],
           [255, 0, 255],
           [255, 0, 255],
           [255, 0, 255]])

b=np.array([[0, 255, 0],
           [0, 255, 0],
           [0, 255, 0],
           [0, 255, 0]])

A=np.array([[233, 0, 233],
           [0, 100, 0],
           [0, 0, 0],
           [0, 194, 0]])

print(a)
print(a.shape)

plt.figure(figsize=(5,5))
plt.imshow(A, cmap='gray', vmin=0, vmax=255)
plt.show()