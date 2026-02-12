import numpy as np

def img_letra(lt):
    if lt=='a':
        return np.array ([
            [0, 0, 0], 
           [0, 255, 0],
           [0, 0, 0],
           [0, 255, 0]])
    elif lt=='t':
        return np.array([
            [255, 255, 255],
               [0,255,0],
               [0,255,0],
               [0,255, 0]])
    
    else:
        raise ValueError('letra no encontrada')
    
def img_letras(lts):
    letras