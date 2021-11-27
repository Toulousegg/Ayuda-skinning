import cv2
import numpy as np
import os

direccion = 'D:/proyectos/ayuda skinning/Images'

original = os.listdir(direccion)

#esto deberia leer muchos archivos y darselos al programa
images = cv2.imread (original)
(alto, ancho) = images.shape

#lo que quiero hacer aca es que tome el tamaño original de las imagenes para que las divida a la mitad
#def original_sizes():
    #cv2.supongo que aquí debería ir algo pero no se que, voy a ver el curso de cv2 y numpy para saber que hacer

#quiero que esto use el tamaño original de la imagen y que la divida a la mitad
#def resize():
#    img = cv2.imread(all)
#    resize = cv2.resize (img, dsize=(original/2))

print(images('alto={}, ancho={}'.format (alto, ancho)))