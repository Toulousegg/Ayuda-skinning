from PIL import Image
import os
import pathlib 
import cv2

direccion = 'D:/proyectos/ayuda skinning/Images'
imagen_name = os.listdir(direccion)

# Nota de lo que aprendí: los bucles sirven para realizar una tarea una y otra vez hasta que se le diga que pare por una condición (las condiciones
# pueden ser tanto 'BREAK' como 'CONTINUE', el break termina por completo el bucle, el continue solo ignora tal cosa, puede ser un bucle While o bucle for
# las dos son muy parecidas y sinceramente no conozco que diferencias tendrán entre ellas.#

for imagen_name in imagen_name:
    image = os.path.join(direccion, imagen_name)
    imagen_to_resize = Image.open(image, 'r')
    ancho, alto = Image.size
    Image.size = Image.resize((ancho/2, alto/2))
    #GUARDADO
    Image.save('Redimensionada')

#Esto es para que cuando quiera redimensionar más de una imagen cambie su nombre
    #if images

    if '@2x' not in imagen_name:
        break