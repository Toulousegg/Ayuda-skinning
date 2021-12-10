import cv2
from PIL import Image
import numpy as np
import os

direccion = 'D:/proyectos/ayuda skinning/Images'

original = os.listdir(direccion)

#lo que quiero hacer aca es que tome el tamaño original de las imagenes para que las divida a la mitad
def original_sizes():
    images = cv2.imread (original)
    print(images)
    imagen = Image.open(images)
    ancho, alto = imagen.size
    imagen = imagen.resize((ancho/2, alto/2))
    
#quiero que esto use el tamaño original de la imagen y que la divida a la mitad
def resize():
    original_sizes.tamano ()

print ('ESTA VAINA ESTA MALISIMA')