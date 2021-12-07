from PIL import Image
import os
import pathlib 
import cv2

direccion = 'D:/proyectos/ayuda skinning/Images'
images = os.listdir(direccion)
#print(images)

for imagen_name in images:
    imagen_to_resize = Image.open(direccion + images)
    ancho, alto = imagen.size
    imagen.size = imagen.resize((ancho/2, alto/2))
    #GUARDADO
    imagen.save('transformada')

    if '@2x' not in images:
        break