from PIL import Image
import os
import pathlib 
import cv2

direccion = 'D:/proyectos/ayuda skinning/Images'
images = os.listdir(direccion)
print(images)

imagen = Image.open(images)
ancho, alto = imagen.size
imagen = imagen.resize((ancho/2, alto/2))
#GUARDADO
imagen.save('transformada')