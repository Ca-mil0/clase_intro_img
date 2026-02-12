import numpy as np
import matplotlib.pyplot as plt

print('paquete numpy importado correctamente')

t=255-np.array([[255, 255, 255],
               [0,255,0],
               [0,255,0],
               [0,255, 0]])

b=np.array([[255],
           [255],
        [255],
           [255]])

A=np.array([[233, 0, 233], 
           [0, 100, 0],
           [0, 0, 0],
           [0, 194, 0]])

#print(t)
#print(t.shape)

#plot figura
plt.figure(figsize=(5,5))
plt.imshow(t, cmap='gray', vmin=0, vmax=255)



#plot figura de matrices concadenadas horizontalmente

esppq =np.ones((4,1))*255 #crea una matriz de puros 1 y lo multimplica por 255 para que simule un espacio entre letras
txt_h=np.concatenate([t , esppq ,A],axis=1)

plt.figure(figsize=(10,5))
plt.imshow(txt_h, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

#Plot figuras de matrices concadenadas verticalmente

esppqv =np.ones((1,3))*255
txt_v=np.concatenate([t , esppqv,A],axis=0)

plt.figure(figsize=(10,5))
plt.imshow(txt_v, cmap='gray', vmin=0, vmax=255)
plt.axis('off')
plt.show()

