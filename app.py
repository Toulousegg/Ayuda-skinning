from PIL import Image
import os
import pathlib 
import cv2

#Esto es una ejemplo de dirección
direccion = 'D:/proyectos/ayuda skinning/Images'
files = os.listdir(direccion)
a = 0 

# Nota de lo que aprendí: los bucles sirven para realizar una tarea una y otra vez hasta que se le diga que pare por una condición (las condiciones
# pueden ser tanto 'BREAK' como 'CONTINUE', el break termina por completo el bucle, el continue solo ignora tal cosa, puede ser un bucle While o bucle for
# las dos son muy parecidas y sinceramente no conozco que diferencias tendrán entre ellas.#

for files in files:
    #el os.path.join es una función para interactuar con el sistema operativo (SO), esta incluido modulos de utilidad por defecto de Python y proporciona
    # una forma portable de utilizar el sistema operativo, así puedes hacer que tu código corra tanto en MAC, Linux y Windows sin problemas, el módulo 'os.path' 
    # es un submódulo del módulo OS en Python que se utiliza para la manipulación de nombres de rutas comunes, en otras palabras se usa para interactuar con las
    # direcciones de nuestros archivos (o por lo menos eso es lo que entendí), el 'os.path.join' une uno o más componentes de una dirección (supongo) de forma
    # inteligente, Este método concadena varios componentes de ruta con exactamente un separador de directorio ('\') en Windows ('/') en Unix/Linuxdespués de 
    # cada parte no vacía, excepto el último componente de ruta. Se usa siempre que quieras usar las direcciones de los archivos.
    #image = os.path.join(direccion, files) (esto tal parece que no iba acá, iba dentro de image_to_resize)
    imagen_to_resize = Image.open(os.path.join(direccion, files))
    ancho, alto = imagen_to_resize.size
    imagen_to_resize = imagen_to_resize.resize((alto//2, ancho//2))
    #GUARDADO
    #Quiero que se guarde redimensionada(1), redimensionada(2), redimensionada(3)... etc
    imagen_to_resize.save('Redimensionada.png')

#Esto es para que cuando quiera redimensionar más de una imagen elimine el '@2x'
    #if images

    if '@2x' not in files:
        break